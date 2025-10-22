import google.generativeai as genai
import streamlit as st


api="AIzaSyBlhInmMsi5e8XmaTizYMFzuErRswZ8kuo"


if api:
    genai.configure(api_key=api)
else:
    st.error("your api is not found")

def generate_text(text):
    model=genai.GenerativeModel('models/gemini-2.5-flash')
    response=model.generate_content(text)
    return response.text


if 'messages' not in st.session_state:
    st.session_state.messages=[]


for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if user_input:=st.chat_input("please enter ....."):
    with st.chat_message('user'):
        st.markdown(user_input)
    st.session_state.messages.append({'role':'user','content':user_input})

    with st.chat_message('assistant'):
        message_placeholder=st.empty()
        with st.spinner('Generating response ...'):
            reponse_text=generate_text(user_input)
            message_placeholder.markdown(f'{reponse_text}')

    st.session_state.messages.append({'role':'assistant','content':reponse_text})
