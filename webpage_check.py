#!/bin/python3

import requests
import os
from threading import Thread 
import time 

page_to_check = "https://facebook.com"

os.system("clear")
print(f"Start program and check {page_to_check} …")
print(f"")
print(f"Press return to quit!")
print()

i = False
install = False
uhrzeit = ""
history = 0

def listen():
    global i
    input()
    i = True

listener = Thread(target=listen)
listener.start()

def status_toggle(bar):
    if bar[1] != history:
        print(f"{bar[0]} We have an {bar[1]} status.")
        return bar
    else:
        pass

def chek():
    global i
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    uhrzeit = time_string
    r = requests.get(page_to_check)
    if r.status_code == 200:
        global i
        i = True
    else:
        sc = r.status_code
        time.sleep(1)
        return uhrzeit, sc
    
while i != True:
    try:
        foo = chek()
        status_toggle(foo)
        history = foo[1]
    except:
        time.sleep(1)

listener.join()