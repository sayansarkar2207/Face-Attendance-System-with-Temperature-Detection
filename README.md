# Face Attendance System with Temperature Detection

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
2. BL   - 5V
3. VCC  - 3.3V
4. CLK  - Pin 8
5. DIN  - Pin 9
6. DC   - Pin 10
7. RST  - Pin 12
8. CE   - Pin 11

### Arduino Libraries

1. Adafruit MLX90614 library: <a href="https://github.com/adafruit/Adafruit-MLX90614-Library">Click to view source</a> ( Already included in Arduino Libraries )
2. Nokia 5110 Graph library: <a href="http://www.rinkydinkelectronics.com/library.php?id=47">Click to view source</a>  ( Already included in Arduino Libraries )

#
## Steps to be followed for setup:
1.First, we must install python on the machine and add it to path variable.

2.We must check that our camera is working, and the Arduino is connected.

3.Now we have to proceed to the wiring of Arduino and the temperature sensor.

4.Now we must upload the Arduino program to the Arduino Board.
![image](https://github.com/sayansarkar2207/Face-Attendance-System-with-Temperature-Detection/assets/70804496/74c868f8-f0ee-423c-a28d-cc7a47abe239)

5.Now run the Codance.bat file
![image](https://github.com/sayansarkar2207/Face-Attendance-System-with-Temperature-Detection/assets/70804496/85f7121f-99e1-48b9-bb1a-a0657ff71833)

6.Now a lot of stuff will be loaded and finally you will hear the voice assistant and a web UI will appear. Click on Start.
![image](https://github.com/sayansarkar2207/Face-Attendance-System-with-Temperature-Detection/assets/70804496/7ea5a63d-ffe7-4768-9df1-26650f95ae86)

7.Now let’s talk about the flow of the program.
![image](https://github.com/sayansarkar2207/Face-Attendance-System-with-Temperature-Detection/assets/70804496/7570d337-8199-4180-bb39-7a80ce9f3b3e)

8.So, we have finally completed the setup.

#
## Future Improvements
The scope of the future of the proposed project could be, photographing students' detailed details and using any cloud technology to store these images. The system can be configured and used on ATM machines to detect fraud. The system can be disseminated to ensure and track the attendance of various government offices and companies. To ensure access control and identification of real users can also be included in bank cabinets and vaults. To identify criminals this program can be used by the police as well.
The purpose of a face-to-face monitoring program is to simplify the time-consuming process and the teacher's efforts that can be used in teaching, are a simple and easy process for students as well. The program will take pictures of students in the classroom and use a face recognition algorithm to mark their presence on the sheet. In this way the class will be marked for its presence without wasting time on a call that often leads to the presence of a representative. User of this program is teacher, admin, students. The program will allow the instructor to control the visit where the photography process should begin. The system will also allow the administrator to update the site when a new student registers. For students, this program will help guide their attendance. Readers can only view their attendance and will not be able to edit or manage system database. The system administrator will be responsible for managing, uploading and updating the site.
