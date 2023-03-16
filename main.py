def on_button_pressed_a():
    gauche.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    basic.pause(500)
    gauche.show_color(neopixel.colors(NeoPixelColors.BLACK))
    basic.pause(500)
    gauche.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    basic.pause(500)
    gauche.show_color(neopixel.colors(NeoPixelColors.BLACK))
    basic.pause(500)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    stop.show_color(neopixel.colors(NeoPixelColors.RED))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    droit.show_color(neopixel.colors(NeoPixelColors.ORANGE))
input.on_button_pressed(Button.B, on_button_pressed_b)

droit: neopixel.Strip = None
stop: neopixel.Strip = None
gauche: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
gauche = strip.range(0, 2)
stop = strip.range(0, 5)
droit = strip.range(3, 2)

def on_forever():
    pass
basic.forever(on_forever)
