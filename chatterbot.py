from chatterbot import ChatBot
import chatterbot_weather
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import subprocess
engine = pyttsx3.init()
listener = sr.Recognizer()
path = "C:\Program Files (x86)\Camera Mouse\Camera Mouse 2018\Camera Mouse 2018.exe"

#logging.basicConfig(level=logging.INFO)


bot = ChatBot('ashu',
    storage_adapters = 'chatterbot.storage.SQLStorageAdapter',
    logic_adapters = [
                      'chatterbot.logic.MathematicalEvaluation',
                      'chatterbot.logic.BestMatch',
                      'chatterbot.logic.UnitConversion',
                      #'chatterbot_weather.WeatherLogicAdapter'
                        
        
    
                        ]
    
            
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
            #user = input("You>>")
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
                            print("speak:)")
                           # user1 = input("You>>>")
                            listener.adjust_for_ambient_noise(source1, duration=0.2)
                            audio1 = listener.listen(source1)
                            user1 = listener.recognize_google(audio1)
                            user1 = user1.lower()
                            print("You>> ",user1)
                            #print(user1.split(' ')[0])
                            if(user1.split(' ')[0] == 'play'):
                                print('Bot>> Playing....',user1.split()[0:])
                                speak('Playing ')
                                speak(user1.split()[0:])
                                pywhatkit.playonyt(user1)
                            elif(user1.split(' ')[0] == 'search'):
                                print('Bot>> Seacrhing....',user1.split()[0:])
                                speak('Searching ')
                                speak(user1.split()[0:])
                                pywhatkit.search(user1)
                            elif(user1.split(' ')[0] == 'open'):
                                print('Bot>> opening....',user1.split()[0:])
                                speak('opening camera mouse')
                                os.startfile(path)
                                os.system(path)
                                subprocess.Popen([path])
                                subprocess.call(path)

                                

                            else:

                                bot_responce = bot.get_response(user1)

                

                                print('bot>> ',bot_responce)
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

