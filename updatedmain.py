import streamlit as st
# Importing necessary libraries

from langchain_experimental.agents import create_csv_agent
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
from streamlit_chat import message
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)



def init():
    # Load the OpenAI API key from the environment variable
    load_dotenv()
    
    # Test that the API key exists
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    # Setup streamlit page
    st.set_page_config(
        page_title="Your own ChatGPT",
        page_icon="🤖"
    )



def main():
    init()

    chat = ChatOpenAI(temperature=0)

    # Initialize message history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]
       
       # Discribing the main page of the Model
    st.header("Your own ChatGPT 🤖")
    genre = st.radio(
       "***What's the choice of your bot*** ",
       ["Csv Bot", "**Normal Bot**"],
   
       captions = ["Ask questions about your csv", "Converse with the Bot"])
   
    if genre == 'Csv Bot':
        with st.sidebar:
           st.header("Ask your CSV 📈")
        
           csv_file = st.file_uploader("Upload a CSV file",type="csv")
           if csv_file is not None:
   
               agent = create_csv_agent(
                   OpenAI(temperature=0), csv_file, verbose=True)
   
               user_question = st.text_input("Ask a question about your CSV: ")
   
               if user_question is not None and user_question != "":
                   st.session_state.messages.append(HumanMessage(content=user_question))
                   with st.spinner(text="In progress..."):
                           res=agent.run(user_question)
                           response = chat(st.session_state.messages)
                   st.session_state.messages.append(
                   AIMessage(content=res))   
      
    else:
       with st.sidebar:
   
           user_input = st.text_input("Your message: ", key="user_input")
   
           # handle user input
           if user_input:
               st.session_state.messages.append(HumanMessage(content=user_input))
               with st.spinner("Thinking..."):
                   response = chat(st.session_state.messages)
                   st.session_state.messages.append(
                   AIMessage(content=response.content))
    # display message history
    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content, is_user=False, key=str(i) + '_ai')
 

if __name__ == "__main__":
    main()
