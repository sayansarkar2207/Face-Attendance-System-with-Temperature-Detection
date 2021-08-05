# Dashing Attendance 

## Our Objective
We are designing a AI based face recognization system for taking attendance of the employees and record their body temperature, to predict any covid positive case.
This is safe in comparison to fingerprint attendance as all the people need to touch the same fingerprint sensor, which is not favourable for the pandemic conditions as need to minimise social contact.
Moreover the device will also register the person's temperature to keep a check on them and predict any abnormal condition.

# 
## For Temperature dectection and display ( Arduino related part )
### a) Materials required:
1) Arduino Uno
2) Jumper wires ( as required )
3) ISB-TS45D Infrared Thermopile Sensor x 1     <a href="https://robu.in/product/isb-ts45d-infrared-thermopile-sensor/">Click to Buy</a>
4) Nokia 5110 LCD Display Module – Blue x 1     <a href="https://robu.in/product/nokia-5110-lcd-display-module-nokia-5110-84x48-lcd-module-blue-backlight/">Click to buy</a>
5) Resistor 4.75K ohm x 2
6) Capacitor 100nF x1
7) Breadboard ( small ) x 1 { if required }
#

### b) Some details about the sensors:

#### 1) ISB-TS45D Infrared Thermopile Sensor
<a href="https://robu.in/product/isb-ts45d-infrared-thermopile-sensor/"><img src="https://cdn-shop.adafruit.com/970x728/1747-00.jpg" width="500px"></a>

<a href="https://robu.in/product/isb-ts45d-infrared-thermopile-sensor/">Click to Buy</a>

Infrared Thermopile Sensor can measure the temperature without contact by detecting the infrared energy of an object. And the higher the temperature, the more infrared energy is produced.

Thermopile sensing elements consist of small thermocouples on silicon chips that absorb energy and produce output signals. ISB-TS45D Infrared Thermopile Sensor can be widely used in non-contact temperature measurement. This product consists of infrared filters, thermistors, and other components, and packaged by TO-46Made of metal, it has high reliability and high sensitivity.

Application:

Non-contact temperature measurement Ear thermometer, forehead thermometer Industrial continuous temperature control

Specs:

1. Detection angle: 90°
2. Thermopile resistance: 95 to 140 KΩ
3. Noise voltage: 45 nV/Hz1/2
4. NEP: 0.27 nW/Hz1/2
5. Voltage Response: 20.11 Vmm2/w
6. Responsivity: 124

Pin configuration for MLX90614 temp sensor
1. VCC ▶ 5V
2. GND ▶ GND
3. SCL ▶ A5
4. SDA ▶ A4

#### 2) Nokia 5110 LCD Display Module – Blue
<a href="https://robu.in/product/nokia-5110-lcd-display-module-nokia-5110-84x48-lcd-module-blue-backlight/"><img src="https://robu.in/wp-content/uploads/2017/09/HTB1hQN7NFXXXXXUXpXX760XFXXXr.png" width="500px"></a>

<a href="https://robu.in/product/nokia-5110-lcd-display-module-nokia-5110-84x48-lcd-module-blue-backlight/">Click to buy</a>

The name of this product itself is enough to explain its origin. Yes of course !!! this LCD module was used in old Nokia 5110/3310 cell phones. Now its been widely used by hobbyists for graphics, text etc.

Though it’s an industrial module, this LCD display is extremely easy to use. The Nokia 5110 is a basic graphic LCD screen for lots of applications. It was originally intended for as a cell phone screen.

This Nokia 5110 LCD Display Module is mounted on an easy to solder PCB. The Nokia 5110 LCD Module uses a Philips PCD8544 LCD driver, which is designed for mobile phones.

Nokia 5110 LCD Display Module is a low-cost monochrome LCD module comprised of 84 X 48 pixels that can be used to display rich graphics and text content. This module is a revision that accepts 3-5V input. So no extra level shifter is needed.

It uses the PCD8544 controller, which is the same used in the Nokia 3310 LCD. The PCD8544 is a low power CMOS LCD controller/driver, designed to drive a graphic display of 48 rows and 84 columns. All necessary functions for the display are provided in a single chip, including on-chip generation of LCD supply and bias voltages, resulting in a minimum of external components and low power consumption. The PCD8544 interfaces to microcontrollers through a serial bus interface.

Specs:

1. Power supply voltage: 2.7 V-3.3 V/5 V
2. Data interface level: 2.7-5V.
3. Resolution: 84 x 48 pixel
4. Backlight power supply voltage: highest 3.3 V.
5. Backlight: Blue.

Pin Configuration :
1. RST– reset
2. CE– chip selection
3. DC– data/commands choice
4. DIN– serial data line
5. CLK– serial Clock Speed.
6. VCC– 3.3V
7. LIGHT– backlight control terminal
8. GND– power negative



### c) Connection procedure of the components with arduino
#
#### i) Connecting the Temperature sensor
<img src="https://hackster.imgix.net/uploads/attachments/225384/FOQV7G4IIQA0IHC.LARGE.jpg" width="500px">

If your sensor is not on breakout board gonna need to pull-up the SDA and SCL pins of it, the put a capacitor between the GND and +3.3v pins. If its on breakout board then just connect the pins to the Arduino board: 
1. SDA with A5
2. SCL with A4
3. GND to GND
4. +3.3 to 3.3v

#### ii) Connecting the LCD Display
<img src="https://www.electronics-lab.com/wp-content/uploads/2017/11/nokia-and-arduino_bb.png" width="500px">

Just connect the pins to the Arduino:
1. GND  - GND
2. BL   - GND
3. VCC  - 3.3V
4. CLK  - Pin 8
5. DIN  - Pin 9
6. DC   - Pin 10
7. RST  - Pin 12
8. CE   - Pin 11

























# Adafruit-MLX90614-Library [![Build Status](https://github.com/adafruit/Adafruit-MLX90614-Library/workflows/Arduino%20Library%20CI/badge.svg)](https://github.com/adafruit/Adafruit-MLX90614-Library/actions)[![Documentation](https://github.com/adafruit/ci-arduino/blob/master/assets/doxygen_badge.svg)](http://adafruit.github.io/Adafruit-MLX90614-Library/html/index.html)

This is a library for the MLX90614 temperature sensor

<a href="https://www.adafruit.com/products/1747"><img src="https://cdn-shop.adafruit.com/970x728/1747-00.jpg" width="500px"></a>

Designed and tested  to work with the MLX90614 sensors in the adafruit shop
 * https://www.adafruit.com/products/1747 3V version
 * https://www.adafruit.com/products/1748 5V version

Check out the links above for our tutorials and wiring diagrams

Adafruit invests time and resources providing this open source code, please support Adafruit and open-source hardware by purchasing products from Adafruit!

# Installation
To install, use the Arduino Library Manager and search for "Adafruit-MLX90614-Library" and install the library.

# Contributing

Contributions are welcome! Please read our [Code of Conduct](https://github.com/adafruit/Adafruit-MLX90614-Library/blob/master/CODE_OF_CONDUCT.md>)
before contributing to help this project stay welcoming.

## Documentation and doxygen
Documentation is produced by doxygen. Contributions should include documentation for any new code added.

Some examples of how to use doxygen can be found in these guide pages:

https://learn.adafruit.com/the-well-automated-arduino-library/doxygen

https://learn.adafruit.com/the-well-automated-arduino-library/doxygen-tips

## Formatting and clang-format
This library uses [`clang-format`](https://releases.llvm.org/download.html) to standardize the formatting of `.cpp` and `.h` files. 
Contributions should be formatted using `clang-format`:

The `-i` flag will make the changes to the file.
```bash
clang-format -i *.cpp *.h
```
If you prefer to make the changes yourself, running `clang-format` without the `-i` flag will print out a formatted version of the file. You can save this to a file and diff it against the original to see the changes.

Note that the formatting output by `clang-format` is what the automated formatting checker will expect. Any diffs from this formatting will result in a failed build until they are addressed. Using the `-i` flag is highly recommended.

### clang-format resources
  * [Binary builds and source available on the LLVM downloads page](https://releases.llvm.org/download.html)
  * [Documentation and IDE integration](https://clang.llvm.org/docs/ClangFormat.html)

## About this Driver
Written by Limor Fried for Adafruit Industries.
BSD license, check license.txt for more information
All text above must be included in any redistribution
