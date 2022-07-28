import streamlit as st
import copy
import pandas as pd
from convokit import Corpus
from time import time
from utils import display_node_box
from utils import print_resource_section
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


# mains = load_data("data")
# ------------------CALLBAKCS----------------------------------------------

# def user_button_callback(selected_user):
#     st.session_state["current_user"] = selected_user
def user_submit_callback(selected_user):
    st.session_state["current_user"] = selected_user
    if st.session_state["current_user"] != None:
        st.success("Welcome to Hogwarts explain their task here before going on further!!    " +
                   str(st.session_state["current_user"]))


def resource_button_callback():
    st.session_state["reader_consent"] = True

# ---------------------SESSION STATE VARIABLES-------------------------------------


if "current_user" not in st.session_state:
    st.session_state["current_user"] = None
    st.session_state["reader_consent"] = False
    st.session_state["user_corpus"] = load_data("data")


# Extra variables :


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
                print_resource_section()
                reader_consent = st.button(
                    "I've done my homework Hagrid", on_click=resource_button_callback)

        else:
            display_node_box()
        # display_node_box()


if __name__ == "__main__":
    main()
