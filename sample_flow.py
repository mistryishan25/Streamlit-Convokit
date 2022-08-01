import streamlit as st
from time import time
from convokit import Corpus
# from utils import display_node_box


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_data(ROOT_DIR):
    start = time()
    corpus = Corpus(ROOT_DIR)
    total = time() - start
    st.write("Time elapsed", total)
    return corpus


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
# else:
#     st.balloons()

# it should change everytime a new conversation appears
if "utt_counter" not in st.session_state:
    # Initial counter to zero
    st.session_state["utt_counter"] = 0
    # st.snow()


#
st.session_state["utt_list"] = st.session_state["current_conv"].get_utterance_ids()


# the current utterance that is going to change
st.session_state["current_utt"] = st.session_state["current_conv"].get_utterance(
    st.session_state["utt_list"][st.session_state["utt_counter"]])

if "progress_utt" not in st.session_state:
    st.session_state["progress_utt"] = 0

st.warning(st.session_state["current_utt"].get_conversation().meta["title"])

# -----------------------------------TESTING CALLBACKS -----------------------


def inc_conv():
    if st.session_state["conv_counter"] == len(static_conv_list):
        st.balloons()
    else:
        st.session_state["conv_counter"] += 1
        st.write("Conv_counter", st.session_state["conv_counter"])


def inc_utt():

    if st.session_state["utt_counter"] == len(st.session_state["utt_list"])-1:
        st.session_state["utt_counter"] = 0
        st.session_state["conv_counter"] += 1
    else:
        st.session_state["utt_counter"] += 1
        st.write("Utt_total", len(st.session_state["utt_list"]))

# --------------------------------MAIN--------------------------------

def main():
    st.write("#### Utterance Progress")
    utt_bar = st.progress(0.0)
    utt_bar.progress((st.session_state["utt_counter"])/(
        len(st.session_state["utt_list"])))

    st.write("con_counter", st.session_state["conv_counter"])
    if st.session_state["conv_counter"] != len(static_conv_list):
        st.write(st.session_state["current_conv"].id)

        if st.session_state["utt_counter"] != len(st.session_state["utt_list"]):
            "utt_counter", st.session_state["utt_counter"]

            utt_button = st.button("Next Utt", on_click=inc_utt)

        else:
            conv_button = st.button("Next Conversation", on_click=inc_conv)

        st.write("#### Conversation progress")
        conv_bar = st.progress(0)
        conv_bar.progress(2*st.session_state["conv_counter"])

    # progress for each cconversation
if __name__ == "__main__":
    main()
