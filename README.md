# Arduino_RGB_LED_Color_Detection

## Arduino with Python detects color and displays as glowing LED of same color.

## Components:
- Arduino
- BreadBoard
- USB cable
- RGB LED / Red Green Blue LEDs
- 1k Resistor
- Wires

## Softwares:
- Arduino-nightly
- Python

## Libraries:
- Python:
  1. Numpy
  2. Open-cv
  3. Pyserial

## Pins:
- PIN 11 – Red LED
- PIN 9 – Green LED
- PIN 10 – Blue LED
- PIN GND – Ground

## Circuit Diagram:
![image](https://github.com/user-attachments/assets/cd490fc7-0bf9-4dbb-ad71-1f2132ab8195)

## Connections:
Connect the +ve end of the red led to pin 11 then connect the +ve end of the blue led to pin 10 then connect +ve end of the green led to pin 9. Take all the grounds common and connect to a 1k ohm resistor. Now connect the other end of the resistor to GND pin on the Arduino.

## Installing Libraries:
- Open CMD and type the following:
  1. pip install numpy
  2. pip install opencv-python
  3. pip install pyserial
