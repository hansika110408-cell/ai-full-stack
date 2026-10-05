from ollama import chat
print("WELCOME HERE I AM MOKU THE CHATBOT  I AM HERE TO HELP YOU WITH ANYTHING")
system_msg="you are a IronMan.answer in one sentense"
print("select the personality")
history=[{"role":"system","content":system_msg}]
question_counter=0
while True:
    question=input("You:")
    if question=="":
        print("MOKU🤖:type something to get a answer")
        continue
    if question.lower().strip()=="/history":
        print("---- your conversation so far---")
        if len(history)<2:
            print("nothing here so far!")
            for msg in history[1:]:
                if msg["role"]=="user":
                    speaker="You"
                else:
                    speaker="MOKU🤖"
                print(f"{speaker}:{msg['content']}")
        print("---------------------------")
        print()
        print("NUMBER OF MESSAGES:", len(history))
        continue

    if question.lower().strip()="/personality":
        print("1.super hero 2.singer 3.teacher")

    if question.lower().strip()=="/clear":
        history=[{"role":"system","content":system_msg}]
        print("your history is cleared start a fresh conversation")
        print()
        continue
    

    if question.lower().strip=="help":
        print("-----available commands----")
        print("/history-display conversation history")
        print("/clear-clears chat history")
        print("/help-displays conversation history")
        print("exit-quits the chatbot")
        print("-----------------------------------------")
        print()
        continue

    if question.lower().strip() in { "exit","bye"}:
        print("MOKU🤖: goodbye user see you soon HANSIKA😘😘")
        print(f"you asked{question_counter} questions today.good job!")
        break
    history.append({"role":"user","content":question})
    question_counter+=1
    try:
        response=chat(
            model="llama3.2",
            messages=history
        )
        reply=response.message.content
        history.append({"role":"assistant","content":reply})
        print(f"MOKU🤖:{reply}")
        print()
    except Exception as e:
        print("unknown issue.is ollama running")


    # history[0]["content"]=new personality

print("nice to talk to you i have a grate time with you GOODBYE!👋🙋‍♂️")
