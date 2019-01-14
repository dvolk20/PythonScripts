### Mouse Jiggler ###
# pip install pyautogui

import pyautogui
print(pyautogui.size())

go=1
while go>0:
    pyautogui.dragRel(100, 0, duration = 1) 
    pyautogui.dragRel(0, 100, duration = 1) 
    pyautogui.dragRel(-100, 0, duration = 1) 
    pyautogui.dragRel(0, -100, duration = 1)

#press ctl + alt + N to START
#press ctl + alt + M to STOP 
