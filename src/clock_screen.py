import time

from rb.core import duty
from rb.core.constants import MONTHS_3, DAYS_3
from rb.core.richtext import rt
from rb.core.tz import get_tz, local_secs
from rb.dev.st7789 import color565

from fonts import condensed90 as font_xl
from fonts import condensed38 as font_lg

dark_blue = color565(6,79,110)
light_blue = color565(167,212,228)
brown = color565(124,66,38)
pink = color565(243,127,148)

color_schemes = (
    (dark_blue, pink, light_blue),
    (brown, light_blue, pink),
)

class ClockScreen:
    """
    Time/date display on a 284x76 screen.
    """
    def __init__(self, display, bl_pwm):
        self.display = display
        self.bl_pwm = bl_pwm
        self.last_min = -1

    def set_brightness(self, hour):
        """
        Dim the display at night.
        """
        if hour >= 22 or hour < 6:
            self.bl_pwm.duty_u16(duty(100 - 15))
        else:
            self.bl_pwm.duty_u16(duty(0))

    def update(self):
        secs = local_secs()
        year, month, day, h, m, s, weekday, yearday = time.localtime(secs)        
        tz, offset = get_tz()

        if m == self.last_min:
            return

        self.last_min = m
        self.set_brightness(h)

        d = self.display
        pad = 4
        left = pad
        top = pad
        right = d.width - pad
        bottom = d.height - pad

        bg, fg, fg2 = color_schemes[m % 2]
        d.fill(bg)

        d.aligned(font_xl, f'{h:02d}:{m:02d}', left, d.height / 2, fg, bg, valign = 'middle')
        d.aligned(font_lg, f'{DAYS_3[weekday]}', right, top, fg2, bg, halign = 'right')
        d.aligned(font_lg, f'{day} {MONTHS_3[month - 1]}', right, bottom, fg2, bg, 
                  halign = 'right', valign = 'bottom')
        