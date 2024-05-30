import pyautogui
import cv2

pyautogui.PAUSE = 0.000


while True:
    billede_koordinater = pyautogui.locateOnScreen('HumanBenchmarkaim.png', confidence=0.4,region=(700, 225, 1700, 600))
    
    if billede_koordinater is not None:
        pyautogui.click(billede_koordinater)
    

import time

try:
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()
        
        # Print the position
        print(f"Mouse position: ({x}, {y})")
        
        # Sleep for a short duration to avoid flooding the output
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Program stopped by user.")
