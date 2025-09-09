from gpt4all import GPT4All

# Model load karo (pehli baar run karoge to model download hoga ~4-8 GB)
model = GPT4All("gpt4all-falcon-newbpe-q4_0.gguf")

def chat_with_gpt(prompt):
    with model.chat_session():
        response = model.generate(prompt, max_tokens=200)
    return response

if __name__ == "__main__":
    print("🤖 GPT4All Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Bye! 👋")
            break
        
        response = chat_with_gpt(user_input)
        print("Bot:", response)
