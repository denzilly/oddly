import keyboard
import time
# Using time.sleep, we can dramatically decrease the amount of CPU our program
# uses.

c1_sell = "4"
c1_buy = "5"
c2_sell = "1"
c2_buy = "2"
ARM = "F24"
armed = False


# Remember that the order in which the hotkey is set up is the order you
# need to press the keys.

while True:

  if keyboard.is_pressed(ARM):
      if armed == False:
        print("ARMED!")
        armed = True
        time.sleep(0.5)
      else:
        print("DISARMED!")
        armed = False
        time.sleep(0.5)

  if armed == True:
    if keyboard.is_pressed(c1_sell):
      print("SELL C1!")
      time.sleep(0.2)
    elif keyboard.is_pressed(c1_buy):
      print("BUY C1!")
      time.sleep(0.2)
    elif keyboard.is_pressed(c2_sell):
      print("SELL C2!")
      time.sleep(0.2)
    elif keyboard.is_pressed(c2_buy):
      print("BUY C2!")
      time.sleep(0.2)
  
  time.sleep(0.01)