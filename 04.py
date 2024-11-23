from gpiozero import LED
from time import sleep

makerobo_RelayPin = LED(17)

def makerobo_setup():
    makerobo_RelayPin.off()

def makerobo_loop():
    while True:
        makerobo_RelayPin.on()
        sleep(0.5)
        makerobo_RelayPin.off()
        sleep(0.5)

def makerobo_destroy():
    makerobo_RelayPin.close()

if __name__ == '__main__':
    makerobo_setup()
    try:
        makerobo_loop()
    except KeyboardInterrupt:
        makerobo_destroy()
