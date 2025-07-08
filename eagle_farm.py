import pyautogui
import cv2
import numpy as np
import time
import random
import mss

# ------------------- Human-like Interaction Helpers -------------------

def human_click(x, y):
    rand_x = x + random.randint(-5, 5)
    rand_y = y + random.randint(-5, 5)
    duration = random.uniform(0.05, 0.2)
    pyautogui.moveTo(rand_x, rand_y, duration=duration)
    pyautogui.click()

def rsleep(low, high):
    time.sleep(random.uniform(low, high))

def maybe_idle():
    if random.random() < 0.1:
        pause_time = random.uniform(3, 6)
        print(f"[Idle] Simulating human pause for {pause_time:.2f}s...")
        time.sleep(pause_time)

# ------------------- Screen Capture (FAST) -------------------

def grab_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Fullscreen
        img = sct.grab(monitor)
        screen = np.array(img)
        screen = cv2.cvtColor(screen, cv2.COLOR_BGRA2BGR)
        return screen

# ------------------- Template Matching (OpenCV) -------------------

def match_template(template_path, threshold=0.8):
    screen = grab_screen()
    template = cv2.imread(template_path)

    if template is None:
        print(f"[ERROR] Could not read {template_path}")
        return None

    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    print(f"[{template_path}] Match confidence: {max_val:.3f}")

    if max_val >= threshold:
        h, w, _ = template.shape
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        return (center_x, center_y)
    else:
        return None

# ------------------- Game Logic -------------------

def start_match():
    print("[START] Starting Match...")
    loc = match_template("attack-button.png", 0.8)
    if loc:
        human_click(*loc)
        rsleep(0.3, 0.6)    

    loc = match_template("find-match.png", 0.8)
    if loc:
        human_click(*loc)
        rsleep(7.0, 8.0)

def find_eagle():
    return match_template("eagle.png", 0.55)

def attack(eagle_pos):
    print("[ATTACK] Dropping spells on Eagle...")
    human_click(1530 + random.randint(-3, 3), 1041 + random.randint(-3, 3))  # Select spell
    rsleep(0.3, 0.5)

    pyautogui.moveTo(eagle_pos[0], eagle_pos[1], duration=random.uniform(0.05, 0.2))
    for _ in range(11):
        human_click(*eagle_pos)
        rsleep(0.1, 0.15)

def disconnect():
    print("[DISCONNECT] Exiting the match...")
    rsleep(1.0, 1.5)

    loc = match_template("surrender.png", 0.8)
    if loc:
        human_click(*loc)

    rsleep(0.5, 1.0)
    loc = match_template("disconnect.png", 0.8)
    if loc:
        human_click(*loc)

    rsleep(0.5, 1.0)
    loc = match_template("return.png", 0.8)
    if loc:
        human_click(*loc)

    rsleep(4.0, 5.0)

def go_next():
    print("[NEXT] Skipping base...")
    loc = match_template("next.png", 0.8)
    if loc:
        human_click(*loc)
        time.sleep(10)

# ------------------- Main Bot Loop -------------------

for i in range(9999):
    print(f"\n=================== 🔁 Match #{i + 1} ===================")
    maybe_idle()
    start_match()

    for j in range(9999):
        eagle_pos = find_eagle()
        if eagle_pos:
            print("🎯 Eagle Found!")
            attack(eagle_pos)
            break
        else:
            go_next()
            maybe_idle()

    disconnect()
