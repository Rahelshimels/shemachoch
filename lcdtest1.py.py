from RPi_GPIO_i2c_LCD import lcd
from time import sleep

## Address of backpack
i2c_address = 0x27

## Initalize display
LCD = lcd.HD44780(i2c_address)

## Set string value to buffer
LCD.set("welcome to",1)
LCD.set(" shemachoch",2)

sleep(2)
LCD.set("scan rfid to",1)
sleep(1)
LCD.set("Enter Password",2)
