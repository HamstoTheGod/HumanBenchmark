import pyautogui
import cv2

pyautogui.PAUSE = 0.000


while True:
    billede_koordinater = pyautogui.locateOnScreen('HumanBenchmarkaim.png', confidence=0.4,region=(700, 225, 1700, 600))
    
    if billede_koordinater is not None:
        pyautogui.click(billede_koordinater)
    


