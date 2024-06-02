import RPi.GPIO as GPIO
from rpi_lcd import LCD
from time import sleep

# I2C address 0x27, 16 columns, 2 rows
lcd = LCD()

# Mapping of keys on the keypad
KEYPAD = [
    [1, 2, 3, 'A'],
    [4, 5, 6, 'B'],
    [7, 8, 9, 'C'],
    ['*', 0, '#', 'D']    
]

# Define GPIO pins for rows, columns, and relay
# Enter column pins
COL_PINS=[19,13,6,5]
# Enter row pins
ROW_PINS=[21,20,16,12]

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    for row_pin in ROW_PINS:
        GPIO.setup(row_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    for col_pin in COL_PINS:
        GPIO.setup(col_pin, GPIO.OUT)

def read_key():
    for col_num, col_pin in enumerate(COL_PINS):
        GPIO.output(col_pin, GPIO.LOW)
        for row_num, row_pin in enumerate(ROW_PINS):
            if GPIO.input(row_pin) == GPIO.LOW:
                return keys[row_num][col_num]
        GPIO.output(col_pin, GPIO.HIGH)
    return None

def display_key(key):
    lcd.LCD_clear()
    lcd.LCD_display_string(f"Key Pressed:", 1)
    lcd.LCD_display_string(f"{key}", 2)

try:
    setup_gpio()

    while True:
        key = read_key()
        if key is not None:
            display_key(key)

        sleep(0.1)  # Adjust the sleep duration as needed

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    lcd.LCD_clear()
