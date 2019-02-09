### Mouse Jiggler ###

# pip install pyautogui (first time only)

import pyautogui
import time

#VARIABLES 
go=1
timeDelay = 2 #seconds
dragAmount = 100 #pixles
dragTime = .1 #seconds
orig_x , orig_y = pyautogui.position() #get the starting mouse poition

print("***START JIGGLE***")
print("Moving your mouse will exit the jiggler...")

while go>0:
    curr_x , curr_y = pyautogui.position() #get current mouse position
    
    if curr_x != orig_x:
        #stops jiggler if mouse is manually moved on the screen
        print("***END JIGGLE***")
        break
    
    pyautogui.moveRel(dragAmount, 0, duration = dragTime)
    pyautogui.moveRel(-dragAmount, 0, duration = dragTime)  
    time.sleep(timeDelay)


#press ctl + alt + N to     START 
#press ctl + alt + M to     FORCE STOP 



#press ctl + alt + N to START
#press ctl + alt + M to STOP 
