from ollama import chat

print("This local AI chatbot developed by Mrshameem")

while True:
    userinput = input("You: ")
    print("Thinking...")

    if userinput.lower() == "exit":
        print("Goodbye user")
        break

    response = chat(
        model='llama3',
        messages=[
            {'role': 'system', 'content': 'You are an ecommerce payment analyst.'},
            {'role': 'user', 'content': userinput}
        ]
    )

    print("AI_Bot:", response['message']['content'])
    print("-" * 50)
