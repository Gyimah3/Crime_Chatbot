from flask import Flask, render_template, request
# jinja2 import escape
#from chatbot import chatbot
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

  # Config & Setup
## Variables of environment
DIRPATH = os.path.dirname(__file__)
ASSETSDIRPATH = os.path.join(DIRPATH, "training_data")
crime = os.path.join(ASSETSDIRPATH, "chatbot\training_data\crime1.txt")# Config & Setup
more =  os.path.join(ASSETSDIRPATH, "chatbot\training_data\more1.txt")
simple =  os.path.join(ASSETSDIRPATH, "chatbot\training_data\simple1.txt")

# Creating ChatBot Instance

chatbot = ChatBot(
'Mercy',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        {
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'I am sorry, but I do not understand. I am still learning.',
        'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'

)
  
 
#reading files
with open('crime1.txt','r') as file:
    training_data_que= file.read().splitlines()

with open('more1.txt','r') as file:
    training_data_con = file.read().splitlines()

with open('simple1.txt','r') as file:
    training_data_personal= file.read().splitlines()

#combining files
training_data = training_data_que+ training_data_personal + training_data_con

trainer = ListTrainer(chatbot)
trainer.train(training_data) 

# Training with English Corpus Data 
#trainer_corpus = ChatterBotCorpusTrainer(bot)

#Flask
app = Flask(__name__)
app.static_folder = 'static'

    
@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
	app.run()
