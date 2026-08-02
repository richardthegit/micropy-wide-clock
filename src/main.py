import time

from rb.core import busy_sleep
from rb.core.rebooter import Rebooter, print_last_reboot
from rb.core.richtext import rt
from rb.core.wifi import Wifi
from rb.dev.st7789 import new_superwide

from clock_screen import ClockScreen


print_last_reboot()

with Rebooter():
    wifi = Wifi()
    if wifi.on():
        wifi.ntp()
        wifi.off()
        wifi = None

    clock = ClockScreen(*new_superwide())
    while True:
        clock.update()
        busy_sleep(1)