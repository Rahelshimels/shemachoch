import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the relay module's IN pin
RELAY_PIN = 12  # Adjust the GPIO pin number as needed

# Set up the relay pin as an output pin
GPIO.setup(RELAY_PIN, GPIO.OUT)

try:
    while True:
        # Turn the relay ON (energize, close the circuit, motor runs)
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        print("Motor open")
        time.sleep(2)  # Motor runs for 2 seconds

        # Turn the relay OFF (de-energize, open the circuit, motor stops)
        GPIO.output(RELAY_PIN, GPIO.LOW)
        print("Motor close")
        time.sleep(2)  # Wait for 2 seconds before the next cycle

except KeyboardInterrupt:
    # Clean up GPIO configuration on exit
    GPIO.cleanup()
    print("Program terminated and GPIO cleaned up")
