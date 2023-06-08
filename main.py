from num import num
from char import char
import time
from maleai import speak
from femaleai import female_voice as fai
import random
from female import main_female
from male import main_male

def main():
    voice="Hello, Are you comfortable with my voice."
    print(voice)
    speak(voice)
    v_input=char()
    print(v_input)
    v_input=v_input.lower()
    if (v_input=='yes'):
        speak('Nice')
        main_male()
    elif(v_input=='no'):
        print("ohh, Ok, Changing audio tone")
        speak("ohh, Ok, Changing audio tone")
        main_female()
    else:
        error="Sorry, Invalid input, Please try again."
        print(error)
        speak(error)
        main()

    run="Do you want to re-run the program?"
    print(run)
    speak(run)
    user_responce=char()
    user_responce=user_responce.lower()
    print(user_responce)
    if(user_responce=='yes'):
        main()
    speak("Thank you")

main()


