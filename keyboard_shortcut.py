#The keyboard module allows you to work with the keyboard in Python, enabling you to listen for key presses, send key events, and create hotkeys.
import keyboard
# This will display the documentation and available functions in the keyboard library directly in the console.
# help(keyboard)

# keyboard.add_hotkey() allows you to assign a function to a key or key combination.
# keyboard.add_hotkey('a', lambda: keyboard.write('Geek'))
# keyboard.add_hotkey('q', lambda: print("you entered q hotkey"))

# Send ALT+F4 at the same time, and then send space,
# (This will close any currently open window)
# keyboard.send("alt+F4, space")

# This will press the CTRL button and then release it.
# keyboard.press("ctrl")
# keyboard.release("ctrl")

# keyboard.write which can be used to type a sequence of characters - It writes where you have the cursor, not in the console - delay parameter is optional - Setting the delay indicates the number of seconds to wait between key presses
# keyboard.write("Python Programming is always fun!", delay = 0.5)

# Record all keyboard clicks until esc is clicked
# events = keyboard.record('esc')
# Play these events
# keyboard.play(events)
# Print all typed strings in the events
# print(list(keyboard.get_typed_strings(events)))

# Log all pressed keys - This will print anything you press on your keyboard.
# keyboard.on_release(lambda e: print(e.name))


# Handling Hotkeys
# Hotkeys are combinations of keys that, when pressed, trigger a specific action. The keyboard.add_hotkey function is used to define hotkeys. Here is an example:

# import keyboard
# def hotkey_callback():
#     print("Hotkey combination was pressed!")
# keyboard.add_hotkey('ctrl+shift+a', hotkey_callback)
# keyboard.wait('esc')

# In this code, the combination ctrl+shift+a is defined as a hotkey. When this combination is pressed, the hotkey_callback function is executed.


#Example of using keyboard.write() to type a message when a specific key is pressed - Si se va a usar una combinación con ctrl, es mejor usar solo print
# def message():
#     keyboard.write("Hello, world!")
#     # Avoid using Ctrl as a modifier with keyboard.write() to prevent stuck keys

# # Use a simple key (no modifiers) to avoid issues with keyboard.write
# keyboard.add_hotkey('m', message)
# keyboard.wait('Esc') # program does not end until esc is pressed