import openai
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

key = st.text_input("API Key")
prompt = st.text_area("Prompt")

col1, col2 = st.columns([1,3])

if st.button('GO'):
    openai.api_key = key
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )
    with col1:
        st.write(prompt)
    with col2:
        st.image(response['data'][0]['url'])
