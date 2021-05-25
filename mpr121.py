#!/usr/bin/env python3

import Adafruit_MPR121.MPR121 as MPR121
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
pygame.mixer.init()

MUSIC_FILE = './sounds/master_of_leaufage.mp3'
SOUND_MAPPING = {
    0: './sounds/long_lines.wav',
    1: './sounds/sharp_ends.wav',
    2: './sounds/spiky_almonds.wav',
    3: './sounds/alien_faces.wav',
    4: './sounds/american_footballs.wav',
    5: './sounds/monster_hearts.wav',
    6: './sounds/natural_satellites.wav',
    7: './sounds/the_untouchables.wav',
    8: './sounds/slim_figures.wav'
}

sounds = len(SOUND_MAPPING) * [None]
touching = None
last_touch_time = 10 * [time.time()]

pygame.mixer.music.load(MUSIC_FILE)
print(f'Loaded music {MUSIC_FILE}')
for key, soundfile in SOUND_MAPPING.items():
    if soundfile[-3:] == 'wav':
        sounds[key] = pygame.mixer.Sound(soundfile)
        print(f'Loaded sound {soundfile}')
    else:
        print(f'{soundfile} sound not loaded')
        continue
    sounds[key].set_volume(1)

pygame.mixer.music.stop()
is_music_playing = False


def handler_press(i):
    global is_music_playing
    if i == 0:
        if is_music_playing is True:
            pygame.mixer.music.fadeout(1000)
            is_music_playing = False
        else:
            pygame.mixer.music.play()
            is_music_playing = True
        return
    if touching is None:
        sounds[i-1].play()


def handler_release(i):
    if i == 0:
        return
    sounds[i-1].fadeout(1000)


print('STARTED!')
last_touched = cap.touched()
while True:
    current_touched = cap.touched()
    for i in range(10):
        pin_bit = 1 << i
        if current_touched & pin_bit and not last_touched & pin_bit:
            print(f'{i} pressed!')
            handler_press(i)
            touching = i
        if not current_touched & pin_bit and last_touched & pin_bit:
            print(f'{i} released!')
            last_touch_time[i] = time.time()
            handler_release(i)
            touching = None
    last_touched = current_touched
    time.sleep(0.2)


# elif TOUCH_PLATE_MODE[i] == TouchMode.TOGGLE:
#     if current_touched & pin_bit and not last_touched & pin_bit:
#         print(" ", (time.time() - last_touch_time[i]))
#         if time.time() - last_touch_time[i] < 1.0:
#             continue
#         if (sounds[i]):
#             if not (touch_counter[i] % 2):
#                 sounds[i].play()
#                 print(' {0} PLAY!'.format(i))
#             else:
#                 sounds[i].stop()
#                 print(' {0} STOP!'.format(i))
#         touch_counter[i] = touch_counter[i] + 1
#         print('{0} clicked!'.format(i))
