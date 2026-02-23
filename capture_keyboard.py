# Script that allows you to take a screenshot of your screen by pressing a keyboard shortcut.

# Import libraries
# We use time to save each screenshot with a unique name
from mss import mss
import keyboard
import time

# Define a function to take screenshots
def screenshot():
    with mss() as sct:
        # time.time() returns a float value
        # int(time.time()) removes the decimal part, making the file name easier to read and cleaner
        file_name = f"screenshot_{int(time.time())}.png"
        # In this case, the screenshot is saved in the Screenshots folder. You can choose any directory to save your screenshots.
        output_path = f"C:\\Users\\Angel\\OneDrive - correounivalle.edu.co\\Pictures\\Screenshots\\{file_name}"
        sct.shot(output = output_path)

# Set up a hotkey to take a screenshot when 'ctrl+alt+s' is pressed
keyboard.add_hotkey('q', screenshot)
# Keep the program running until 'esc' is pressed
keyboard.wait('esc')