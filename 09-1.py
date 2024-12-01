from gpiozero import Buzzer
from gpiozero import LED
from time import sleep
from signal import pause

makerobo_Buzzer = 17

def makerobo_setup():
    global bz
    bz = Buzzer(pin=makerobo_Buzzer,active_high = False)
    bz.off()

def makerobo_buzzer_on():
    bz.on()

def makerobo_buzzer_off():
    bz.off()

def makerobo_beep(x):
    makerobo_buzzer_on()
    sleep(x)
    makerobo_buzzer_off()
    sleep(x)

def makerobo_loop():
    while True:
        makerobo_beep(1)

def destroy():
    bz.close()

if __name__ == '__main__':
    makerobo_setup()
    try:
        makerobo_loop()
    except KeyboardInterrupt:
        destroy()