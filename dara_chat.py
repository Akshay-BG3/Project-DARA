print("Hello i am DARA, Your Data assistant.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit","quit","stop"]:
        print("DARA: Goodbye!")
        break
    else:
        print("DARA: I am still learning. You said:", user_input)