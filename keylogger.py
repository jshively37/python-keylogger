import keyboard


def on_key_press(event):
    """Function to handle key press events"""

    print(f"Key pressed: {event.name}")

    if event.name == "esc":
        print("Escape key pressed - exiting program")
        return False

    return True


def main():
    print("Keyboard input capture started. Press ESC to exit.")

    keyboard.on_press(on_key_press)

    try:
        keyboard.wait("esc")
        print("Exiting the program.")
    except KeyboardInterrupt:
        print("Program interrupted by user.")


if __name__ == "__main__":
    main()
