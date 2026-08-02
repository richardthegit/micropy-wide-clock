Clock
=====

Very basic time/date on the ultrawide 284x76 Estar Dyn display.

# Fonts

Using the display driver here: https://russhughes.github.io/st7789py_mpy

The script in the utils directory can be used to prepare the fonts used:

    python write_font_converter.py <fonts>/SpecialGothicCondensedOne-Regular.ttf 90 -s "0123456789:" > <repo>/src/fonts/condensed90.py
    python write_font_converter.py <fonts>/SpecialGothicCondensedOne-Regular.ttf 38 -c 0x20-0x7f > <repo>/src/fonts/condensed38.py
