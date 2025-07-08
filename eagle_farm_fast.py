import pyautogui
import cv2
import numpy as np
import time

time.sleep(3)

def start_match():
    attack_button_location = pyautogui.locateCenterOnScreen("attack-button.png", confidence=0.8)
    pyautogui.click(attack_button_location)
    # 0.30 to 0.60
    time.sleep(0.30)
    find_match_location = pyautogui.locateCenterOnScreen("find-match.png", confidence=0.8)
    pyautogui.click(find_match_location)
    # 7.00 to 8.00
    time.sleep(7.50)

def capture_screen(path="screen.png"):
    screenshot = pyautogui.screenshot()
    screenshot.save(path)

def find_eagle():
    capture_screen("screen.png")

    # Load images using OpenCV
    screen = cv2.imread("screen.png")
    template = cv2.imread("eagle.png")

    # Match template
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    print(f"Match confidence: {max_val:.3f}")

    # Set a confidence threshold
    threshold = 0.5
    if max_val >= threshold:
        # Get the center of the matched region
        h, w, _ = template.shape
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        return (center_x, center_y)
    else:
        return None

def attack():
    pyautogui.click(1630, 1041)
    # 0.30 to 0.50
    time.sleep(0.40)
    pyautogui.moveTo(eagle_pos)
    for i in range(10):
        pyautogui.click()
        # 0.10 to 0.15
        time.sleep(0.125)

def disconnect():
    # 1.00 to 1.50
    time.sleep(1.25)
    surrender_button_location = pyautogui.locateCenterOnScreen("surrender.png", confidence=0.8)
    pyautogui.click(surrender_button_location)
    # 0.50 to 1.00
    time.sleep(0.75)
    confirm_button_location = pyautogui.locateCenterOnScreen("disconnect.png", confidence=0.8)
    pyautogui.click(confirm_button_location)
    # 0.50 to 1.00
    time.sleep(0.75)
    return_button_location = pyautogui.locateCenterOnScreen("return.png", confidence=0.8)
    pyautogui.click(return_button_location)
    # 4.00 to 5.00
    time.sleep(4.50)

def go_next():
    next_button_location = pyautogui.locateCenterOnScreen("next.png", confidence=0.8)
    pyautogui.click(next_button_location)
    time.sleep(10)

for i in range(9999):
    start_match()
    for j in range(9999):
        capture_screen()
        eagle_pos = find_eagle()
        if eagle_pos:
            attack()
            break
        else:
            go_next()
    disconnect()
