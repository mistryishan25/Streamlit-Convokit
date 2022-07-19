import streamlit as st
import pandas as pd
from convokit import Corpus
from utils import print_resource_section, display_node_box


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_data(ROOT_DIR):
    corpus = Corpus(ROOT_DIR)
    # st.write(corpus.print_summary_stats())
    return corpus


# -------------Upload option-------------
# Do we get the entire folder?


# -------------Session States------------------------
# keep the entire corpus in the session state

# --------User selection from side bar---------------

# Get the entire corpus from an upload

# filter out the conversations based on the person

# Labelling - directly append to the meta data

# Upload the updated corpus to the cloud

def show_sidebar():
    # Using object notation
    add_selectbox = st.sidebar.selectbox(
        " Who is this? ",
        ("User1","User2","User3")
    )

    # Using "with" notation
    with st.sidebar:
        add_radio = st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )


def main():
    corpus = load_data("data")
    if corpus is not None:
        "Corpus is loaded"
        # list = corpus.random_conversation()
        # list._utterance_ids
    else:
        "corpus is none"
    # show_sidebar()


if __name__ == "__main__":
    main()
