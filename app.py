import os
from tempfile import NamedTemporaryFile
import streamlit as st
from langchain.agents import initialize_agent
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from tools import ImageCaptionTool, ObjectDetectionTool
from typing import Optional
from langchain_google_genai import ChatGoogleGenerativeAI

##############################
### initialize agent #########
##############################
tools = [ImageCaptionTool(), ObjectDetectionTool()]

conversational_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)

# Set your API key as an environment variable
os.environ["GOOGLE_API_KEY"] = ""  # Replace with your actual API key

# Configuration for the generative model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

agent = initialize_agent(
    agent="chat-conversational-react-description",
    tools=tools,
    llm=llm,
    max_iterations=5,
    verbose=True,
    memory=conversational_memory,
    early_stopping_method='generate'
)

# set title
st.title('Ask a question to an image')

# set header
st.header("Please upload an image")

# upload file
file = st.file_uploader("", type=["jpeg", "jpg", "png"])

if file:
    # display image
    st.image(file, use_column_width=True)

    # text input
    user_question: Optional[str] = st.text_input('Ask a question about your image:')

    ##############################
    ### compute agent response ###
    ##############################
    with NamedTemporaryFile(dir='.', delete=False) as f:
        f.write(file.getbuffer())
        image_path = f.name

        # write agent response
        if user_question and user_question != "":
            with st.spinner(text="In progress..."):
                response = agent.run(f'{user_question}, this is the image path: {image_path}')
                st.write(response)
