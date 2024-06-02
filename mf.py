import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Create an instance of the SimpleMFRC522 class
reader = SimpleMFRC522()

try:
    # Read the RFID tag
    id, text = reader.read()
    print(f"ID: {id}")
    print(f"Text: {text}")

finally:
    # Clean up the GPIO pins
    GPIO.cleanup()
