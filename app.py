import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import dotenv

dotenv.load_dotenv()

st.set_page_config(page_title="Chat with Websites", page_icon="🤖")
st.title("Chat with Websites")

openai_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

def get_content_from_url(url):
    try:
        loader = WebBaseLoader(url)
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        document_chunks = text_splitter.split_documents(documents)
        
        content = "\n".join([chunk.page_content for chunk in document_chunks])
        return content

    except Exception as e:
        st.error(f"Error loading content from the URL: {e}")
        return None

def generate_response(user_input, website_content):
    llm = ChatOpenAI(model=openai_model)  
    prompt = f"""
    The following is content from a website:
    {website_content}

    Based on this content, please answer the user's question:
    {user_input}
    """
    
    ai_message = llm.invoke(prompt)  
    return ai_message.content  

with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

if website_url is None or website_url == "":
    st.info("Please enter a website URL")
else:
    website_content = get_content_from_url(website_url)

    if website_content:
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        user_query = st.chat_input("Type your message here...")

        if user_query:
            st.session_state.chat_history.append(HumanMessage(content=user_query))
            
            for message in st.session_state.chat_history:
                if isinstance(message, HumanMessage):
                    with st.chat_message("Human"):
                        st.write(message.content)
                elif isinstance(message, AIMessage):
                    with st.chat_message("AI"):
                        st.write(message.content)

            with st.chat_message("AI"):
                thinking_message = st.empty()  
                thinking_message.write("Bot is thinking...") 

                with st.spinner("Generating response..."):
                    response = generate_response(user_query, website_content)

                thinking_message.write(response)

                st.session_state.chat_history.append(AIMessage(content=response))

       
