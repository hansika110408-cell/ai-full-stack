from ollama import chat
good="tell me cat breeds that are suitable for the duplex house.give any 5 cat breeds."
bad="give me cat breeds"
response=chat(
    model="llama3.2",
    messages=[
        {
        "role":"user",
        "content":good
        },
        {
            "role":"user",
            "content":bad
        }
    ]
)
print(response.message.content)

