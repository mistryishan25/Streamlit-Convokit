import streamlit as st
import pandas as pd
import convokit
from convokit import Corpus


def display_node_box():
    """

    """

    with st.form("comment"):
        st.write("### Comment #")
        node = st.selectbox('Type', ['Agreement',
                                     'Announcement',
                                     'Answer',
                                     'Appreciation',
                                     'Disagreement',
                                     'Elaboration',
                                     'Humour',
                                     'Negative Reaction',
                                     'Question'], key="Node_1")
        keep_node = st.checkbox(
            'Should we exclude this one?', key="Keep_node")
        sub1 = st.form_submit_button(
            'Submit 1')

# -----------------------------------------------------------------------


def print_resource_section() -> None:
    """

    """
    st.write('''# Resource section''')
    with st.expander("Click to expand info about the sentence categories", expanded=True):
        st.write(
            """
          #### Agreement :
              - Agreeing to the point made before
              - Positive example/experience or confirming or acknowledging the made point
          #### Answer : 
              - Any general response to a Question
              - Many comments underneath a question can be Answers,unless they look more like other options
          #### Appreciation
              - Just praise, appreciation or excitement
              - Has less intent of educating others.

          #### Disagreement
              - comment that is correcting, criticizing, contradicting, or objecting. 
              - can also be an experience or story that expresses disagreement 
          #### Elaboration
              - Adding extra relevant information to the previous comment
              - A good test would be if I just add this to the previous comment, the flow of the idea remains intact.
          #### Humour
              - A joke, piece of SaRcAsM or just silly puns
              - Could be a fun story
              - Intent here is just to have fun, for example if that joke supports then it might belong in other category
          #### Negative Reaction
              - attacking or mocking the commenter, or expressing emotions like disgust, derision, or anger
              - Has no intent of adding value or justification or correction
          #### Question
              - Is it a question or a request seeking forfeedback, help, or other kinds of responses.
              - Remember not every comment that ends with a "?" is a question
              - If it ends with a "?" does not mean it is a question
          """
        )
    with st.expander("Click to expand the relations between the sentences", expanded=True):
        st.write(
            '''
          #### Asking
              - Ask questions of the other person in a conversation to discover information about them, their situation and what they do or do not know.
          #### Informing
              - Providing information to others helps them understand what you understand and enables them to make informed, sensible decisions.
          #### Asserting
              - Asserting is stating something as if it were true.
              -When a person asserts something, they are also sending a message that they do not want to have an argument whether it is true or not.
          #### Proposing
          #### Summarizing
          #### Checking
          #### Building
          #### Including
          #### Excluding
          #### Self-promotion
          #### Supporting
          #### Disagreeing
          #### Avoiding
          #### Challenging
          #### Attacking
          #### Defendin    
          '''
        )


# ----------------------------------------------------------------------


def user_info(main_corpus, user_list_dict):
    """
    Prints out the form and ask for the user.
        Arguments : 
            user_list_dict : The list of users you have in mind
        Returns :
            A list of conversations 
    """

    def user_button_pressed(user_name, main_corpus):
        st.session_state["current_user"] = user_name
        st.session_state["user_corpus"] = get_user_corpus(
            main_corpus, st.session_state["user_list_dict"][st.session_state["current_user"]])

    with st.form("User_identity"):
        users = user_list_dict.keys()
        st.write("### Who would this wizard be?")
        selected_user = st.selectbox("Reveal yourself", users)
        user_submit = st.form_submit_button(
            "Submit", on_click=user_button_pressed, args=[selected_user, main_corpus])
        # if user_submit:
        #     return user_list_dict[st.session_state["current_user"]]


# main = Corpus("data")

def get_user_corpus(main_corpus: convokit.Corpus, user_list: dict) -> convokit.Corpus:
    user_corpus = main_corpus.filter_conversations_by(
        lambda conv: True if conv.id in user_list else False)
    return user_corpus


# Do tabs for tree structure?
