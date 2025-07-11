import pyautogui
import time

time.sleep(1)

def start_match_and_quit():
    pyautogui.click(250, 1000)
    pyautogui.click(1451, 741)
    while True:
            try:
                battle_machine_loc = pyautogui.locateCenterOnScreen("battle-machine.png", confidence=0.99)
                pyautogui.click(384, 1022)
                time.sleep(0.1)
                pyautogui.click(183, 586)
                time.sleep(0.1)
                pyautogui.click(265, 843)
                time.sleep(0.1)
                pyautogui.click(1195, 696)
                time.sleep(0.5)
                pyautogui.click(1011, 949)
                break
            except:
                pass


if __name__ == "__main__":
    for i in range(20):
        start_match_and_quit()
        time.sleep(2)