import streamlit as st
import copy
import pandas as pd
from convokit import Corpus
from time import time
from utils import print_resource_section_edges, print_resource_section_nodes, node_box_without_form
from utils import user_info, get_user_corpus

# Each of them will be having their own data folder where there is their down corpus that they are dealing with.

# ------------------------LOADING THE DATA------------------------------------


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_data(ROOT_DIR):
    start = time()
    corpus = Corpus(ROOT_DIR)
    total = time() - start
    st.write("Time elapsed", total)
    return corpus


# ------------------CALLBAKCS----------------------------------------------

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


# ---------------------SESSION STATE VARIABLES-------------------------------------


if "current_user" not in st.session_state:
    st.session_state["current_user"] = None
    st.session_state["reader_consent"] = False
    st.session_state["user_corpus"] = load_data("data")


# The corpus that will update itself through all the changes
if "user_corpus" not in st.session_state:
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


# ----------------------------MAIN-------------------------------------------

def main():
    # --------------USER FORM------------------------------------------------
    if st.session_state["current_user"] == None:
        with st.container():
            st.write("### Who would this wizard be?")
            # change the list here when needed
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
            # st.session_state["current_user"] = selected_user

        # ---------------------RESOURCE SECTION--------------------------------------
    if st.session_state["current_user"] != None:
        # should come up everytime a new conversation comes up
        if st.session_state["reader_consent"] == False:
            with st.container():
                print_resource_section_nodes()
                button = st.button("Read Next")
                if button:
                    print_resource_section_edges()
                    reader_consent = st.button(
                        "I've done my homework Hagrid", on_click=resource_button_callback)

        else:
            st.write("#### Conversation progress")
            conv_bar = st.progress(0)
            conv_bar.progress(2*st.session_state["conv_counter"])

            # st.write("con_counter", st.session_state["conv_counter"])
            if st.session_state["conv_counter"] != len(static_conv_list):
                # st.write(st.session_state["current_conv"].id)

                if st.session_state["utt_counter"] != len(st.session_state["utt_list"]):
                    # "utt_counter", st.session_state["utt_counter"]
                    # "utt_id",st.session_state["current_utt"].id

                    # display_node_box(st.session_state["current_utt"])
                    node_box_without_form()

                else:
                    conv_button = st.button(
                        "Next Conversation", on_click=inc_conv)

            st.write("#### Utterance Progress")
            utt_bar = st.progress(0.0)
            utt_bar.progress(
                (st.session_state["utt_counter"])/(len(st.session_state["utt_list"])))

            if st.session_state["utt_counter"] != 0:
                st.write(st.session_state["current_conv"].get_utterance(
                    st.session_state["utt_list"][st.session_state["utt_counter"]-1]).meta)


if __name__ == "__main__":
    main()
