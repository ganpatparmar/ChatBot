''' 
Author: Ganpat Parmar
E-mail: ganpat5489@gmail.com
Last Edit: 29-12-2021
License: Copyright (C) Ganpat Parmar.
General Public License (AGPL-3.0)
'''

"""
This is a ChatBot named ASHU
with following features.
1. Conversing with it's user.
2. Doing some minor calculations.
3. Opening CAMERA MOUSE for it's user.
4. Searching things for user on GOOGLE.
5. Playing videos for user on YOUTUBE.
"""

from chatterbot import ChatBot # Importing ChatBot Library
from chatterbot.trainers import ChatterBotCorpusTrainer # Importing ChatBot Trainer Library to train our ChatBot
import speech_recognition as sr # Importing speech_recongnition  Library for speech to text conversion
import pyttsx3 # Importing pythtsx3  Library for conversation
import pywhatkit # Importing pywhatkit Library for automatic web and Youtube task
import os # # Importing OS Library for os related operations
import subprocess

''' creating an object for pyttsx3 and intialising it'''
engine = pyttsx3.init() 
''' creating an object for speech_recongnition and intialising it'''
listener = sr.Recognizer()


''' creating an object for ChatBot and intialising it'''
bot = ChatBot('ashu',
    storage_adapters = 'chatterbot.storage.SQLStorageAdapter', # this adapter is SQL adapter for storing our conversations
    logic_adapters = [
                      'chatterbot.logic.MathematicalEvaluation', # this adapter is Mathematical adapter for samll calculations
                      'chatterbot.logic.BestMatch', # this adapter is for finding best match for our conversations
                      'chatterbot.logic.UnitConversion'] # this adapeter is  for Unit conversations
                      )

""" Training Our Bot  """
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

""" Function that will speack any thing that you give as a command """
def speak(command):
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

    
""" Function for searching things for us """
def search(command):
    print('Bot>> Seacrhing....',command.join(command.split()[1:]))
    speak('Searching ')
    speak(command.split()[1:])
    pywhatkit.search(command)


""" Funtion for Playing things from YOUTUBE  """
def play(command):
    print('Bot>> Playing....',command.join(command.split()[1:]))
    speak('Playing ')
    speak(command.split()[1:])
    pywhatkit.playonyt(command)


""" Function for opening CAMERA MOUSE """
def open(command):
    path = "C:\Program Files (x86)\Camera Mouse\Camera Mouse 2018\Camera Mouse 2018.exe"
    print('Bot>> opening....',command.join(command.split()[1:]))
    speak('opening camera mouse')
    os.startfile(path)
    os.system(path)
    subprocess.Popen([path])
    subprocess.call(path)


""" Fiunction for getting responce from bot """
def bot_responce(command):
    responce = bot.get_response(command)
    print('Bot>> ',responce)
    speak(responce)

""" Function for listing stuff from user """
def listen():
    while True:
        try:
            with sr.Microphone() as source:
               # print("Speack 'HEllO ASHU to start your' ")
                #user = input("You>>")
                listener.adjust_for_ambient_noise(source, duration=0.2)
                audio = listener.listen(source)
                user = listener.recognize_google(audio)
                user = user.lower()
                return user

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
          
        except sr.UnknownValueError:
            print("unknown error occured")

        except(SystemError,EOFError,KeyboardInterrupt):
            break


""" MAIN DRIVING CODE  """
while True:
    print("Say hellow ASHU to start your conversation :)")
    user = listen()
    if(user == 'hello ashu'):
        speak('Hi buddy how can I help you')
        while True:
            print("speak:)")
            user1 = listen()
            print("You>> ",user1)
            if(user1.split(' ')[0] == 'play'):
                play(user1)
            elif(user1.split(' ')[0] == 'search'):
                search(user1)
            elif(user1.split(' ')[0] == 'open'):
                open(user1)                          
            else:
                bot_responce(user1)
                
    else:
        continue
            

    
