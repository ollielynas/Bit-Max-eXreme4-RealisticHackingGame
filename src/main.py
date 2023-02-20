import msvcrt
import time
import os
import random

def hack_1():
    os.system("cls")
    start = time.time()
    print("!!SYSTEM WARNING!! we are being hacked ")
    print("!!SYSTEM WARNING!! you have 60 seconds to prevent the hack ")
    
    hack_text = ["start anti hack","init anti SSl ripper","bypassing firewall"]
    random.shuffle(hack_text)
    hack_text += ["LAUNCH CYBER NUKE"]
    letters = list(set("LAUNCH CYBER NUKE"))
    random.shuffle(letters)
    text = ""
    n=1
    nuke_time=False
    while time.time() - start <= 60:
        remaining = time.time() - start
        if msvcrt.kbhit():
            msvcrt.getch()
            if nuke_time or hack_text[0] == "AUNCH CYBER NUKE" :
                nuke_time = True
                l = random.choice(letters)
                a =random.choice([0,0,0,1])
                n+=a
                if n == len("LAUNCH CYBER NUKE")-1:
                    print("LAUNCH CYBER NUKE"+" "*30)
                    print("SYSTEM: we won!")
                    time.sleep(4)
                    return
                text = "LAUNCH CYBER NUKE"[:n] + l*[1,0][a]
            if hack_text[0] == "":
                del hack_text[0]
                print(text+' '*35)
                text = ""

            if not nuke_time:
                text += hack_text[0][:1]
                hack_text[0] = hack_text[0][1:]
        print(
            f"  TIME REMAINING : {(round(20-remaining))}:{round((((20-remaining)-round(20-remaining))*100)+50)}{'0'*int((round((((20-remaining)-round(20-remaining))*100)+50))< 10)} >{text} {' '*35}", end="\r")
        

def home():
    input("start hack")
    hack_1()
    
home()