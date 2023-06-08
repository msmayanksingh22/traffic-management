from num import num
from char import char
import time
from femaleai import female_voice as fai
import random
import winsound
from ip import ip_loc

def main_female():
    welcome="Welcome to this AI Traffic Management system"
    print(welcome)
    fai(welcome)
    greet="How are you?"
    print(greet)
    fai(greet)
    g_input=char()
    g_input=g_input.lower()
    if (g_input=='i am good'or'i am great'or'i am fine'or'good'or'fine'or'great'):
        reply=["That's great","good to hear"]
        reply_r=random.choice(reply)
        print(reply_r)
        fai(reply_r)
    else:
        print("Continuing with the program")
        fai("Continuing with the program")
        
    gps="Finding your GPS location"
    print(gps)
    fai(gps)
    time.sleep(1)
    print("Locating")
    fai('locating')
    time.sleep(1)
    print(".......")
    time.sleep(1)
    loc="Location found"
    print(loc)
    fai(loc)

    ip_location=ip_loc()
    print('\n',ip_location,'\n')
    fai('Your current location is in')
    fai(ip_location)
    
    zone="Your current area is divided into 4 main zones."
    print(zone)
    fai(zone)
    zone_parts=['zone 1','zone 2','zone 3','zone 4']
    print(zone_parts)
    fai(zone_parts)
    zone_now=random.choice(zone_parts)
    print(zone_now)
    fai('You are currently in')
    fai(zone_now)
    
    speed_q="Can you please update me with your speed?"
    print(speed_q)
    fai(speed_q)
    speed_user=num()
    
    speed=[35,40,45,50]
    speed_r=random.choice(speed)
    print("Safe speed limit for this zone is ",speed_r)
    fai("Safe speed limit for this zone is ")
    fai(speed_r)
    
    if (speed_user<=speed_r):
        print("You are going good.")
        fai("You are going good.")
    else:
        winsound.Beep(440,1000)
        speed_max="Please reduce your speed for your and others safety."
        print(speed_max)
        fai(speed_max)

    op=["This zone has clumsy roads beaware of the sharp turns and voilent drivers.",
          "Accident rate in this zone is graded as 5 from a total of 10."]
    op_r=random.choice(op)
    print(op_r)
    fai(op_r)
    print("Have a safe drive!")
    fai("Its all from my side. Have a safe drive!")

