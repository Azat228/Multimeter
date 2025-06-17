def on_received_number(receivedNumber):
    global Ohms
    Ohms = receivedNumber
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global meisure, converter, value, Valueround, index
    OLED12864_I2C.clear()
    meisure = pins.analog_read_pin(AnalogReadWritePin.P0)
    converter = 3.3 * (meisure / 1023)
    value = converter + converter * difference
    Valueround = Math.round(value * 10) / 10
    OLED12864_I2C.show_number(0, 0, Valueround, 1)
    OLED12864_I2C.show_string(3, 0, "V", 1)
    basic.pause(500)
    while index <= Math.round(Valueround) - 1:
        music.play(music.create_sound_expression(WaveShape.SQUARE,
                3540,
                1,
                255,
                90,
                100,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.LOGARITHMIC),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(500)
        index += 1
    basic.pause(5000)
    OLED12864_I2C.clear()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global roundedOhms, index2
    OLED12864_I2C.clear()
    roundedOhms = Math.round(Ohms * 1000)
    OLED12864_I2C.show_number(0, 2, roundedOhms, 1)
    OLED12864_I2C.show_string(5, 2, "Ohms", 1)
    basic.pause(500)
    while index2 <= Math.round(roundedOhms) / 1000 - 1:
        music.play(music.create_sound_expression(WaveShape.SQUARE,
                3540,
                1,
                255,
                90,
                100,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.LOGARITHMIC),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(500)
        index2 += 1
    basic.pause(5000)
    OLED12864_I2C.clear()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global I, SetRealI, roundI, index3
    OLED12864_I2C.clear()
    I = pins.analog_read_pin(AnalogReadWritePin.P1)
    SetRealI = I / 1023 * 3.3 * 10
    roundI = Math.round(SetRealI * 100) / 100
    OLED12864_I2C.show_number(0, 1, roundI, 1)
    OLED12864_I2C.show_string(3, 1, "miliA", 1)
    basic.pause(500)
    while index3 <= Math.round(roundI) - 1:
        music.play(music.create_sound_expression(WaveShape.SQUARE,
                3540,
                1,
                255,
                90,
                100,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.LOGARITHMIC),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(500)
        index3 += 1
    basic.pause(5000)
    OLED12864_I2C.clear()
input.on_button_pressed(Button.B, on_button_pressed_b)

index3 = 0
roundI = 0
SetRealI = 0
I = 0
index2 = 0
roundedOhms = 0
index = 0
Valueround = 0
value = 0
converter = 0
meisure = 0
Ohms = 0
difference = 0
difference = 3.9
radio.set_group(1991)
OLED12864_I2C.init(60)
basic.show_icon(IconNames.HEART)