def node_edge_work():
    import streamlit as st
    from utils import node_box_without_form
    from time import time
    from convokit import Corpus
    # --------------------- DATA ----------------------------------------

    @st.cache(suppress_st_warning=True, allow_output_mutation=True)
    def load_data(ROOT_DIR):
        start = time()
        corpus = Corpus(ROOT_DIR)
        total = time() - start
        st.write("Time elapsed", total)
        return corpus

    # ------------------- GLOBAL SESSION STATE VARIABLES ------------------
    if "current_user" not in st.session_state:
        st.session_state["current_user"] = None
        st.session_state["reader_consent"] = False
        st.session_state["user_corpus"] = load_data("data")

    # This is the list of all the ids
    static_conv_list = st.session_state["user_corpus"].get_conversation_ids()

    if "conv_progress" not in st.session_state:
        # to keep track of which index we are currently working on
        st.session_state["conv_counter"] = 4

        # to update the finsihed conversation ids to some central place as log
        st.session_state["conv_progress"] = []

    # current conversation to be stored - The conv object
    if st.session_state["conv_counter"] != len(static_conv_list):
        st.session_state["current_conv"] = st.session_state["user_corpus"].get_conversation(
            static_conv_list[st.session_state["conv_counter"]])

    # it should change everytime a new conversation appears
    if "utt_counter" not in st.session_state:
        # Initial counter to zero
        st.session_state["utt_counter"] = 0

    st.session_state["utt_list"] = st.session_state["current_conv"].get_utterance_ids()

    # the current utterance that is going to change
    st.session_state["current_utt"] = st.session_state["current_conv"].get_utterance(
        st.session_state["utt_list"][st.session_state["utt_counter"]])

    if "progress_utt" not in st.session_state:
        st.session_state["progress_utt"] = 0

    # ----------STATIC VARIABLES---------------------------------
    static_conv_list = st.session_state["user_corpus"].get_conversation_ids()

    # -----------CALLBACKS---------------

    # def exit_callback():
    #     # chnage the parameter : overwrite_exisiting_corpus to true in the end
    #     st.session_state["user_corpus"].dump(overwrite_existing_corpus=True, base_path="data")
    #     st.success("The data has been downloaded. You can close the app now!")

    def user_submit_callback(selected_user):
        st.session_state["current_user"] = selected_user
        if st.session_state["current_user"] != None:
            st.success("Welcome to Hogwarts explain their task here before going on further!! Showed only once    " +
                       str(st.session_state["current_user"]))

    def resource_button_callback():
        st.session_state["reader_consent"] = True

    def inc_conv():
        if st.session_state["conv_counter"] == len(static_conv_list):
            st.balloons()
        else:
            st.session_state["conv_counter"] += 1
            st.write("Conv_counter", st.session_state["conv_counter"])
        # --------------USER FORM------------------------------------------------
        if st.session_state["current_user"] == None:
            with st.container():
                st.write("### Who would this wizard be?")
                # change the list here when needed - using the keys to
                users = ["Ron", "Hermoine", "Neville",
                         "Harry", "Professor Snape", None]
                default_idx = users.index(None)
                selected_user = st.selectbox(
                    "Reveal yourself", users, index=default_idx)
                # st.write(default_idx)
                if selected_user:
                    st.success(str(selected_user) +
                               " , \n you many now enter the Floo Network")
                user_submit = st.button(
                    "Jump right in", on_click=user_submit_callback, args=(selected_user,))

    # ---------------------RESOURCE SECTION--------------------------------------
    st.write("#### Utterance Progress :\t " + str(st.session_state["utt_counter"])+"/"+ str(len(st.session_state["utt_list"])))
    utt_bar = st.progress(0.0)
    utt_bar.progress(
        (st.session_state["utt_counter"])/(len(st.session_state["utt_list"])))

    if st.session_state["conv_counter"] != len(static_conv_list):

        if st.session_state["utt_counter"] != len(st.session_state["utt_list"]):
            node_box_without_form()

      
        st.write("#### Conversation progress  : " + "  " +
                 str((st.session_state["conv_counter"]/len(static_conv_list))*100) + "%")
        st.write(len(static_conv_list))
        conv_bar = st.progress(0)
        # considering that ther are 25
        conv_bar.progress(4*st.session_state["conv_counter"])

    else :
        st.write("Work done!!")
