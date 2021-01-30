import speech_recognition as sr

def speaker():
	recognizer = sr.Recognizer()	

	with sr.Microphone() as source_for_speech:
		recognizer.adjust_for_ambient_noise(source_for_speech)

		print("I'm trying to hear you: ")
		audio = recognizer.listen(source_for_speech)
		try:
			phrase = recognizer.recognize_google(audio, language='en')
            #wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level  
			return phrase
		except sr.UnkownValueError:
			return "I didn't understand what you said"

if __name__ == '__main__':
	text =speaker()
    with open('output_text.txt','w') as file:
		file.write(text) 
    print('Speech is saved at your location') 
