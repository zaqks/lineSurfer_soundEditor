import pygame as pg

DELAY = 3.5
TRACK = "tracks/track.mp3"
BPM = 97


def kill():
    pg.mixer.stop()
    pg.quit()
    exit()


pg.init()
pg.display.set_mode(size=(800, 600)).fill((0, 0, 0))
pg.display.flip()

pg.mixer.init()
pg.mixer.music.load(TRACK)
pg.mixer.music.play(loops=1, start=DELAY)


TICKS = 100  # per sec
bpm = 0
avr = 0

while pg.mixer.music.get_busy():
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
            if event.key == pg.K_SPACE:
                # bmp = time between 2 beats is seconds
                avr += 60/bpm
                avr /= 2
                print(
                    f"BPM: {int(60/bpm)} AVR: {int(avr)} SYNC: {int(100*(1- min(bpm, avr)/max(bpm, avr) ))}%")
                bpm = 0

    bpm += 1/TICKS
    #
    pg.time.Clock().tick(100)  # tick/s


kill()
