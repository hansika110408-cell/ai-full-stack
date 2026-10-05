from ollama import chat

response=chat(
    model="llama3.2"
    messege=[
        {
        "role"="user",
        "content":"what is SQL?"
        }
    ]
)
print(response)