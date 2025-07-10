from multiprocessing import Process, Value, Manager, Queue
import time
from threading import Thread
import pyautogui
import tkinter as tk

def logger_popup(log_q):
    root = tk.Tk()
    root.title("COC HACK v2.0 - [ACTIVE]")
    root.attributes("-topmost", True)
    root.geometry("600x400+1200+20")
    root.configure(bg="#0a0a0a")  # Very dark gray background
    
    # Hacker-style header frame
    header = tk.Frame(root, bg="black", height=30)
    header.pack(fill="x", padx=5, pady=5)
    
    # Creator label with glitch effect
    creator = tk.Label(header, 
                     text="> DEVELOPED BY MANIK <", 
                     fg="lime", 
                     bg="black", 
                     font=("Courier New", 12, "bold"))
    creator.pack(side="left", padx=10)
    
    # Pulsing status indicator
    status = tk.Label(header, 
                     text="SYSTEM ACTIVE ■", 
                     fg="lime", 
                     bg="black", 
                     font=("Courier New", 10, "bold"))
    status.pack(side="right", padx=10)
    
    # Main console area with matrix vibe
    text = tk.Text(root, 
                  bg="black", 
                  fg="#e0e0e0",  # Off-white text
                  insertbackground="lime",  # Bright cursor
                  selectbackground="#333333",  # Dark selection
                  font=("Consolas", 11), 
                  wrap="word",
                  relief="flat",
                  borderwidth=0,
                  padx=10,
                  pady=10)
    text.pack(expand=True, fill="both", padx=5, pady=(0,5))
    
    # Add scrollbar with custom style
    scrollbar = tk.Scrollbar(text)
    scrollbar.pack(side="right", fill="y")
    scrollbar.config(command=text.yview, troughcolor="black", bg="#333333")
    text.config(yscrollcommand=scrollbar.set)
    
    # Define tag styles - keeping your original colors but enhanced
    text.tag_config("green", foreground="lime", font=("Consolas", 12, "bold"))
    text.tag_config("red", foreground="red", font=("Consolas", 12, "bold"))
    text.tag_config("yellow", foreground="yellow", font=("Consolas", 12, "bold"))
    text.tag_config("blue", foreground="deepskyblue", font=("Consolas", 12, "bold"))
    text.tag_config("gray", foreground="gray", font=("Consolas", 11))
    text.tag_config("timestamp", foreground="#555555", font=("Consolas", 10, "italic"))
    text.tag_config("hotpink", foreground="darkgreen", font=("Consolas", 10))
    text.tag_config("orange", foreground="orange", font=("Consolas", 12, "bold"))
    
    def show_initial_messages():
        # Initial boot message with your original colors
        timestamp = time.strftime("%H:%M:%S")
        text.insert(tk.END, f"[{timestamp}] ", "timestamp")
        text.insert(tk.END, "COC AUTOMATION SYSTEM ONLINE\n", "green")
        text.insert(tk.END, f"[{timestamp}] ", "timestamp")
        text.insert(tk.END, "CREATED BY MANIK\n", "blue")
        text.insert(tk.END, "INITIALIZING BOT PROCESSES...\n\n", "yellow"),
        
        # Pause for 3 seconds before showing the next message
        root.after(10000, lambda: [
            text.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] ", "timestamp"),
            poll_queue()  # Start polling after the delay
        ])

    def poll_queue():
        try:
            while not log_q.empty():
                msg, color = log_q.get()
                timestamp = time.strftime("%H:%M:%S")
                text.insert(tk.END, f"[{timestamp}] ", "timestamp")
                text.insert(tk.END, msg + "\n", color)
                text.see(tk.END)
        except Exception as e:
            timestamp = time.strftime("%H:%M:%S")
            text.insert(tk.END, f"[{timestamp}] ", "timestamp")
            text.insert(tk.END, f"ERROR: {str(e)[:50]}...\n", "red")
        root.after(200, poll_queue)
    
    # Pulsing border effect
    def pulse_border():
        for i in range(1, 4):
            root.after(i*100, lambda: root.configure(highlightbackground="lime", highlightthickness=1))
        root.after(400, lambda: root.configure(highlightthickness=0))
        root.after(5000, pulse_border)
    
    pulse_border()
    show_initial_messages()  # Start with the initial messages
    root.mainloop()

def network_error_fix(network_error, log_q):
    while True:
        try:
            try_again_loc = pyautogui.locateCenterOnScreen("network-error.png", confidence=0.8) 
            log_q.put(("‼️Network Error Detected", "red"))
            log_q.put(("Attempting to click 'Try Again' button at coordinates (689, 652)", "hotpink"))
            pyautogui.moveTo(675, 652)
            pyautogui.click()
            time.sleep(0.1)
            pyautogui.moveTo(678, 652)
            pyautogui.click()
            time.sleep(0.1)
            pyautogui.moveTo(683, 652)
            pyautogui.click()
            time.sleep(0.1)
            pyautogui.moveTo(700, 650)
            pyautogui.click()
            log_q.put(("Clicked 'Try Again', waiting 10 seconds for reconnection", "hotpink"))
            time.sleep(10)
        except:
            network_error.value = False
        log_q.put(("Network status check completed successfully", "timestamp"))
        time.sleep(2)

def start_match(network_error, log_q):
    if network_error.value == False:
        while True:
            try:
                attack_button_loc = pyautogui.locateCenterOnScreen("builder-attack-button.png", confidence=0.8)
                log_q.put(("⚔️Starting Match", "blue"))
                log_q.put(("Found attack button at coordinates: {}".format(attack_button_loc), "hotpink"))
                pyautogui.click(attack_button_loc)
                time.sleep(0.5)
                find_now_button_loc = pyautogui.locateCenterOnScreen("find-now-button.png", confidence=0.8)
                log_q.put(("Found 'Find Now' button at coordinates: {}".format(find_now_button_loc), "hotpink"))
                pyautogui.click(find_now_button_loc)
                log_q.put(("Matchmaking initiated, waiting for opponent", "hotpink"))
            except:
                log_q.put(("Attack button or Find Now button not found, retrying in 5 seconds", "hotpink"))
                pass
            time.sleep(5)

def attack(network_error, log_q):
    if network_error.value == False:
        while True:
            try:
                battle_machine_loc = pyautogui.locateCenterOnScreen("battle-machine.png", confidence=0.99)
                log_q.put(("🗡️Attack - 1", "green"))
                log_q.put(("Battle machine detected, starting first phase attack", "hotpink"))
                pyautogui.click(384, 1022)
                log_q.put(("Clicked troop slot 1 at (384, 1022)", "hotpink"))
                time.sleep(0.1)
                pyautogui.click(183, 586)
                log_q.put(("Deployed troop at (183, 586)", "hotpink"))
                time.sleep(10)
                pyautogui.click(384 + 125, 1022)
                log_q.put(("Clicked troop slot 2 at ({}, 1022)".format(384 + 125), "hotpink"))
                time.sleep(0.1)
                pyautogui.moveTo(183, 586)
                pyautogui.mouseDown()
                time.sleep(3)
                pyautogui.mouseUp()
                log_q.put(("Held and released mouse for 3 seconds at (183, 586)", "hotpink"))
                slots = [1, 2, 3, 4, 5, 6]  # Exclude slot 1 (already used)
                for slot in slots:
                    x = 384 + 125 * slot
                    pyautogui.click(x, 1022)
                    log_q.put(("Clicked troop slot {} at ({}, 1022)".format(slot + 1, x), "hotpink"))
                    time.sleep(3)
                pyautogui.click(384, 1022)
                log_q.put(("First phase attack completed, returning to slot 1", "hotpink"))
            except:
                log_q.put(("Attack phase 1 elements not found, retrying in 5 seconds", "hotpink"))
                pass
                time.sleep(5)

def second_phase_attack(network_error, log_q):
    if network_error.value == False:
        while True:
            try:
                reinforcement_loc = pyautogui.locateCenterOnScreen("reinforcement.png", confidence=0.95)
                log_q.put(("🗡️🗡️Attack - 2", "green"))
                log_q.put(("Reinforcement detected, starting second phase attack", "hotpink"))
                pyautogui.click(384, 1022)
                log_q.put(("Clicked troop slot 1 at (384, 1022)", "hotpink"))
                time.sleep(0.1)
                pyautogui.click(183, 586)
                log_q.put(("Deployed troop at (183, 586)", "hotpink"))
                time.sleep(0.1)
                pyautogui.click(384 + 125 + 750, 1022)
                log_q.put(("Clicked troop slot 8 at ({}, 1022)".format(384 + 125 + 750), "hotpink"))
                time.sleep(0.1)
                pyautogui.moveTo(183, 586)
                pyautogui.mouseDown()
                time.sleep(3)
                pyautogui.mouseUp()
                log_q.put(("Held and released mouse for 3 seconds at (183, 586)", "hotpink"))
                time.sleep(5)
                for i in range(7, 9):  # Slots 7 and 8
                    x = 384 + 125 * i
                    pyautogui.click(x, 1022)
                    log_q.put(("Clicked troop slot {} at ({}, 1022)".format(i + 1, x), "hotpink"))
                    time.sleep(3)
                log_q.put(("Second phase attack completed", "hotpink"))
            except: 
                log_q.put(("Attack phase 2 elements not found, retrying in 5 seconds", "hotpink"))
                pass
            time.sleep(5)

def end_game(network_error, log_q):
    if network_error.value == False:
        while True:
            try:
                end_game_loc = pyautogui.locateCenterOnScreen("builder-return-home.png", confidence=0.8)
                log_q.put(("🔚Ending Game", "blue"))
                log_q.put(("Found return home button at coordinates: {}".format(end_game_loc), "hotpink"))
                pyautogui.click(end_game_loc)
                log_q.put(("Clicked return home button, waiting for base to load", "hotpink"))
            except:
                log_q.put(("Return home button not found, retrying in 5 seconds", "hotpink"))
                pass
            time.sleep(5)

if __name__ == "__main__":
    manager = Manager()
    log_q = Queue()
    Thread(target=logger_popup, args=(log_q,), daemon=True).start()
    network_error = Value('b', False)
    network_error_fix_process = Process(target=network_error_fix, args=(network_error,log_q,))
    start_match_process = Process(target=start_match, args=(network_error,log_q,))
    attack_process = Process(target=attack, args=(network_error,log_q,))
    second_phase_attack_process = Process(target=second_phase_attack, args=(network_error,log_q,))
    end_game_process = Process(target=end_game, args=(network_error,log_q,))

    network_error_fix_process.start()
    start_match_process.start()
    attack_process.start()
    second_phase_attack_process.start()
    end_game_process.start()