#!/usr/bin/env python3
import pygame

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

# sounds[i].play()
# sounds[i].stop()
