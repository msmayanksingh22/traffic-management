import pyttsx3

def female_voice(text1):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text1)
    engine.runAndWait()
