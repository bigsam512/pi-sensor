from gpiozero import RGBLED
from colorzero import Color
from time import sleep

colors = ['red','magenta', 'green', 'yellow','blue', 'cyan']

led = RGBLED(17, 18, 27)

def makerobo_loop():
    while True:
        for col in colors:
            led.color = Color(col)
            sleep(2)

def makerobo_destroy():
    led.close()

if __name__ == "__main__":
    print(colors)
    try:
        makerobo_loop()
    except KeyboardInterrupt:
        makerobo_destroy()
