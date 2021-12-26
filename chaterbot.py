from chatterbot import ChatBot # importing chatterbot
import logging
from chatterbot.trainers import ChatterBotCorpusTrainer #impoting corpus trainer
import speech_recognition as sr # for speech recognition 
import pyttsx3
import pywhatkit
engine = pyttsx3.init()
listener = sr.Recognizer()


logging.basicConfig(level=logging.INFO)
bot = ChatBot('walle', # creating instance by giving it a name
    storage_adapters = 'chatterbot.storage.SQLStorageAdapter',#defining storage adapter
    logic_adapters = [
                      'chatterbot.logic.MathematicalEvaluation',# logic adapter for mathematical evaluation
                        'chatterbot.logic.TimeLogicAdapter', # logic adapter for current time
                        'chatterbot.logic.BestMatch', # logic adapter for selecting most appropriate response
                       'chatterbot.logic.UnitConversion', # logic adapter for unit conversion
                       #'chatterbot_weather.WeatherLogicAdapter'
                        
        
    
                        ],
    preprocessors=[ 
        'chatterbot.preprocessors.clean_whitespace'
    ]
            
)
trainer = ChatterBotCorpusTrainer(bot) #trainig the instance

trainer.train(
    "chatterbot.corpus.english"
)

print("Speak here something to begine.....")
def speak(command): #method that will speak what input it recives
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

while True: # main code to generate responce by taking inputs. 
    try:
        with sr.Microphone() as source2:
            print("You>> ")
            listener.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = listener.listen(source2)
            user = listener.recognize_google(audio2)
            user = user.lower()

            bot_responce = bot.get_response(user)

            print('bot: ')
            speak(bot_responce)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")

    except(SystemError,EOFError,KeyboardInterrupt):
        break

