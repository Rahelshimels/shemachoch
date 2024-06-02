import RPi.GPIO as GPIO
from time import sleep
from rpi_lcd import LCD
import time

# Initialize display
mylcd = LCD()
mylcd.backlight(1)
mylcd.clear()

# Keypad characters
keypad_chars = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# Define GPIO pin connections (adjust based on your Raspberry Pi model and LCD module)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # Disable warnings for clean output

# Row pins
R1 = 21  # BCM21 (physical pin 40, common)
R2 = 20  # BCM20 (physical pin 38, common)
R3 = 16  # BCM16 (physical pin 36, common)
R4 = 12  # BCM12 (physical pin 32, common)

# Column pins
C1 = 19  # BCM19 (physical pin 35, common)
C2 = 13  # BCM13 (physical pin 33, common)
C3 = 6   # BCM6 (physical pin 31, common)
C4 = 5   # BCM5 (physical pin 29, common)

# Set the correct password
CORRECT_PASSWORD = "1234"

# Initialize GPIO pins
GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
GPIO.setup(R3, GPIO.OUT)
GPIO.setup(R4, GPIO.OUT)
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Display welcome message
mylcd.text('Welcome to', 1)
mylcd.text('Shemachoch', 2)
sleep(5)
mylcd.clear()
mylcd.text('Enter password', 1)
sleep(2)
mylcd.clear()

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        return characters[0]
    if(GPIO.input(C2) == 1):
        return characters[1]
    if(GPIO.input(C3) == 1):
        return characters[2]
    if(GPIO.input(C4) == 1):
        return characters[3]
    GPIO.output(line, GPIO.LOW)
    return None

def get_password():
    entered_password = ""
    while True:
        for i, row in enumerate([R1, R2, R3, R4]):
            char = readLine(row, keypad_chars[i])
            if char is not None:
                if char == '#':  # Enter key
                    return entered_password
                elif char == '*':  # Clear key
                    entered_password = ""
                    mylcd.clear()
                else:
                    entered_password += char
                    mylcd.text('*' * len(entered_password), 2)
                time.sleep(0.3)  # Debounce delay

try:
    while True:
        entered_password = get_password()
        mylcd.clear()
        if entered_password == CORRECT_PASSWORD:
            mylcd.text("Password", 1)
            mylcd.text("Correct", 2)
        else:
            mylcd.text("Password", 1)
            mylcd.text("Incorrect", 2)
        sleep(3)
        mylcd.clear()
        mylcd.text('Enter password', 1)
        sleep(2)
        mylcd.clear()
except KeyboardInterrupt:
    print("\nProgram is stopped")
    mylcd.clear()
finally:
    GPIO.cleanup()
    mylcd.clear()

