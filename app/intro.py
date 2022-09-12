import streamlit as st
from pages.node_edge import *
from time import time
from convokit import Corpus


# ----------------------- PAGES --------------------------------
    # ------------------------INTRO-------------------------------


def intro():
    import streamlit as st
    st.sidebar.success("Select the annotation type")
    st.markdown("Annotation guidlines")
    info_page()

    # -------------------------SUB-PROBLEMS--------------------------


def sub_problem_page():
    from pages.sub_problem import sub_problem_work
    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    sub_problem_work()

    # ---------------------------NODE-EDGE-PAGE-----------------------


def node_edge_page():
    from pages.node_edge import node_edge_work
    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
    node_edge_work()

    # ---------------------------INFORMATION----------------------------


def info_page():
    from pages.info import info_page
    st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
    info_page()


page_names_to_funcs = {
    "—": intro,
    " Nodes and Edges ": node_edge_page,
    "Sub Problems": sub_problem_page,
    "Information": info_page
}

demo_name = st.sidebar.selectbox(
    "Choose your work", page_names_to_funcs.keys(), key="demo_seelct")
page_names_to_funcs[demo_name]()
