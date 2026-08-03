import time

from rb.core import busy_sleep
from rb.core.rebooter import Rebooter, print_last_reboot
from rb.core.richtext import rt
from rb.core.wifi import Wifi
from rb.dev.st7789 import new_superwide

from clock_screen import ClockScreen


print_last_reboot()

display, bl_pwm = new_superwide()
clock = ClockScreen(display, bl_pwm)

def run():
    with Rebooter():
        wifi = Wifi()
        if wifi.on():
            wifi.ntp()
            wifi.off()
            wifi = None

        while True:
            clock.update()
            busy_sleep(1)

if __name__ == '__main__':
    run()