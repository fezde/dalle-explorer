import openai
import streamlit as st


def go():
    with st.spinner('Wait for it...'):
        openai.api_key = key
        response = openai.Image.create(
            prompt=prompt,
            n=count,
            size=size
        )
        urls = [x['url'] for x in response['data']]

        st.session_state.images.insert(0, urls)
        st.session_state.prompts.insert(0, prompt)


if 'prompts' not in st.session_state:
    st.session_state.prompts = []
    st.session_state.images = []

key_from_secret = ""
if "API_KEY" in st.secrets:
    print("Using key from secrets")
    key_from_secret = st.secrets["API_KEY"]

key = st.text_input("API Key", type="password", help="Your openAI API Key", value=key_from_secret)
prompt = st.text_area("Prompt")
size = st.selectbox(
    'Size in pixels',
    ("256x256", "512x512", "1024x1024"))
count = st.slider(
    "How many images should be requested",
    value=1,
    min_value=1,
    max_value=10
)
button = st.button('GO', on_click=go)

for i in range(len(st.session_state.prompts)):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write(st.session_state.prompts[i])
    with col2:
        for url in st.session_state.images[i]:
            st.image(url)
