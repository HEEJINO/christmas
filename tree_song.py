import os
import time
import random

import numpy as np
import pygame


def clear():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:
        os.system("clear")


COLORS = [
    "\033[31m",  # 빨강
    "\033[32m",  # 초록
    "\033[33m",  # 노랑
    "\033[35m",  # 자주
    "\033[36m",  # 청록
    "\033[91m",  # 밝은 빨강
    "\033[92m",  # 밝은 초록
    "\033[93m",  # 밝은 노랑
    "\033[94m",  # 밝은 파랑
]
RESET = "\033[0m"


def random_rainbow_line(star_count: int) -> str:
    colored_count = random.randint(1, star_count)
    colored_indices = set(random.sample(range(star_count), colored_count))

    line_chars = []
    for i in range(star_count):
        if i in colored_indices:
            color = random.choice(COLORS)
            line_chars.append(color + "*" + RESET)
        else:
            line_chars.append("*")
    return "".join(line_chars)


def draw_rainbow_tree(height: int):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        star_count = 2 * i - 1
        stars = random_rainbow_line(star_count)
        print(spaces + stars)


    for _ in range(2):
        spaces = " " * (height - 1)
        trunk = "\033[32m" + "|||" + RESET
        print(spaces + trunk)


NOTE_FREQS = {
    "C4": 262,
    "D4": 294,
    "E4": 330,
    "F4": 349,
    "F#5": 743,
    "G4": 392,
    "A4": 440,
    "A#5": 936,
    "B4": 494,
    "C5": 523,
    "C#5":555,
    "D5": 587,
    "E5": 659,
    "F5": 698,
    "G5": 784,
    "A5": 880,
    "B5": 988,
    "C6": 1047,
    "D6": 1188,
}


def init_audio():
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2)
    pygame.init()

def play_tone(freq: int, dur_ms: int, volume: float = 0.3):
    sample_rate = 44100
    n_samples = int(sample_rate * dur_ms / 1000)

    t = np.linspace(0, dur_ms / 1000, n_samples, False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)

    mono = (wave * 32767).astype(np.int16)  # 16-bit PCM
    audio = np.column_stack((mono, mono))
    sound = pygame.sndarray.make_sound(audio)
    sound.set_volume(volume)
    sound.play()
    pygame.time.delay(dur_ms)
    sound.stop()


def get_melody(song: str):
    s = song.lower()


    if "jingle" in s or "징글" in s:
        melody = [
            ("E5", 300), ("E5", 300), ("E5", 600),
            ("E5", 300), ("E5", 300), ("E5", 600),
            ("E5", 300), ("G5", 300), ("C5", 400), ("D5", 150), ("E5", 900),
            ("pause", 400),
            ("F5", 300), ("F5", 300), ("F5", 500), ("F5", 150),
            ("F5", 300), ("E5", 300), ("E5", 300), ("E5", 300), 
            ("E5", 400), ("D5", 300), ("D5", 300), ("E5", 300),
            ("D5", 600), ("G5", 600),
            ("E5", 300), ("E5", 300), ("E5", 600),
            ("E5", 300), ("E5", 300), ("E5", 600),
            ("E5", 300), ("G5", 300), ("C5", 400), ("D5", 150), ("E5", 900),
            ("pause", 400),
            ("F5", 300), ("F5", 300), ("F5", 500), ("F5", 150),
            ("F5", 400), ("E5", 300), ("E5", 300), ("E5", 300),
            ("G5", 300), ("G5", 300), ("F5", 300), ("D5", 300), ("C5", 400),
        ]


    elif "last christmas" in s or "라스트" in s:
        melody = [
            ("G5", 700), ("G5", 600), ("F5", 400), ("pause", 100), ("C5", 300), ("G5", 300), ("G5", 300), ("A5", 300), ("F5", 700),
            ("pause", 400),
            ("C5", 400), ("G5", 300), ("G5", 300), ("A5", 500), ("F5", 700), 
            ("pause", 300), 
            ("C5", 300), ('pause', 100), ("E5", 300), ("F5", 300), ("E5", 300), ("D5", 600), 
            ("pause", 500),
            ("A5", 900), ("G5", 900), ("pause", 300), 
            ("D5", 300), ("pause", 100), ("A5", 300), ("A#5", 300), ("A5", 300), ("G5", 900), ("pause", 400), 
            ("F5", 300), ("E5", 400), ("F5", 400),("F5", 400),("E5", 600), ("pause", 100), ("F5", 400),("E5", 400), ("C5", 900),

        ]


    elif "all i want" in s or "all i want for christmas" in s or "all" in s:
        melody = [
            ("G5", 400), ("A5", 400), ("F#5", 400), ("G5", 300), ("E5", 400), ("F#5", 300), ("E5", 200), ("D5", 400), ("pause", 300), 
            ("G5", 400), ("A5", 400), ("F#5", 400), ("G5", 300), ("E5", 400), ("F#5", 300), ("E5", 200), ("D5", 400), ("pause", 500), 
            ("C5", 400), ("D5", 400), ("F5", 400), ("C6", 400), ("A#5", 700),("pause", 900),
            ("A5", 500), ("G5", 500), ("F5", 500),("D5", 500),("C#5", 400), ("G5", 700), ("A5", 600), ("G5", 200),("G5", 600), ("F5", 700)
        ]


    elif "christmas tree" in s or "tree" in s or "트리" in s:
        melody = [
            ("C5", 500), ("F5", 400),  ("F5", 200),  ("F5", 400),  ("G5", 400),  ("A5", 150),  ("A5", 200),  ("A5", 400),  ("pause", 200),
            ("A5", 200),  ("G5", 300),  ("A5", 300),  ("A#5", 400), ("E5", 400), ("G5", 400),  ("F5", 400), ("pause", 300),
            ("C5", 500), ("F5", 400),  ("F5", 200),  ("F5", 400),  ("G5", 400),  ("A5", 150),  ("A5", 200),  ("A5", 400),  ("pause", 300),
            ("A5", 20),  ("G5", 300),  ("A5", 300),  ("A#5", 400), ("E5", 400), ("G5", 400),  ("F5", 500), ("pause", 300),

            ("C6", 400),  ("C6", 300),  ("A5", 300),  ("D6", 500),  ("C6", 300),  ("C6", 300),  ("A#5", 300),  ("A#5", 600), ("pause", 300),
            ("A#5", 400),  ("A#5", 300),  ("G5", 300),  ("C6", 500), ("A#5", 300),  ("A#5", 300),  ("A5", 300),  ("A5", 600), ("pause", 300),

            ("C5", 500), ("F5", 400),  ("F5", 200),  ("F5", 400),  ("G5", 400),  ("A5", 150),  ("A5", 200),  ("A5", 400),  ("pause", 300),
            ("A5", 200),  ("G5", 300),  ("A5", 300),  ("A#5", 400), ("E5", 400), ("G5", 400),  ("F5", 700),
        ]


    elif "we wish" in s or "we" in s or "위" in s:
        melody = [
            ("C5", 500), ("F5", 500), ("F5", 300), ("G5", 300), ("F5", 300), ("E5", 300), ("D5", 500), ("D5", 500), ("pause", 200),
            ("D5", 500), ("G5", 500), ("G5", 300), ("A5", 300), ("G5", 300), ("F5", 300), ("E5", 500), ("C5", 500), ("pause", 200),
            ("C5", 500), ("A5", 500), ("A5", 300), ("A#5", 300), ("A5", 300), ("G5", 300), ("F5", 500), ("D5", 500), ("C5", 200), ("C5", 200),
            ("D5", 500), ("G5", 500), ("E5", 500), ("F5", 500),
        ]

    elif "noel" in s or "노엘" in s or "노앨" in s:
        melody = [
            ("E5", 400), ("D5", 400), ("C5", 900), ("D5", 300), ("E5", 300), ("F5", 400), ("G5", 900),
            ("pause", 500),
            ("A5", 400), ("B5", 500), ("C6", 700), ("B5", 700), ("A5", 700), ("G5", 700),
            ("pause", 600),
            ("A5", 400), ("B5", 500), ("C6", 700), ("B5", 700), ("A5", 700), ("G5", 700), 
            ("A5", 700), ("B5", 700), ("C6", 700), ("G5", 700), ("F5", 700), ("E5", 1000),
        ]


    else:
        melody = [
            ("C6", 500), ("A#5", 200), ("A5", 500), ("G5", 500), ("F5", 400), ("G5", 400), ("A5", 400), ("F5", 400),
            ("G5", 200), ("A5", 200), ("A#5", 200), ("G5", 200), ("A5", 500), ("G5", 300), ("F5", 500), ("E5", 500), ("F5", 700),
            ("pause", 300),
            ("C6", 500), ("A#5", 300), ("A5", 500), ("G5", 500), ("F5", 400), ("G5", 400), ("A5", 400), ("F5", 400), 
            ("D6", 200),("D6", 200),("D6", 200),("D6", 200), ("C6", 600), ("A#5", 300), ("A5", 500), ("G5", 500), ("F5", 700), 
        ]

    return melody

def main():
    print("Song list: \n-🎄 Noel\n-🎄 Last Christmas\n-🎄 We wish you a Merry Christmas\n-🎄 Oh Christmas Tree\n-🎄 All I Want a lot for christmas\n-🎄 Jingle bells")
    song = input("~~Put the christmas carol: ")

    height = 8
    melody = get_melody(song)

    init_audio()

    for note, dur_ms in melody:
        clear()
        draw_rainbow_tree(height)

        if note == "pause":
            time.sleep(dur_ms / 1000.0)
        else:
            freq = NOTE_FREQS.get(note, 600)
            play_tone(freq, dur_ms)

    print("\n\n\n Merry Christmas! 🎄✨")
    pygame.quit()

if __name__ == "__main__":
    main()
