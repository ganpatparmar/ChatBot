from chatterbot import ChatBot
import logging
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
import pyttsx3
import pywhatkit
engine = pyttsx3.init()
listener = sr.Recognizer()


logging.basicConfig(level=logging.INFO)
bot = ChatBot('walle',
    storage_adapters = 'chatterbot.storage.SQLStorageAdapter',
    logic_adapters = [
                      'chatterbot.logic.MathematicalEvaluation',
                        'chatterbot.logic.TimeLogicAdapter',
                        'chatterbot.logic.BestMatch',
                       'chatterbot.logic.UnitConversion',
                       #'chatterbot_weather.WeatherLogicAdapter'
                        
        
    
                        ],
    preprocessors=[ 
        'chatterbot.preprocessors.clean_whitespace'
    ]
            
)
trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english"
)

print("Speak here something to begine.....")
def speak(command):
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

while True:
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

