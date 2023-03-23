import openai
import streamlit as st


def go():
    with st.spinner('Wait for it...'):
        openai.api_key = key
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="256x256"
        )
        st.session_state.images.insert(0, response['data'][0]['url'])
        st.session_state.prompts.insert(0, prompt)


if 'prompts' not in st.session_state:
    st.session_state.prompts = []
    st.session_state.images = []

key = st.text_input("API Key", type="password", help="Your openAI API Key")
prompt = st.text_area("Prompt")
button = st.button('GO', on_click=go)

for i in range(len(st.session_state.prompts)):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write(st.session_state.prompts[i])
    with col2:
        st.image(st.session_state.images[i])
