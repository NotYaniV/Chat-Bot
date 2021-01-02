import random
import json
import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize


class ChatBot():
    def __init__(self):
        self.device = torch.device(
            'cuda' if torch.cuda.is_available() else 'cpu')

        with open('intents.json', 'r') as json_data:
            self.intents = json.load(json_data)

        FILE = "data.pth"
        data = torch.load(FILE)

        input_size = data["input_size"]
        hidden_size = data["hidden_size"]
        output_size = data["output_size"]

        self.all_words = data['all_words']
        self.tags = data['tags']

        model_state = data["model_state"]

        self.model = NeuralNet(input_size, hidden_size,
                               output_size).to(self.device)
        self.model.load_state_dict(model_state)
        self.model.eval()

        ''' 
        option = input("Hey, Do you want to name your bot?(Y/N)\n")
        if (option.lower() == 'yes' or option.lower() == 'y'):
            name = input("Enter Bot name\n")

        if (option.lower() == 'no' or option.lower() == 'n'):
            name = 'Sam'
        '''

        print("Let's chat! (type 'quit' to exit)")

    def get_response(self, sentence):
        # print(sentence)
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, self.all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(self.device)

        output = self.model(X)
        _, predicted = torch.max(output, dim=1)

        tag = self.tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in self.intents['intents']:
                if tag == intent["tag"]:
                    return (f"{random.choice(intent['responses'])}")
        else:
            return (f"Sorry, can't understand you, Please give me more info")


''' 
bot = ChatBot()
a = 0
while a != 1:
    s = input("input  ")

    print(bot.get_response(s))
 '''
