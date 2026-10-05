import streamlit as st

st.set_page_config(page_title="Text Input Demo")
st.title("text Input Demo")

name=st.text_input("enter your name:", placeholder="e.g.Hansi")
st.write(f"Hello,{name}!")

secret=st.text_input("enter your password:",type="password")
st.write(f"your password has {len(secret)} characters.")

comments=st.text_area("Any additional comments?",height=150)
st.write(f"Your wrote {len(comments)} characters.")



if st.button("Submit"):
    st.write("you clicked on submit")

show_message=st.checkbox("do you want an extra message?")
if show_message:
    st.write("this is the message.Have a good day")