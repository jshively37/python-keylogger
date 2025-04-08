import keyboard
import time

def on_key_press(event):
    """Function to handle key press events"""
    # Print the name of the key that was pressed
    print(f"Key pressed: {event.name}")

    # If you want to capture special key combinations (like Ctrl+C)
    if event.name == 'esc':
        print("Escape key pressed - exiting program")
        return False  # Returning False will stop the listener

    return True  # Continue listening

def main():
    print("Keyboard input capture started. Press ESC to exit.")

    # Register the callback function for key press events
    keyboard.on_press(on_key_press)

    # Keep the program running until ESC is pressed
    try:
        keyboard.wait('esc')  # Wait until 'esc' key is pressed
        print("Exiting the program.")
    except KeyboardInterrupt:
        print("Program interrupted by user.")

if __name__ == "__main__":
    main()
