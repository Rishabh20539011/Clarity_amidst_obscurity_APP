from tempfile import NamedTemporaryFile

import streamlit as st
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from tools import ImageCaptionTool, ObjectDetectionTool
from gtts import gTTS
from playsound import playsound
from io import BytesIO

##############################
### initialize agent #########
##############################
tools = [ImageCaptionTool(), ObjectDetectionTool()]

conversational_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)

llm = ChatOpenAI(
    openai_api_key='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',    
    temperature=0,
    model_name="gpt-3.5-turbo"
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
    user_question = st.text_input('Ask a question about your image:')

    ##############################
    ### compute agent response ###
    ##############################
    with NamedTemporaryFile(dir='.') as f:
        f.write(file.getbuffer())
        image_path = f.name

        # write agent response
        if user_question and user_question != "":
            with st.spinner(text="In progress..."):
                # response = agent.run('{}, this is the image path: {}'.format(user_question, image_path))
                response = agent.run('{},{}'.format(user_question, image_path))

                speech = gTTS(response, lang = 'en', slow = False)
                # st.audio(speech,sample_rate = 44100)
                st.write(response)
                # speech.save('speech.mp3')
                # print('speech------------------------',speech)

                # audio_file = open('speech.mp3', 'rb')
                # audio_bytes = audio_file.read()
                # st.audio(audio_bytes, format='audio/mp3')
                mp3_fp=BytesIO()
                speech.write_to_fp(mp3_fp)
                mp3_fp.seek(0)
                st.audio(mp3_fp)
                