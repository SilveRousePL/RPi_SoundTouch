#!/usr/bin/env python3

import Adafruit_MPR121.MPR121 as MPR121
import pygame
import time
import sys

cap = MPR121.MPR121()

if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

SOUND_MAPPING = {
    0: './Sounds/Animal/Bird.wav',
    1: './Sounds/Animal/Cricket.wav',
    2: './Sounds/Animal/Dog1.wav',
    3: './Sounds/Animal/Dog2.wav',
    4: './Sounds/Animal/Duck.wav',
    5: './Sounds/Animal/Goose.wav',
    6: './Sounds/Animal/Horse.wav',
    7: './Sounds/Animal/Kitten.wav',
    8: './Sounds/Animal/Meow.wav',
    9: './Sounds/Animal/Owl.wav',
    10: './Sounds/Animal/Rooster.wav',
    11: './Sounds/Animal/WolfHowl.wav',
}

sounds = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for key, soundfile in SOUND_MAPPING.items():
    sounds[key] = pygame.mixer.Sound(soundfile)
    sounds[key].set_volume(1)

print('Press Ctrl-C to quit.')

# For RPi
last_touched = cap.touched()
while True:
    current_touched = cap.touched()
    for i in range(12):
        pin_bit = 1 << i
        if current_touched & pin_bit and not last_touched & pin_bit:
            print('{0} touched!'.format(i))
            if (sounds[i]):
                sounds[i].play()
        if not current_touched & pin_bit and last_touched & pin_bit:
            print('{0} released!'.format(i))

    last_touched = current_touched
    time.sleep(0.1)


# For PC
# touching = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# while True:
#     i = int(input())
#     if touching[i] == 0:
#         touching[i] = 1
#         print('{0} touched!'.format(i))
#         if (sounds[i]):
#             sounds[i].play()
#     else:
#         touching[i] = 0
#         print('{0} released!'.format(i))
