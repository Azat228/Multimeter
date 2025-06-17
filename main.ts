radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    Ohms = receivedNumber
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    OLED12864_I2C.clear()
    meisure = pins.analogReadPin(AnalogReadWritePin.P0)
    converter = 3.3 * (meisure / 1023)
    value = converter + converter * difference
    Valueround = Math.round(value * 10) / 10
    OLED12864_I2C.showNumber(0, 0, Valueround, 1)
    OLED12864_I2C.showString(3, 0, "V", 1)
    basic.pause(500)
    while (index <= Math.round(Valueround) - 1) {
        music.play(music.createSoundExpression(WaveShape.Square, 3540, 1, 255, 90, 100, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
        basic.pause(500)
        index += 1
    }
    basic.pause(5000)
    OLED12864_I2C.clear()
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    OLED12864_I2C.clear()
    roundedOhms = Math.round(Ohms * 1000)
    OLED12864_I2C.showNumber(0, 2, roundedOhms, 1)
    OLED12864_I2C.showString(5, 2, "Ohms", 1)
    basic.pause(500)
    while (index2 <= Math.round(roundedOhms) / 1000 - 1) {
        music.play(music.createSoundExpression(WaveShape.Square, 3540, 1, 255, 90, 100, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
        basic.pause(500)
        index2 += 1
    }
    basic.pause(5000)
    OLED12864_I2C.clear()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    OLED12864_I2C.clear()
    I = pins.analogReadPin(AnalogReadWritePin.P1)
    SetRealI = I / 1023 * 3.3 * 10
    roundI = Math.round(SetRealI * 100) / 100
    OLED12864_I2C.showNumber(0, 1, roundI, 1)
    OLED12864_I2C.showString(3, 1, "miliA", 1)
    basic.pause(500)
    while (index3 <= Math.round(roundI) - 1) {
        music.play(music.createSoundExpression(WaveShape.Square, 3540, 1, 255, 90, 100, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
        basic.pause(500)
        index3 += 1
    }
    basic.pause(5000)
    OLED12864_I2C.clear()
})
let index3 = 0
let roundI = 0
let SetRealI = 0
let I = 0
let index2 = 0
let roundedOhms = 0
let index = 0
let Valueround = 0
let value = 0
let converter = 0
let meisure = 0
let Ohms = 0
let difference = 0
difference = 3.9
radio.setGroup(1991)
OLED12864_I2C.init(60)
basic.showIcon(IconNames.Heart)
