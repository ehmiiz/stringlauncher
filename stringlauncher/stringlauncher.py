import time
import tkinter as tk
from pynput.keyboard import Controller, Key

def countdown():
    # Simply counts down
    global countdown_val
    countdown_val = int(countdown_var.get())

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
    '@': (Key.alt_gr, '2'),
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

def launch():
    # Sleeps 3 seconds (or whatever countdown is), types hidden string.
    hidden_string = entry_var.get()
    previous_char = None
    # Sleep
    time.sleep(countdown_val)
    keyboard = Controller()
    for hidden_char in hidden_string:

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
            keyboard.type(hidden_char)
            keyboard.release(hidden_char)

        previous_char = hidden_char
        time.sleep(0.03)

    if previous_char in ['`', "^", '´']:
        # if this is true, the last element of the loop must be spaced
        keyboard.press(Key.space)
        keyboard.release(Key.space)

root = tk.Tk()
root.title("StringLauncher")
root.geometry("300x150")  # Set default window size

# Make window non-resizable
root.resizable(False, False)

# Entry for hidden string
entry_label = tk.Label(root, text="Enter hidden string:")
entry_label.pack()
entry_var = tk.StringVar()
entry_entry = tk.Entry(root, textvariable=entry_var, show='*')  # show '*' instead of actual characters
entry_entry.pack()

# Countdown dropdown
countdown_label = tk.Label(root, text="Seconds to countdown:")
countdown_label.pack()
countdown_var = tk.StringVar()
countdown_var.set(3)  # default value
countdown_dropdown = tk.OptionMenu(root, countdown_var, *[str(i) for i in range(3, 11)])
countdown_dropdown.pack()

# Launch button
launch_button = tk.Button(root, text="Launch", command=launch)
launch_button.pack()

countdown_val = 3  # default value for countdown

root.mainloop()
