""" Faça um programa em Python que abra
    e reproduza o áudio de um arquivo MP3. """

from pygame import mixer
from pygame import event

mixer.init()
mixer.music.load('ex021-again.mp3')
mixer.music.play()
input()
event.wait()
