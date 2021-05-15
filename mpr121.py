#!/usr/bin/env python3

import Adafruit_MPR121.MPR121 as MPR121
import enum
import pygame
import time
import sys
import os
os.chdir('/home/pi/RPi_SoundTouch')

cap = MPR121.MPR121()

if not cap.begin():
    print('Error initializing MPR121. Check your wiring!')
    sys.exit(1)

pygame.mixer.pre_init(48000, -16, 2, 4096)
pygame.init()

class TouchMode(enum.Enum):
    TOUCH = 0
    HOLD = 1
    TOGGLE = 2

TOUCH_PLATE_MODE = {
    0: TouchMode.TOGGLE,
    1: TouchMode.HOLD,
    2: TouchMode.HOLD,
    3: TouchMode.HOLD,
    4: TouchMode.HOLD,
    5: TouchMode.HOLD,
    6: TouchMode.HOLD,
    7: TouchMode.HOLD,
    8: TouchMode.HOLD,
    9: TouchMode.HOLD,
    10: TouchMode.HOLD,
    11: TouchMode.HOLD
}

SOUND_MAPPING = {
    0: './sounds/master_of_leaufage.wav',
    1: './sounds/long_lines.wav',
    2: './sounds/sharp_ends.wav',
    3: './sounds/spiky_almonds.wav',
    4: './sounds/alien_faces.wav',
    5: './sounds/american_footballs.wav',
    6: './sounds/monster_hearts.wav',
    7: './sounds/natural_satellites.wav',
    8: './sounds/the_untouchables.wav',
    9: './sounds/slim_figures.wav'
}

sounds = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
touch_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
last_touch_time = 10 * [time.time()]

for key, soundfile in SOUND_MAPPING.items():
    sounds[key] = pygame.mixer.Sound(soundfile)
    sounds[key].set_volume(1)
    print('Loaded ' + soundfile)

print('Loaded successfully!')
print('Press Ctrl-C to quit.')

# For RPi
last_touched = cap.touched()
while True:
    current_touched = cap.touched()
    for i in range(10):
        pin_bit = 1 << i
        if TOUCH_PLATE_MODE[i] == TouchMode.TOUCH:
            if current_touched & pin_bit and not last_touched & pin_bit:
                print('{0} touched!'.format(i))
                if (sounds[i]):
                    sounds[i].play()
            if not current_touched & pin_bit and last_touched & pin_bit:
                print('{0} released!'.format(i))
        elif TOUCH_PLATE_MODE[i] == TouchMode.HOLD:
            if current_touched & pin_bit and not last_touched & pin_bit:
                print('{0} touched!'.format(i))
                if (sounds[i]):
                    sounds[i].play()
            if not current_touched & pin_bit and last_touched & pin_bit:
                print('{0} released!'.format(i))
                if (sounds[i]):
                    sounds[i].stop()
        elif TOUCH_PLATE_MODE[i] == TouchMode.TOGGLE:
            if current_touched & pin_bit and not last_touched & pin_bit:
                print(" ", (time.time() - last_touch_time[i]))
                if time.time() - last_touch_time[i] < 1.0:
                    continue
                if (sounds[i]):
                    if not (touch_counter[i] % 2):
                        sounds[i].play()
                        print(' {0} PLAY!'.format(i))
                    else:
                        sounds[i].stop()
                        print(' {0} STOP!'.format(i))
                touch_counter[i] = touch_counter[i] + 1
                print('{0} clicked!'.format(i))
            if not current_touched & pin_bit and last_touched & pin_bit:
                last_touch_time[i] = time.time()
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
