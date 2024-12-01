from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
from signal import pause

makerobo_Buzzer = 17

l = [220,220,220,220,220,220,220,248]
m = [220,262,294,330,350,393,441,495]
h = [220,525,589,661,700,786,800,880]

makerobo_song_1 = [m[3],m[5],m[6],m[3],m[2],m[3],m[5],m[6],
                   h[1],m[6],m[5],m[1],m[3],m[2],m[2],m[3],
                   m[5],m[2],m[3],m[3],l[6],l[6],l[6],m[1],
                   m[2],m[3],m[2],l[7],l[6],m[1],l[5]]

makerobo_beat_1 = [1,1,3,1,1,3,1,1,
                   1,1,1,1,1,1,3,1,
                   1,3,1,1,1,1,1,1,
                   1,2,1,1,1,1,1,1,
                   1,1,3]

makerobo_song_2 = [m[1],m[1],m[1],l[5],m[3],m[3],m[3],m[1],
                   m[1],m[3],m[5],m[5],m[4],m[3],m[2],m[2],
                   m[3],m[4],m[4],m[3],m[2],m[3],m[1],m[1],
                   m[3],m[2],l[5],l[7],m[2],m[1]]

makerobo_beat_2 = [1,1,2,2,1,1,2,2,
                   1,1,2,2,1,1,3,2,
                   1,2,2,1,1,2,2,1,
                   1,2,2,1,1,3]

def makerobo_setup():
    global bz
    bz = TonalBuzzer(makerobo_Buzzer)
    bz.stop()

def makerobo_loop():
    while True:
        for i in range(1, len(makerobo_song_1)):
            bz.play(Tone(makerobo_song_1[i]))
            sleep(makerobo_beat_1[i]* 0.5)
        sleep(1)
        for i in range(1,len(makerobo_song_2)):
            bz.play(Tone(makerobo_song_2[i]))
            sleep(makerobo_beat_2[i] * 0.5)
        
def makerobo_destory():
    bz.stop()

if __name__ == '__main__':
    makerobo_setup()
    try:
        makerobo_loop()
    except KeyboardInterrupt:
        makerobo_destory()