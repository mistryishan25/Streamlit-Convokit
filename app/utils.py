import streamlit as st
import pandas as pd

def display_node_box(file_df, update_on_submit):
    """
    Takes in the input dataframe and displays the node container
    """

    with st.form("comment", clear_on_submit=True):
        st.write("Comment #"+str(st.session_state['index_utterances']))
        st.info(file_df.iloc[st.session_state["index_utterances"]][2])
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
            'Submit 1', on_click=update_on_submit(keep_node, node))

def print_resource_section() -> None:
    st.write('''# Resource section''')
    with st.expander("Click to expand info about the sentence categories"):
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
    with st.expander("Click to expand the relations between the sentences"):
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
