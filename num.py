import speech_recognition as sr

global n
def num():
    r = sr.Recognizer()

    mic = sr.Microphone(device_index=0)

    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)
        #print("Please speak: ")
        audio = r.listen(source,timeout=5)
    try:
        n=r.recognize_google(audio)
        try:
            print("You have spoken: ",n)
            return int(n)
        except:
            print("Sorry, Unable to understand.")
            num()
    except:
        print("Sorry, Unable to hear.")
        num()
