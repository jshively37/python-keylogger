from pynput import keyboard

def on_press(key):
    try:
        print(key.char)
    except AttributeError:
        print(key.char)

def on_release(key):
    print(key)


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)

listener.start()
