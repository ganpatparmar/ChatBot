from chatterbot import ChatBot
import logging
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
import pyttsx3
import pywhatkit
engine = pyttsx3.init()
listener = sr.Recognizer()


#logging.basicConfig(level=logging.INFO)


bot = ChatBot('ashu',
    storage_adapters = 'chatterbot.storage.SQLStorageAdapter',
    logic_adapters = [
                      'chatterbot.logic.MathematicalEvaluation',
                       # 'chatterbot.logic.TimeLogicAdapter',
                        'chatterbot.logic.BestMatch',
                       'chatterbot.logic.UnitConversion',
                       #'chatterbot_weather.WeatherLogicAdapter'
                        
        
    
                        ],
    
            
)
trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")

def speak(command):
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
print("Speak here something to begine.....")

while True:
    try:
        with sr.Microphone() as source2:
            print("Speack 'HEllO ASHU to start your' ")
            listener.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = listener.listen(source2)
            user = listener.recognize_google(audio2)
            user = user.lower()
            #print(user.split())
            if(user == 'hello ashu'):
                #print('GOOD')
                speak('Hi buddy how can i help you')
                while True:
                    try:
                        with sr.Microphone() as source1:
                            print("You>> ")
                            listener.adjust_for_ambient_noise(source1, duration=0.2)
                            audio1 = listener.listen(source1)
                            user1 = listener.recognize_google(audio1)
                            user1 = user.lower()

                            bot_responce = bot.get_response(user1)

                

                            print('bot: ')
                            speak(bot_responce)
                    
                    except sr.RequestError as e:
                        print("Could not request results; {0}".format(e))
          
                    except sr.UnknownValueError:
                        print("unknown error occured")

                    except:
                        break

                    
                
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")

    except(SystemError,EOFError,KeyboardInterrupt):
        break

