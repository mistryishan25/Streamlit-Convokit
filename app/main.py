import streamlit as st
import pandas as pd
from convokit import Corpus
from utils import print_resource_section, display_node_box, user_info


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_data(ROOT_DIR):
    corpus = Corpus(ROOT_DIR)
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


def main():
    
    #Change later with real values
    if "user_list_dict" not in st.session_state:
        st.session_state["user_list_dict"] = {"Ron": ["9c716m", "9c8amk", "9ca0yk", "9cfz10", "9crqp2", "9d07z8", "9dbjxa", "9dhcnh", "9dhek8"],"Hermoine":[1,2,3,4,5,6], "Harry" : ["Lol"]}
    #Print the form and get the list of conv-ids
    user_conv_list = user_info(st.session_state["user_list_dict"])
    user_conv_list
    corpus = load_data("data")
    assert corpus is not None


if __name__ == "__main__":
    main()
 