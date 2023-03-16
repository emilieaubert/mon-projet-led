input.onButtonPressed(Button.A, function () {
    gauche.showColor(neopixel.colors(NeoPixelColors.Orange))
    basic.pause(500)
    gauche.showColor(neopixel.colors(NeoPixelColors.Black))
    basic.pause(500)
    gauche.showColor(neopixel.colors(NeoPixelColors.Orange))
    basic.pause(500)
    gauche.showColor(neopixel.colors(NeoPixelColors.Black))
    basic.pause(500)
})
input.onButtonPressed(Button.AB, function () {
    stop.showColor(neopixel.colors(NeoPixelColors.Red))
})
input.onButtonPressed(Button.B, function () {
    droit.showColor(neopixel.colors(NeoPixelColors.Orange))
})
let droit: neopixel.Strip = null
let stop: neopixel.Strip = null
let gauche: neopixel.Strip = null
let strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
gauche = strip.range(0, 2)
stop = strip.range(0, 5)
droit = strip.range(3, 2)
basic.forever(function () {
	
})
