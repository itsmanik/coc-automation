import pyautogui
import threading
import time
import random

# ------------------- Human-like Behavior Helpers -------------------

def rand_sleep(a, b):
    """Sleep for a random time between a and b seconds."""
    time.sleep(random.uniform(a, b))

def human_click(x, y, move=True):
    """Move to (x, y) with slight randomness and click."""
    rand_x = x + random.randint(-5, 5)
    rand_y = y + random.randint(-5, 5)
    duration = random.uniform(0.05, 0.25) if move else 0
    pyautogui.moveTo(rand_x, rand_y, duration=duration)
    pyautogui.click()

def maybe_idle(chance=0.1):
    """Randomly idle for 3-6 sec with a given chance."""
    if random.random() < chance:
        pause_time = random.uniform(3, 6)
        print(f"[Idle] Human-like pause for {pause_time:.2f}s...")
        time.sleep(pause_time)

# ------------------- Match Logic -------------------

def start_match():
    print("[MATCH] Starting...")
    loc = pyautogui.locateCenterOnScreen("builder-attack-button.png", confidence=0.8)
    if loc:
        human_click(*loc)
        rand_sleep(0.3, 0.6)

    loc = pyautogui.locateCenterOnScreen("find-now-button.png", confidence=0.8)
    if loc:
        human_click(*loc)
        rand_sleep(0.3, 0.6)

# ------------------- Reinforcement Logic -------------------

def start_attack2():
    print("[REINFORCEMENT] Triggered!")
    human_click(384, 1022)
    rand_sleep(0.1, 0.3)

    human_click(183, 586)
    rand_sleep(0.1, 0.3)

    human_click(384 + 125 + 750, 1022)
    rand_sleep(0.1, 0.3)

    pyautogui.moveTo(183 + random.randint(-10, 10), 586 + random.randint(-10, 10), duration=random.uniform(0.1, 0.3))
    pyautogui.mouseDown()
    rand_sleep(2.5, 3.5)
    pyautogui.mouseUp()

    rand_sleep(9, 11)

    # Drop reinforcement troops/spells
    for i in range(7, 9):  # Slots 7 and 8
        x = 384 + 125 * i
        human_click(x, 1022)
        rand_sleep(0.2, 0.4)

def reinforcement_watcher():
    while True:
        try:
            reinforcement_location = pyautogui.locateCenterOnScreen("reinforcement.png", confidence=0.95)
            if reinforcement_location:
                start_attack2()
        except:
            pass
        rand_sleep(0.5, 1.0)

# ------------------- Main Attack Logic -------------------

def attack():
    print("[ATTACK] Executing main attack...")
    human_click(384, 1022)
    rand_sleep(0.1, 0.3)

    human_click(183, 586)
    rand_sleep(0.1, 0.3)

    human_click(384 + 125, 1022)
    rand_sleep(0.1, 0.3)

    pyautogui.moveTo(183 + random.randint(-10, 10), 586 + random.randint(-10, 10), duration=random.uniform(0.1, 0.25))
    pyautogui.mouseDown()
    rand_sleep(2.5, 3.5)
    pyautogui.mouseUp()

    rand_sleep(9, 11)   

    # Drop spell bar items in randomized order
    slots = [2, 3, 4, 5, 6]  # Exclude slot 1 (already used)
    random.shuffle(slots)
    for slot in slots:
        x = 384 + 125 * slot
        human_click(x, 1022)
        rand_sleep(0.2, 0.4)

# ------------------- Main Bot Loop -------------------

def main_loop():
    while True:
        maybe_idle(0.2)
        start_match()
        rand_sleep(4, 6)
        attack()

        print("[WAIT] Watching for return-home button...")
        while True:
            maybe_idle(0.1)
            try:
                end_game_location = pyautogui.locateCenterOnScreen("builder-return-home.png", confidence=0.8)
                if end_game_location:
                    print("[MATCH END] Returning home.")
                    human_click(*end_game_location)
                    rand_sleep(4.5, 5.5)
                    break
            except:
                pass
            time.sleep(1)

# ------------------- Entry Point -------------------

if __name__ == "__main__":
    print("[BOT] Starting in 3 seconds... Switch to game window.")
    time.sleep(3)

    # Start reinforcement detection thread
    reinforce_thread = threading.Thread(target=reinforcement_watcher, daemon=True)
    reinforce_thread.start()

    # Run the bot loop
    main_loop()
