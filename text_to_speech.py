# a simple text to speech code implementation 


import pyttsx3 
def text_to_speech(text):
    speech_engine = pyttsx3.init()
    speech_engine.say(text) # say the word 
    speech_engine.runAndWait() # wait to say the word incase it's delaying

# context text to speech 
text_to_speak = input('Enter a word to speak out: ').strip() 


if __name__ == '__main__':
    text_to_speech(text_to_speak) 