# Crime_Chatbot

## Problem Definition
Crime has been a grim and strong undercurrent of human culture throughout history. Activities like murder, thefts and attacks happening frequently are indications of an unsafe society. These kinds of activities have been happening since a very long time.

## Project Aim and Objectives
This project aims at building a conversational bot that is capable of providing useful information
on the subject of crime and its related subjects. It provides awareness on crime.

## Scope of Work
In this mini-project, I aimed to create a simple conversational AI bot using Python and the opensource library, Chatterbot. This work uses Chatbot, a computer program designed to simulate conversation with human users in the crime detection procedures. This project aims at building conversational bot that is capable of providing useful information on the subject of crime and its related subjects. It provides awareness on crime.This work covers the methodology and installation requirements needed for the building of the conversational Chatbot. The training of the bot was based on a rule-based approach to provide easy and simple query and response. 

The first step in creating my bot was to install chatterbot and set up the basic infrastructure. I then defined a set of pre-written responses for  my bot to use in specific situations. These responses were based on common questions or statements that users might make, such as "What should I ask?" or "what is a dowry?".
Next, I trained the bot using a corpus of conversational text data that some was written by me  called "training_data" to train the bot on this dataset of verbal exchanges.

Once the bot was trained,I named it "Mercy the chatbot", I integrated it into a simple web app using Flask, a micro-framework for Python. This allowed users to interact with the bot by entering text into a chatbot interface. The bot would then process the input, generate a response based on the trained model, and display it to the user in real-time. 


### Manual Setup

For manual installation, you need to have [`Python3`](https://www.python.org/) on your system. Then you can clone this repo and being at the repo's `root :: friendly_web_interface_for_chatbot> ...`  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

    **NB:** For MacOs users, please install `Xcode` if you have an issue.



- Run the demo apps (being at the repository root):

        python main.py
        
        
 ## Screenshots

<table>
    <tr>
        <th>chat Interface</th>
        <th>chat Interface</th>
        <th>cat Interface</th>
    </tr>
    <tr>
        <td><img src="./images/screen1.png"/></td>
        <td><img src="./images/screen2.png"/></td>
        <td><img src="./images/screen3.png"/></td>
    </tr>
</table>

    
  ## Author:
[Gyimah Gideon](https://www.linkedin.com/in/gideon-gyimah-08268b243/)  
