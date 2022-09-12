
def info_page():
    import streamlit as st
    from utils import print_resource_section_edges, print_resource_section_nodes, print_resource_section_problems




    tab1, tab2, tab3 = st.tabs(["Information_nodes", "Information_edges", "Information_sub_probolems"])

    with tab1:
        print_resource_section_nodes()

    with tab2:
        print_resource_section_edges()

    with tab3:
        print_resource_section_problems()

