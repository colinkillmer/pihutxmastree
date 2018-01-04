#lights go on one by one with a second delay in between. then all blink on and off.
from gpiozero import LED
from time import sleep
from gpiozero import PWMLED
from gpiozero.tools import random_values

star = PWMLED(2)
led18 = PWMLED(19)
led5 = PWMLED(25)
led11 = PWMLED(27)
led10 = PWMLED(17)
led21 = PWMLED(11)
led9 = PWMLED(16)
led12 = PWMLED(26)
led14 = PWMLED(9)
led20 = PWMLED(18)
led1 = PWMLED(4)
led7 = PWMLED(5)
led6 = PWMLED(8)
led3 = PWMLED(13)
led24 = PWMLED(22)
led13 = PWMLED(24)
led2 = PWMLED(15)
led15 = PWMLED(12)
led16 = PWMLED(6)
led17 = PWMLED(20)
led4 = PWMLED(21)
led8 = PWMLED(10)
led23 = PWMLED(23)
led19 = PWMLED(14)
led22 = PWMLED(7)

while True:
    
    #all off
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    led6.off()
    led7.off()
    led8.off()
    led9.off()
    led10.off()
    led11.off()
    led12.off()
    led13.off()
    led14.off()
    led15.off()
    led16.off()
    led17.off()
    led18.off()
    led19.off()
    led20.off()
    led21.off()
    led22.off()
    led23.off()
    led24.off()
    star.off()
    
    #turn on 1 at a time
    led1.on()
    sleep(1)
    led2.on()
    sleep(1)
    led3.on()
    sleep(1)
    led4.on()
    sleep(1)
    led5.on()
    sleep(1)
    led6.on()
    sleep(1)
    led7.on()
    sleep(1)
    led8.on()
    sleep(1)
    led9.on()
    sleep(1)
    led10.on()
    sleep(1)
    led11.on()
    sleep(1)
    led12.on()
    sleep(1)
    led13.on()
    sleep(1)
    led14.on()
    sleep(1)
    led15.on()
    sleep(1)
    led16.on()
    sleep(1)
    led17.on()
    sleep(1)
    led18.on()
    sleep(1)
    led19.on()
    sleep(1)
    led20.on()
    sleep(1)
    led21.on()
    sleep(1)
    led22.on()
    sleep(1)
    led23.on()
    sleep(1)
    led24.on()
    sleep(1)
    star.on()
    sleep(3)
    
    #all off
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    led6.off()
    led7.off()
    led8.off()
    led9.off()
    led10.off()
    led11.off()
    led12.off()
    led13.off()
    led14.off()
    led15.off()
    led16.off()
    led17.off()
    led18.off()
    led19.off()
    led20.off()
    led21.off()
    led22.off()
    led23.off()
    led24.off()
    star.off()
    sleep(1)
    
    #light in groups
    led1.on()
    led2.on()
    led3.on()
    led4.on()
    led5.on()
    led6.on()
    led7.on()
    led8.on()
    sleep(.3)
    led9.on()
    led10.on()
    led11.on()
    led12.on()
    led13.on()
    led14.on()
    led15.on()
    led16.on()
    sleep(.3)
    led17.on()
    led18.on()
    led19.on()
    led20.on()
    led21.on()
    led22.on()
    led23.on()
    led24.on()
    sleep(1)
    star.on()
    sleep(1)
    #turn off in groups
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    led6.off()
    led7.off()
    led8.off()
    sleep(.3)
    led9.off()
    led10.off()
    led11.off()
    led12.off()
    led13.off()
    led14.off()
    led15.off()
    led16.off()
    sleep(.3)
    led17.off()
    led18.off()
    led19.off()
    led20.off()
    led21.off()
    led22.off()
    led23.off()
    led24.off()
    sleep(1)
    
    #turn on dim
    led1.value=0
    led2.value=0
    led3.value=0
    led4.value=0
    led5.value=0
    led6.value=0
    led7.value=0
    led8.value=0
    led9.value=0
    led10.value=0
    led11.value=0
    led12.value=0
    led13.value=0
    led14.value=0
    led15.value=0
    led16.value=0
    led17.value=0
    led18.value=0
    led19.value=0
    led20.value=0
    led21.value=0
    led22.value=0
    led23.value=0
    led24.value=0
    led1.value=.1
    led2.value=.1
    led3.value=.1
    led4.value=.1
    led5.value=.1
    led6.value=.1
    led7.value=.1
    led8.value=.1
    led9.value=.1
    led10.value=.1
    led11.value=.1
    led12.value=.1
    led13.value=.1
    led14.value=.1
    led15.value=.1
    led16.value=.1
    led17.value=.1
    led18.value=.1
    led19.value=.1
    led20.value=.1
    led21.value=.1
    led22.value=.1
    led23.value=.1
    led24.value=.1
    sleep(5)

    #pulse all on
    brightness = .3
    while brightness <= 1:
        led1.value=brightness
        led2.value=brightness
        led3.value=brightness
        led4.value=brightness
        led5.value=brightness
        led6.value=brightness
        led7.value=brightness
        led8.value=brightness
        led9.value=brightness
        led10.value=brightness
        led11.value=brightness
        led12.value=brightness
        led13.value=brightness
        led14.value=brightness
        led15.value=brightness
        led16.value=brightness
        led17.value=brightness
        led18.value=brightness
        led19.value=brightness
        led20.value=brightness
        led21.value=brightness
        led22.value=brightness
        led23.value=brightness
        led24.value=brightness
        sleep(.7)
        brightness = brightness + .1
    
    #blink
    r=0
    while r<5:
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        led5.off()
        led6.off()
        led7.off()
        led8.off()
        led9.off()
        led10.off()
        led11.off()
        led12.off()
        led13.off()
        led14.off()
        led15.off()
        led16.off()
        led17.off()
        led18.off()
        led19.off()
        led20.off()
        led21.off()
        led22.off()
        led23.off()
        led24.off()
        sleep(.5)
    
        led1.on()
        led2.on()
        led3.on()
        led4.on()
        led5.on()
        led6.on()
        led7.on()
        led8.on()
        led9.on()
        led10.on()
        led11.on()
        led12.on()
        led13.on()
        led14.on()
        led15.on()
        led16.on()
        led17.on()
        led18.on()
        led19.on()
        led20.on()
        led21.on()
        led22.on()
        led23.on()
        led24.on()
        sleep(.5)
        r=r+1
    
    #all dim off
    brightness = 1
    while brightness >=0 and brightness <=1:
        led1.value=brightness
        led2.value=brightness
        led3.value=brightness
        led4.value=brightness
        led5.value=brightness
        led6.value=brightness
        led7.value=brightness
        led8.value=brightness
        led9.value=brightness
        led10.value=brightness
        led11.value=brightness
        led12.value=brightness
        led13.value=brightness
        led14.value=brightness
        led15.value=brightness
        led16.value=brightness
        led17.value=brightness
        led18.value=brightness
        led19.value=brightness
        led20.value=brightness
        led21.value=brightness
        led22.value=brightness
        led23.value=brightness
        led24.value=brightness
        sleep(.7)
        brightness = brightness - .1
    sleep(1)
        
    #star blinks
    b=0
    while b<3:
        star.off()
        sleep(.5)
        star.on()
        sleep(.5)
        b=b+1
    sleep(3)
    
    #all twinkle
    t=0
    while t<30:
        led1.off()
        sleep(.1)
        led1.on()
        sleep(.2)
        led2.off()
        sleep(.1)
        led2.on()
        sleep(.2)
        led3.off()
        sleep(.1)
        led3.on()
        sleep(.2)
        led4.off()
        sleep(.1)
        led4.on()
        sleep(.2)
        led5.off()
        sleep(.1)
        led5.on()
        sleep(.2)
        led6.off()
        sleep(.1)
        led6.on()
        sleep(.2)
        led7.off()
        sleep(.1)
        led7.on()
        sleep(.2)
        led8.off()
        sleep(.1)
        led8.on()
        sleep(.2)
        led9.off()
        sleep(.1)
        led9.on()
        sleep(.2)
        led10.off()
        sleep(.1)
        led10.on()
        sleep(.2)
        led11.off()
        sleep(.1)
        led11.on()
        sleep(.2)
        led12.off()
        sleep(.1)
        led12.on()
        sleep(.2)
        led13.off()
        sleep(.1)
        led13.on()
        sleep(.2)
        led14.off()
        sleep(.1)
        led14.on()
        sleep(.2)
        led15.off()
        sleep(.1)
        led15.on()
        sleep(.2)
        led16.off()
        sleep(.1)
        led16.on()
        sleep(.2)
        led17.off()
        sleep(.1)
        led17.on()
        sleep(.2)
        led18.off()
        sleep(.1)
        led18.on()
        sleep(.2)
        led19.off()
        sleep(.1)
        led19.on()
        sleep(.2)
        led20.off()
        sleep(.1)
        led20.on()
        sleep(.2)
        led21.off()
        sleep(.1)
        led21.on()
        sleep(.2)
        led22.off()
        sleep(.1)
        led22.on()
        sleep(.2)
        led23.off()
        sleep(.1)
        led23.on()
        sleep(.2)
        led24.off()
        sleep(.1)
        led24.on()
        sleep(.2)
        t=t+1
    #all off except star
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    led6.off()
    led7.off()
    led8.off()
    led9.off()
    led10.off()
    led11.off()
    led12.off()
    led13.off()
    led14.off()
    led15.off()
    led16.off()
    led17.off()
    led18.off()
    led19.off()
    led20.off()
    led21.off()
    led22.off()
    led23.off()
    led24.off()
    sleep(3)
    
    #star fades
    brightness = 1
    while brightness >=0 and brightness <=1:
        star.value=brightness
        brightness=brightness-.1
    sleep(2)
    star.off()
    



