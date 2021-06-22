import keyboard
import time
# Using time.sleep, we can dramatically decrease the amount of CPU our program
# uses.

hotkey = "shift + ctrl + 1"
# Remember that the order in which the hotkey is set up is the order you
# need to press the keys.

while True:
  if keyboard.is_pressed(hotkey):
    print("Hotkey is being pressed")
    time.sleep(0.5)
  time.sleep(0.01)