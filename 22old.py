import time
import pylirc as lirc
from gpiozero import RGBLED

rgb_Lv = [100, 10, 0]
rgb_color = [00, 00, 00]

led = RGBLED(18, 19, 20)
makerobo_blocking = 0

def makerobo_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def makerobo_ledColorSet(color):
    r_val = 100 - color[0]
    g_val = 100 - color[1]
    b_val = 100 - color[2]
    r_val = makerobo_map(r_val, 0, 100, 0, 1)
    g_val = makerobo_map(g_val, 0, 100, 0, 1)
    b_val = makerobo_map(b_val, 0, 100, 0, 1)
    led.color = (r_val, g_val, b_val)


def makerobo_setup():
    lirc.init("pylirc", "/etc/lire/conf", makerobo_blocking)


def RGB_control(config):
    global color
    if config == "KEY_CHANNELDOWN":
        rgb_color[0] = rgb_Lv[0]
        print("makerobo Red OFF")

    if config == "KEY_CHANEL":
        rgb_color[0] = rgb_Lv[1]
        print("makerobo Light Red")

    if config == "KEY_CHANNELUP":
        rgb_color[0] = rgb_Lv[2]
        print("makerobo Red")

    if config == "KEY_PREVIOUS":
        rgb_color[1] = rgb_Lv[0]
        print("makerobo Green OFF")

    if config == "KEY_NEXT":
        rgb_color[1] = rgb_Lv[1]
        print("makerobo Light Green")

    if config == "KEY_PLAYPAUSE":
        rgb_color[1] = rgb_Lv[2]
        print("makerobo Green")

    if config == "KEY_VOLUMEDOWN":
        rgb_color[2] = rgb_Lv[0]
        print("makerobo Blue OFF")

    if config == "KEY_VOLUMEUP":
        rgb_color[2] = rgb_Lv[2]
        print("makerobo Light Blue")

    if config == "KEY_EQUAL":
        rgb_color[2] = rgb_Lv[2]
        print("makerobo Blue")


def makerobo_loop():
    while True:
        s = lirc.nextcode(1)
        while s:
            for code in s:
                print("Command:", code["config"])
                RGB_control(cod["config"])
                makerobo_ledColorSedt(rgb_color)
            if not makerobo_blocking:
                s = lirc.nextcode(1)
            else:
                s = []


def destroy():
    led.close()
    lirc.exit()


if __name__ == "__main__":
    try:
        makerobo_setup()
        makerobo_loop()
    except KeyboardInterrupt:
        destroy()
