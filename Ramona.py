from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'Ramona'
    )

trainer = ChatterBotCorpusTrainer(chatbot)
  
#trainer.train(
#    'chatterbot.corpus.spanish'
#    )

while True: 
    usuario = input(">>>Usuario: ")
    respuesta = chatbot.get_response(usuario)
    print(">>>Ramona: "+str(respuesta))
