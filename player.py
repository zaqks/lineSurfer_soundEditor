import pygame as pg
from pygame import mixer
from libs.Clock import Clock




MTR = False

TRACK = "tracks/TSFHA.mp3"
BEATS = "out/out.txt"
BPM = 79
MEASURES = 4


def kill():
    mixer.stop()
    pg.quit()

    exit()


pg.init()
pg.display.set_mode(size=(800, 600)).fill((0, 0, 0))
pg.display.flip()

mixer.init()
mixer.music.load(TRACK, "main")
# mixer.music.load("sounds/tick.wav", "tick")

mixer.Channel(0).play(pg.mixer.Sound(TRACK))


clk = Clock(60/(BPM*MEASURES), (60/(BPM)))

while True:
    # event capture
    for event in pg.event.get():
        if event.type == pg.QUIT:
            kill()
        #
        if event.type == pg.KEYDOWN:
            # killing stuff
            if event.key in [pg.K_q, pg.K_ESCAPE]:
                kill()

    #
    if MTR:
        mixer.Channel(1).play(pg.mixer.Sound("sounds/tick.wav"))

    #
    if clk.tick():
        print("tick")



    #
    pg.time.Clock().tick((BPM*MEASURES)/60)  # tick/s


kill()
