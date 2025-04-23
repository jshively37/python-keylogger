import keyboard
import win32gui
import win32api
import win32process

def get_active_window_title():
    """Gets the title of the currently active window."""
    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)
    return title

def get_active_window_process_name():
    """Gets the process name of the currently active window."""
    hwnd = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    try:
        process_handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid)
        process_name = win32process.GetModuleFileNameEx(process_handle, 0)
        win32api.CloseHandle(process_handle)
        return process_name
    except Exception as e:  # pylint: disable=broad-except
        print(f"Error getting process name: {e}")
        return None

def on_key_press(event):
    """Handles key press events, logging the key and active window."""
    title = get_active_window_title()
    process_name = get_active_window_process_name()

    print(f"Key pressed: {event.name} in window: {title} ({process_name})")

    if event.name == 'esc':
        print("Escape key pressed - exiting program")
        return False  # Stop listening

    return True  # Keep listening


def main():
    """Starts the keyboard listener and waits for the 'esc' key."""
    print("Keyboard input capture started. Press ESC to exit.")

    keyboard.on_press(on_key_press)

    try:
        keyboard.wait('esc')
        print("Exiting the program.")
    except KeyboardInterrupt:
        print("Program interrupted by user.")

if __name__ == "__main__":
    main()
