#include <LCD5110_Graph.h>
#include <Wire.h>
#include <Adafruit_MLX90614.h>

//Pin configuration for MLX90614 temp sensor
//VCC ▶ 5V
//GND ▶ GND
//SCL ▶ A5
//SDA ▶ A4

// This program requires a Nokia 5110 LCD module.
//
// It is assumed that the LCD module is connected to
// the following pins:
//      SCK  - Pin 2
//      MOSI - Pin 3
//      DC   - Pin 4
//      RST  - Pin 5
//      CS   - Pin 6

LCD5110 lcd(2,3,4,6,5); //Use this line with the shield

// LCD5110 lcd(8,9,10,12,11); //Use this line with a standalone Nokia 5110 display

extern uint8_t SmallFont[];
extern uint8_t BigNumbers[];
extern uint8_t uic[];
extern uint8_t uif[];
extern uint8_t splash[];

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup()
{
  Serial.begin(9600);
  lcd.InitLCD(60);
  mlx.begin();
  lcd.drawBitmap(0, 0, splash, 84, 48);
  lcd.update();
  delay(3000);
  if (!mlx.begin()) //sensor health check
  {
    Serial.println("Error connecting to MLX sensor. Check wiring.");
    while (1);
  }
  else
  {
    Serial.println("Done connecting to MLX sensor. starting sensor.");
  }
  delay(3000);
}

void loop()
{
  delay(5000);
  if(Serial.read()=='T') //trigerring the sensor
  {
    Serial.println("Started");
    String temperature="";
    float temp=0;
    lcd.clrScr();
    for(int i=1;i<=10;i++)
    {
      temp=temp+mlx.readObjectTempF(); // reading 10 values for 5 seconds
      delay(500);
    }
    temperature = String(temp/10.0,1); // finally calulating the average to get proper results
    lcd.drawBitmap(0, 0, uif, 84, 48); 
    if(temperature.length()>4)
    {
      temperature.remove(3,2); // formating the output to show upto 1 decimal place
    }
    Serial.print(temperature);Serial.println("*F"); // sending the output to serial moniter for storage and further processing
    lcd.setFont(BigNumbers);
    if(temperature.length()==4)
    {
      lcd.print(temperature,5,19); // printing the temperature in the lcd display to be viewed by the user.
    }
    else
    {
      lcd.print(temperature,15,19);
    }
    lcd.update(); // updating the display to show the new value
    delay(5000);
    lcd.print("",15,19);
    lcd.update();
    Serial.println("Ended");
  }
} 
