import re
responses={
    'hi|hey|hello': 'Hello! How can I assist you today?',
    'what is you name?': 'I am a chatbot created to assist you.',
    'how are you?': 'I am just a program, but I am functioning as expected!',
    'bye|goodbye': 'Goodbye! Have a great day!',
}

def botresponse(userinput):
    userinput=userinput.lower()
    
    for i in responses:
        if re.search(i, userinput):
            return responses[i]

def chatbot(userinput):
    print("chatbot: hello i am here to assist you and help you in building product")
while True:
    userinput = input("You: ")
    if userinput.lower() in ['exit', 'quit']:
        print("chatbot: Goodbye! Have a great day!")    
        break 

    response=botresponse(userinput)   
    print(f"chatbot: {response}")
chatbot()





    
