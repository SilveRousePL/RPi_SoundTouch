#!/usr/bin/env python3

from playsound import playsound
import Adafruit_MPR121.MPR121 as MPR121
import logging
import threading
import time
import sys

x1 = threading.Thread(target=thread_function, args=("frogs2.wav",))
x2 = threading.Thread(target=thread_function, args=("moor6.wav",))

def thread_function(filename):
    logging.info("Sound %s: play", filename)
    playsound(filename)
    logging.info("Sound %s: stop", filename)


def playsound(touched_pin):
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    if touched_pin is 0:
        x1.start()
    if touched_pin is 11:
        x2.start()


cap = MPR121.MPR121()

if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

print('Press Ctrl-C to quit.')
last_touched = cap.touched()
while True:
    current_touched = cap.touched()
    for i in range(12):
        pin_bit = 1 << i
        if current_touched & pin_bit and not last_touched & pin_bit:
            playsound(i)
        if not current_touched & pin_bit and last_touched & pin_bit:
            pass
    last_touched = current_touched
    time.sleep(0.1)
