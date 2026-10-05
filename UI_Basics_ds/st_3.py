import streamlit as st
import time

st.set_page_config(page_title="chatbot app demo")
st.title("Chatbot UI Demo")

# with st.chat_message("user"):
#     st.write("Hello from the user side!")

with st.chat_message("assistant"):
    st.write("Hello from the llama3.2!")

user_message=st.chat_input("type something....")
if user_message:
    with st.chat_message("user"):
        st.write(f"you:{user_message}")
    with st.chat_message("assistant"):
        with st.spinner("thinking..."):
            time.sleep(1.5)
        st.write(f"hey,you wrote: {user_message},but i'm still in development.i cant reply.")