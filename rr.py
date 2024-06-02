import mfrc522

def main():
    try:
        # Your code using the mfrc522 module here (replace with your actual logic)
        reader = mfrc522.MFRC522()
        # ... (code to interact with the reader)
    except KeyboardInterrupt:
        mfrc522.GPIO.cleanup()  # Assuming the library uses mfrc522.GPIO

if __name__ == "__main__":
    main()
