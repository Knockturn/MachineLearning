# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 08:38:44 2019

@author: Philippe Kjellberg Bräuner (PKB)
"""
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot_éner = ChatBot('ÉNER 2.0',
                   storage_adapter='chatterbot.storage.SQLStorageAdapter',
                   database_uri='sqlite:///database.sqlite3',
                   logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        }]
)
'''
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot_éner)

# Train based on the english corpus
trainer.train("chatterbot.corpus.english")

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")
'''
print('Éner: Type something to begin.')

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()

        bot_response = bot_éner.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break