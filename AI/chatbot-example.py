import random
import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "a61c38d0-bf7f-11e9-a76b-516230dc8ceaa3146498-61ba-4745-9086-0086c411b701"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def answer_question():
    question = input("> ")
    answer = classify(question)
    answer_class = answer["class_name"]
    confidence = answer["confidence"]

    if confidence < 75:
        valid_answers = [
            "I don't know, ask me something else",
            "I'm not sure what you're asking..."
        ]
        print(random.choice(valid_answers))
    elif answer_class == "Weather":
        print("The weather in Edmonton is warm is summer, around 20C, and cold in winter, around -20C.")
    elif answer_class == "Chatbot":
        print("The chatbot analyzes the input, then categorizes it and responds")

if __name__ == "__main__":
    print("What do you want to know")
    while True:
        answer_question()