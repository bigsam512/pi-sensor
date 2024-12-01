from gpiozero import Button 
from gpiozero import LED
from time import sleep
from signal import pause

makerobo_VibratePin = Button(17)
p_R = LED(18)
p_G = LED(27)

def pressed():
    print('********************************')
    print('* makerobo                   ON*')
    print('********************************')
    p_R.on()
    p_G.off()

def released():
    print('***************')
    print('* OFF Makerobo*')
    print('***************')
    p_R.off()
    p_G.on()

makerobo_VibratePin.when_pressed = pressed
makerobo_VibratePin.when_released = released

def makerobo_loop():
    pause()

def makerobo_destroy():
    p_R.close()
    p_G.close()

if __name__=='__main__':
    try:
        makerobo_loop()
    except KeyboardInterrupt:
        makerobo_destroy()