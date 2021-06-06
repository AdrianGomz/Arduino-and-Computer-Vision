# Arduino-and-Computer-Vision

## required libraries
+ cv2
+ numpy
+ pyfirmata

## StandartFirmata
First we will have to load in the Arduino the standartFirmata program, which comes in the example programs of the Arduino IDE.

## settings

The first thing we will have to change will be the port. In this line of code we will have to put the port in which our Arduino is connected, in this case it is COM15

``` python
ard=pyfirmata.Arduino("COM15")
```
The second thing we eill have to change is the servomotor pin. By deafult I selected the pin 9, but it can be change for another pin.
``` python
servo_motor=ard.get_pin('d:9:s')
```

To conect the leds we have to conect 6 leds, one for each pin from 3 to 6 on the arduino.




[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/akrJ4UTmD2M/0.jpg)](https://www.youtube.com/watch?v=akrJ4UTmD2M)
