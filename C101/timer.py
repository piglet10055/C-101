import time
import random

def countdown_timer(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)
    
        timer=f'{mins}:{secs}'
        print(timer)
    
        seconds-=1
    print("tempo esgotado")

seconds= input("digite o tempo em segundos: ")

countdown_timer(int(seconds))