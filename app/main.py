import streamlit as st
import copy
import pandas as pd
from convokit import Corpus
from time import time
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


# ---------------------SESSION STATE VARIABLES-------------------------------------

if "current_user" not in st.session_state:
    st.session_state["current_user"] = " "

    st.session_state["user_corpus"] = load_data("data")


# ----------------------------MAIN-------------------------------------------

def main():

    with st.form("User_identity"):
        st.write("### Who would this wizard be?")
        selected_user = st.selectbox(
            "Reveal yourself", ["Ron", "Hermoine", "Snape", "Neville", "Harry"])
        user_submit = st.form_submit_button("Submit")
        st.session_state["current_user"] = selected_user

    st.write(st.session_state["current_user"])


if __name__ == "__main__":
    main()
