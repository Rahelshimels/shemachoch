import RPi.GPIO as GPIO
import time

# Set the GPIO mode (BCM or BOARD)
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the relay module's IN pin
RELAY_PIN = 12

# Set the relay pin as an output pin
GPIO.setup(RELAY_PIN, GPIO.OUT)

try:
    # Run the loop function indefinitely
    while True:
        # Turn the relay ON (HIGH)
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        time.sleep(1)  # Wait for 1 seconds

        # Turn the relay OFF (LOW)
        GPIO.output(RELAY_PIN, GPIO.LOW)
        time.sleep(1)  # Wait for 1 seconds

except KeyboardInterrupt:
    # If the user presses Ctrl+C, clean up the GPIO configuration
    GPIO.cleanup()
