#Convert text to speech 
#Modules needed for text to speech:
#There are several APIs available to convert text to speech in Python. One of such APIs is the Google Text to Speech API commonly known as the gTTS API. gTTS is a very easy to use tool which converts the text entered, into audio which can be saved as a mp3 file.The gTTS API supports several languages including English, Hindi, Tamil, French, German and many more."""
#To install the gTTS API, open terminal and write 
#pip install gTTs

from gtts import gTTS 
import os # This module is imported so that we can play the converted audio 
file = open("text for text to speech.txt","r").read()

speech = gTTS(text=file, lang='en', slow=False)
# Passing the text and language to the engine,here we have marked slow=False. Which tells the module that the converted audio should have a high speed 
speech.save("text_to_speech.mp3")
os.system("text_to_speech.mp3")
