from num import num
from char import char
import time
from maleai import speak
import random
import winsound
from ip import ip_loc

def main_male():
    
    welcome="Welcome to this AI Traffic Management system"
    print(welcome)
    speak(welcome)
    
    greet="How are you?"
    print(greet)
    speak(greet)
    
    g_input=char()
    g_input=g_input.lower()
    if (g_input=='i am good'or'i am great'or'i am fine'or'good'or'fine'or'great'):
        reply=["That's great","Good to Hear"]
        reply_r=random.choice(reply)
        print(reply_r)
        speak(reply_r)
    else:
        print("Continuing with the program")
        speak("Continuing with the program")

    gps="Accessing your GPS location..."
    print(gps)
    speak(gps)
    
    time.sleep(1)

    print("Locating")
    speak('locating')
    time.sleep(1)
    print(".......")
    time.sleep(1)
    loc="Location found"
    print(loc)
    speak(loc)

    ip_location=ip_loc()
    print('\n',ip_location,'\n')
    speak('Your current location is in')
    speak(ip_location)
    
    zone="Your current area is divided into 4 main zones."
    print(zone)
    speak(zone)
    zone_parts=['zone 1','zone 2','zone 3','zone 4']
    print(zone_parts)
    speak(zone_parts)
    
    zone_now=random.choice(zone_parts)
    print(zone_now)
    speak('You are currently in')
    speak(zone_now)
    
    speed_q="Can you please update me with your speed?"
    print(speed_q)
    speak(speed_q)
    speed_user=num()
    
    speed=[35,40,45,50,55,60]
    speed_r=random.choice(speed)
    print("Safe speed limit for this zone is ",speed_r)
    speak("Safe speed limit for this zone is ")
    speak(speed_r)
    
    if (speed_user<=speed_r):
        print("You are going good.")
        speak("You are going good.")
    else:
        winsound.Beep(440,1000)
        speed_max="Please reduce your speed for your and others safety."
        print(speed_max)
        speak(speed_max)

    op=["This zone has clumsy roads beaware of the sharp turns and voilent drivers.",
          "Accident rate in this zone is graded as 5 from a total of 10."]
    op_r=random.choice(op)
    print(op_r)
    speak(op_r)
    print("Have a safe drive!")
    speak("Its all from my side. Have a safe drive!")

