import ollama

response = ollama.chat(
    model='llama3.2',
    message=[
        {
            'role': 'user',
            'content': 'Explain Python in simple words'
        }
    ]
)

print(response['message']['content'])