from gpiozero import LED
from time import sleep

makerobo_LaserPin = LED(17)

def makerobo_setup():
    makerobo_LaserPin.off()

def makerobo_loop():
    while True:
        makerobo_LaserPin.on()
        sleep(0.5)
        makerobo_LaserPin.off()
        sleep(0.5)

def makerobo_destory():
    makerobo_LaserPin.close()

if __name__ == "__main__":
    makerobo_setup
    try:
        makerobo_loop()
    except KeyboardInterrupt:    
        makerobo_destory()
