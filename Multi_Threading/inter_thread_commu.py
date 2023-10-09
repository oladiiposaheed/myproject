import time
from threading import *

def trafficpolice():
    while True:
        time.sleep(10) # ON for red signal
        print('Traffic Police Giving GREEN Signal')   #2
        e.set()
        time.sleep(20)  # ON for green signal
        print('Traffic Police Giving RED Signal')   #5
        e.clear()

def vehicle():
    num = 0
    while True:
        print('Vehicles are in Waiting for GREEN Signal')  # 1
        e.wait()
        print('Traffic Signal is GREEN, Vehicles can move')   #3
        while e.isSet():
            num += 1
            print('Vehicle Number: {}, Crossing the Signal.'.format(num))  #4
            time.sleep(2)
        print('Traffic Signal is RED... Vehicles has to wait.')

e = Event()
t1 = Thread(target=trafficpolice)
t2 = Thread(target=vehicle)
t1.start()
t2.start()