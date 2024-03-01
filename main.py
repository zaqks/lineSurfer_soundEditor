import pygame as pg
from pygame import mixer


MTR = False

TRACK = "tracks/track-[AudioTrimmer.com].mp3"
BPM = 97
MEASURES = 4
# units

rslt = ""


def kill():
    mixer.stop()
    pg.quit()
    # save the file before quitting

    with open("out/out.txt", "w") as f:
        f.write(rslt)
        f.close()
    print("data saved")

    exit()


pg.init()
pg.display.set_mode(size=(800, 600)).fill((0, 0, 0))
pg.display.flip()

mixer.init()
mixer.music.load(TRACK, "main")
# mixer.music.load("sounds/tick.wav", "tick")

mixer.Channel(0).play(pg.mixer.Sound(TRACK))


one = False
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
            one = event.key in [pg.K_f, pg.K_g, pg.K_h]

    if one:
        rslt += "1"
    else:
        rslt += "0"
    one = False

    #
    if MTR:
        mixer.Channel(1).play(pg.mixer.Sound("sounds/tick.wav"))

    #
    pg.time.Clock().tick(BPM*MEASURES/60)  # tick/s


kill()
