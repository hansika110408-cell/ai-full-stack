from ollama import chat
import streamlit as st

st.set_page_config(page_title="Llamabot App",page_icon="")
st.title("Llama-here to talk")

personality="You are a freindly and patient tutor named llama.Answer warmly keep answers with one sentence."

personality_2="You are a police officer answer my questions accordingly"
if "history" not in st.session_state:
    st.session_state.history=[{"role":"system","content":personality}]

if "toast_msg" not in st.session_state:
    st.session_state.toast_msg=None

if st.session_state.toast_msg:
    st.toast(st.session_state.toast_msg[0],icon=st.session_state.toast_msg[1])
    st.session_state.toast_msg=None

with st.sidebar:
    st.header("Chat Controls")
    if st.button("Clear Chat",type="primary"):
        st.session_state.history=[{"role":"system","content":personality}]
        st.session_state.toast_msg=("Chat cleared successfully!","🧺")
        st.rerun()
    if st.button("Change personality"):
        st.session_state.history[0]["content"]=personality_2
        st.session_state.toast_msg=("Bot personality changed successfully!","🎭")
        st.rerun()

    if st.button("Change personality"):
            st.session_state.history[0]["content"]=personality
            st.session_state.toast_msg=("Bot personality resetted successfully!","🎭")
            st.rerun()


with st.chat_message("assistant"):
    st.write("Hello!I'am Llama.Ask something to get started.")

for msg in st.session_state.history[1:]:
    with st.chat_message(msg['role']):
        st.write(msg['content'])

question=st.chat_input("Type Something...")
if question:
    st.session_state.history.append({"role":"user","content":question})

    with st.chat_message("user"):
        st.write(question)
    try:

        with st.spinner("Thinking..."):
            response=chat(model="llama3.2",messages=st.session_state.history)
        reply=response["message"]["content"]
        st.session_state.history.append({"role":"assistant","content":reply})

        with st.chat_message("assistant"):
            st.write(reply)

    except Exception as e:
        st.write("Ollama is not working try again.")
