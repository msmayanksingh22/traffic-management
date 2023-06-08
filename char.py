import speech_recognition as sr

global c
def char():
    r = sr.Recognizer()

    mic = sr.Microphone(device_index=0)

    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source,timeout=6)
    try:
        c=r.recognize_google(audio)
        try:
            return c
        except:
            print("Sorry, Unable to understand.")
            char()
    except:
        print("Sorry, Unable to hear.")
        char()
