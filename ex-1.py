from ollama import chat

response = chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": """You did a good job
                AI: You didn't just do a good job, you did an amazing job!

                You look nice today
                AI: You don't just look nice today, you look absolutely stunning!

                You are very talented
                AI: You aren't just talented, you're unbelievably talented!"""
        }
    ]
)

print(response.message.content)