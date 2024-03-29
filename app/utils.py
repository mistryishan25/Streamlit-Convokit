import streamlit as st
import pandas as pd
import convokit
from convokit import Corpus
import json


def update_meta(node, edge, keep_node):
    # add node to the meta
    st.session_state["current_utt"].meta["node_label"] = node
    # Update the edge to the meta
    st.session_state["current_utt"].meta["edge_label"] = edge
    # update the keep node info
    st.session_state["current_utt"].meta["keep_node"] = keep_node

    # st.write(st.session_state["current_utt"].meta)

    if st.session_state["utt_counter"] == len(st.session_state["utt_list"])-1:
        st.session_state["utt_counter"] = 0
        st.session_state["conv_counter"] += 1
    else:
        st.session_state["utt_counter"] += 1
        


def update_meta_sub(subproblem):
    st.session_state["current_conv"].meta["subproblem"] = subproblem


def update_next():
    if st.session_state["utt_counter"] == len(st.session_state["utt_list"])-1:
        st.session_state["utt_counter"] = 0
        st.session_state["conv_counter"] += 1
    else:
        st.session_state["utt_counter"] += 1


def exit_callback():
    status_dict = {}
    # chnage the parameter : overwrite_exisiting_corpus to true in the end
    if st.session_state["user_corpus"].dump(name="data",overwrite_existing_corpus=True):
        st.success("The data has been downloaded. You can close the app now!")
    status_dict["conv_done"] = st.session_state["conv_counter"]
    status_dict["test"] = st.session_state["utt_counter"]
    json_object = json.dumps(status_dict)
    with open("status.json", "w") as file:
        file.write(json_object)
    st.success("Added to file")

def next_data_callback():
    if st.session_state["utt_counter"] == len(st.session_state["utt_list"])-1:
        st.session_state["utt_counter"] = 0
        st.session_state["conv_counter"] += 1
    else:
        st.session_state["utt_counter"] += 1


def node_box_sub_problem():

    st.write("#### Previous Comment")
    if st.session_state["utt_counter"] == 0:
        st.info("This is the first comment on the conversation")
    else:
        st.success(st.session_state["current_conv"].get_utterance(
            st.session_state["utt_list"][st.session_state["utt_counter"]-1]).text)

    st.write("#### Current Comment")
    st.success(st.session_state["current_utt"].text)

    subproblem = st.selectbox("Select the subproblem", [
        "Polarization",
        "Hate Speech",
        "Condescension",
        "Ploliteness",
        "Alignment",
        "Trolls", "Cannot Decide"], key="subprob_node")

    but1, but2, but3 = st.columns(3)
    with but1:
        subproblem_submit = st.button(
            "Submit", on_click=update_meta_sub, args=[subproblem])

    with but2:
        st.button("Exit", on_click=exit_callback)

    with but3:
        st.button("next", on_click=next_data_callback)


def node_box_without_form():
    col1, col2 = st.columns(2)

    with col1:
        st.write("#### Previous Comment")
        with st.expander("Click to expand", expanded=True):
            if st.session_state["utt_counter"] == 0:
                st.success("This is the first comment on the conversation")
            else:
                st.success(st.session_state["current_conv"].get_utterance(
                    st.session_state["utt_list"][st.session_state["utt_counter"]-1]).text)

    with col2:
        st.write("#### Current Comment")
        with st.expander("Click to expand", expanded=True):
            st.warning(st.session_state["current_utt"].text)


    st.write("#### Options")
    node = st.selectbox("What do you think is the current comment type? ", ['Agreement',
                                                                            'Announcement',
                                                                            'Answer',
                                                                            'Appreciation',
                                                                            'Disagreement',
                                                                            'Elaboration',
                                                                            'Humour',
                                                                            'Negative Reaction',
                                                                            'Question',
                                                                            'Other',
                                                                            None], key="Node_1",)

    if st.session_state["utt_counter"] != 0:
        st.write("#### Relation b/w them")
        edge = st.selectbox("What kind of realtionship exists between these sentenes", ['Asking',
                                                                                        'Informing',
                                                                                        'Asserting',
                                                                                        'Proposing',
                                                                                        'Summarizing',
                                                                                        'Checking',
                                                                                        'Building',
                                                                                        'Including',
                                                                                        'Excluding',
                                                                                        'Self-promotion',
                                                                                        'Supporting',
                                                                                        'Disagreeing',
                                                                                        'Avoiding',
                                                                                        'Challenging',
                                                                                        'Attacking',
                                                                                        'Defending',
                                                                                        None], key="Edge_1 ")
    else:
        edge = None
    keep_node = st.checkbox('Should we exclude this one?', key="Keep_node")

    but_1,_,_,_,_,_,_,_,but_9 = st.columns(9)
    with but_1:
        submit_box = st.button("Submit", on_click=update_meta, args=[
                            node, edge, keep_node])
    
    with but_9:
        # download button
        st.button("Exit", on_click=exit_callback)



def display_node_box(utt):

    def progress_click(node, edge, keep_node):

        # add node to the meta
        st.session_state["current_utt"].meta["node_label"] = node
        # Update the edge to the meta
        st.session_state["current_utt"].meta["edge_label"] = edge
        # update the keep node info
        st.session_state["current_utt"].meta["keep_node"] = keep_node

        st.write(st.session_state["current_utt"].meta)

        if st.session_state["utt_counter"] == len(st.session_state["utt_list"])-1:
            st.session_state["utt_counter"] = 0
            st.session_state["conv_counter"] += 1
        else:
            st.session_state["utt_counter"] += 1

    """
    Takes in the utterance object and displays information about it.
    """

    with st.form(key=str(st.session_state["current_utt"].id)):
        st.write("#### Previous Comment")
        if st.session_state["utt_counter"] == 0:
            st.success("This is the first comment on the conversation")
        else:
            st.success(st.session_state["current_conv"].get_utterance(
                st.session_state["utt_list"][st.session_state["utt_counter"]-1]).text)
        st.write("#### Current Comment")
        st.warning(str(utt.text))
        node = st.selectbox("What do you think is the current comment type? ", ['Agreement',
                                                                                'Announcement',
                                                                                'Answer',
                                                                                'Appreciation',
                                                                                'Disagreement',
                                                                                'Elaboration',
                                                                                'Humour',
                                                                                'Negative Reaction',
                                                                                'Question',
                                                                                'Other',
                                                                                None], key="Node_1",)
        st.write(node)

        if st.session_state["utt_counter"] != 0:
            st.write("#### Relation b/w them")
            edge = st.selectbox("What kind of realtionship exists between these sentenes", ['Asking',
                                                                                            'Informing',
                                                                                            'Asserting',
                                                                                            'Proposing',
                                                                                            'Summarizing',
                                                                                            'Checking',
                                                                                            'Building',
                                                                                            'Including',
                                                                                            'Excluding',
                                                                                            'Self-promotion',
                                                                                            'Supporting',
                                                                                            'Disagreeing',
                                                                                            'Avoiding',
                                                                                            'Challenging',
                                                                                            'Attacking',
                                                                                            'Defending',
                                                                                            None], key="Edge_1 ")
        else:
            edge = None
        st.write(edge)
        keep_node = st.checkbox(
            'Should we exclude this one?', key="Keep_node")

        sub1 = st.form_submit_button('Submit 1', on_click=progress_click, args=[
                                     node, edge, keep_node])


def print_resource_section_nodes() -> None:
    """

    """
    st.write('''## Resource section - Nodes''')
    with st.expander("Comment types - i.e. Nodes", expanded=True):
        st.write("### Sentence categories")
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


def print_resource_section_edges():
    st.write('''## Resource section - Edges''')
    with st.expander("Relation Types - i.e. Edges", expanded=True):
        st.write(
            '''
          #### Asking
              - Ask questions of the other person in a conversation to discover information about them, their situation and what they do or do not know.
          #### Informing
              - Providing information to others helps them understand what you understand and enables them to make informed, sensible decisions.
          #### Asserting
              - Asserting is stating something as if it were true.
              -When a person asserts something, they are also sending a message that they do not prefer to have an argument whether it is true or not.
          #### Proposing
                - Simply the sentences that invite discussion(good or bad)
                - Intent is to float ideas for discussion or offer solutions to problems
                - A little persuasion to seek agreement is also a kind of a proposal. 
          #### Summarizing
                - Intent is to summarize what you/they said, to show that you understood them correctly and emphasize the main ideas
                - Look for clues like "In other words..", "So what you are saying is..", "To sum it up or conclude"
                - You probably dont want the conversation to go on after this.
          #### Checking
                - A question meant to promote further discovery/discussion
                - In summarization, you agree to some extent with the idea, but checking is neutral in nature.

          #### Building
                - an attempt to be more inclusive, by adding bits to the current idea and giving it coherence.
                - Like "I like your idea. Can we also do this?"
                - Or "Now that we both are on the same page, what do you think should be..."
          #### Including
                - Having people reference others in their comments is your best bet at this one.
                - This is meant to be drawing people in and facilitating the conversation
          #### Excluding
                - ngnioengnen

          #### Self-promotion
                - Intent : Building your own status in the conversation, appear clever, smart.
                - Look for clues of flattery along with usage of first person pronouns(me, I, myself).
                - Note that just because you see an I or self including idea does not make it self promotion by itself.
          #### Supporting
                - giving a reasoning or evidence to show agreement 
          #### Disagreeing
                - having a differing viewpoint, could include a rationale or counter idea or alternate idea suggestions.
                - Pretty obvious : "You're completely wrong" is a strong example
          #### Avoiding
                - Things that can make someone uncomfortable -ex. Harming children/animals are avoided - So if the topic is such then this is your guy
                - Changing the topic or requesting to stop talknig
                - Giving vague answers and skipping detail
          #### Challenging
                - Challenging is not disagreeing, it is like you are just not convinved yet, you have'nt picked sides
                - Look for intents : "Asking the source","Incorrect info", Questioning the logic, providing counter arguments
          #### Attacking 
                - This is not just having a differing opinion as we saw with disagree
                - The intent here is to attack the person/idea and demoralize them
                - Look for sharpened use of language adn power words that show assertions of authority.
          #### Defending
                - Providing justifications to your argument thathas been attacked    
                - Like defneding yourself : "Yes, I know it's irrational, but I want to do it"
                - Or defending someone else : "Leave her alone, that was an unecessary personal attack"      
          '''
        )


def print_resource_section_problems():
    st.write('''## Resource section - Sub-Problems''')
    pass


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


def get_user_corpus(main_corpus: convokit.Corpus, user_list: dict) -> convokit.Corpus:
    user_corpus = main_corpus.filter_conversations_by(
        lambda conv: True if conv.id in user_list else False)
    return user_corpus
