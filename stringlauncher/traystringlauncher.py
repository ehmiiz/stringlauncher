import time
from tkinter import simpledialog
import tkinter as tk
from pynput.keyboard import Controller, Key
from PIL import Image
from pystray import Icon as icon, Menu as menu, MenuItem as item

root = tk.Tk()
root.withdraw()

char_mappings = {
    '!': (Key.shift, '1'),
    '"': (Key.shift, '2'),
    '#': (Key.shift, '3'),
    '¤': (Key.shift, '4'),
    '%': (Key.shift, '5'),
    '&': (Key.shift, '6'),
    '/': (Key.shift, '7'),
    '(': (Key.shift, '8'),
    ')': (Key.shift, '9'),
    '=': (Key.shift, '0'),
    '?': (Key.shift, '+'),
    '`': (Key.shift, '´'),
    #'@': (Key.alt_gr, '2'),
    '£': (Key.alt_gr, '3'),
    '$': (Key.alt_gr, '4'),
    '€': (Key.alt_gr, '5'),
    '{': (Key.alt_gr, '7'),
    '[': (Key.alt_gr, '8'),
    ']': (Key.alt_gr, '9'),
    '}': (Key.alt_gr, '0'),
    '\\': (Key.alt_gr, '+'),
    '|': (Key.alt_gr, '<'),
    'µ': (Key.alt_gr, 'm'),
    '*': (Key.shift, "'"),
    '^': (Key.shift, '¨'),
    '_': (Key.shift, '_'),
    ':': (Key.shift, '.'),
    ';': (Key.shift, ','),
    '½': (Key.shift, '§'),
    'A': (Key.shift, 'a'),
    'B': (Key.shift, 'b'),
    'C': (Key.shift, 'c'),
    'D': (Key.shift, 'd'),
    'E': (Key.shift, 'e'),
    'F': (Key.shift, 'f'),
    'G': (Key.shift, 'g'),
    'H': (Key.shift, 'h'),
    'I': (Key.shift, 'i'),
    'J': (Key.shift, 'j'),
    'K': (Key.shift, 'k'),
    'L': (Key.shift, 'l'),
    'M': (Key.shift, 'm'),
    'N': (Key.shift, 'n'),
    'O': (Key.shift, 'o'),
    'P': (Key.shift, 'p'),
    'Q': (Key.shift, 'q'),
    'R': (Key.shift, 'r'),
    'S': (Key.shift, 's'),
    'T': (Key.shift, 't'),
    'U': (Key.shift, 'u'),
    'V': (Key.shift, 'v'),
    'W': (Key.shift, 'w'),
    'X': (Key.shift, 'x'),
    'Y': (Key.shift, 'y'),
    'Z': (Key.shift, 'z'),
    'Å': (Key.shift, 'å'),
    'Ä': (Key.shift, 'ä'),
    'Ö': (Key.shift, 'ö'),
}

delay_seconds = 3

def simulate_keystrokes(text, delay):
    time.sleep(delay) 
    keyboard = Controller()
    previous_char = None

    for hidden_char in text:
        if previous_char in ['`', "^", '´']:
            keyboard.press(Key.space)
            keyboard.release(Key.space)

        if hidden_char in char_mappings:
            modifier, char = char_mappings[hidden_char]
            keyboard.press(modifier)
            keyboard.press(char)
            keyboard.release(char)
            keyboard.release(modifier)
        else:
            if hidden_char in ['@', '£', '$', '€', '{', '[', ']', '}', '\\', '|']:
                keyboard.type(hidden_char)
                continue
            
            keyboard.type(hidden_char)

        previous_char = hidden_char
        time.sleep(0.03)

    if previous_char in ['`', "^", '´']:
        keyboard.press(Key.space)
        keyboard.release(Key.space)

def ask_for_text():
    text = simpledialog.askstring("Text to Type", "Enter the text you want to type:", parent=root)
    if text:
        simulate_keystrokes(text, delay_seconds)

def set_delay():
    """Allows the user to set the typing delay."""
    global delay_seconds
    delay = simpledialog.askinteger("Set Delay", "Enter the delay in seconds before typing:", initialvalue=delay_seconds, parent=root)
    if delay is not None:
        delay_seconds = delay

def create_tray_icon():
    icon_image = Image.open(f'C:\\Users\\emilt\\git\\StringLauncher\\stringlauncher\\favicon.ico')
    tray_icon = icon("StringLauncher", icon_image, menu=menu(
        item("Type Text", ask_for_text),
        item("Set Delay", set_delay),
        item("Exit", lambda icon: icon.stop())
    ))
    tray_icon.run()

if __name__ == "__main__":
    create_tray_icon()