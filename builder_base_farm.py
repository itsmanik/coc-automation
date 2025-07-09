from multiprocessing import Process, Value, Manager, Queue
import time
from threading import Thread
import pyautogui
import tkinter as tk

def logger_popup(log_q):
    root = tk.Tk()
    root.title("Log Console")
    root.attributes("-topmost", True)
    root.geometry("600x300+1200+20")
    root.configure(bg="black")

    text = tk.Text(root, bg="black", fg="white", font=("Consolas", 10), wrap="word")
    text.pack(expand=True, fill="both")

    def poll_queue():
        try:
            while not log_q.empty():
                msg, color = log_q.get()
                timestamp = time.strftime("%H:%M:%S")
                text.insert(tk.END, f"[{timestamp}] ", "timestamp")
                text.insert(tk.END, msg + "\n", color)
                text.see(tk.END)
        except Exception as e:
            text.insert(tk.END, f"[ERROR] Logger died: {e}\n")
        root.after(200, poll_queue)

    # Define tag styles
    # Define tag styles
    text.tag_config("green", foreground="lime", font=("Consolas", 15, "bold"))
    text.tag_config("red", foreground="red", font=("Consolas", 15, "bold"))
    text.tag_config("yellow", foreground="yellow", font=("Consolas", 15, "bold"))
    text.tag_config("blue", foreground="deepskyblue", font=("Consolas", 15, "bold"))
    text.tag_config("gray", foreground="gray", font=("Consolas", 15))
    text.tag_config("timestamp", foreground="gray", font=("Consolas", 10, "italic"))
    text.tag_config("hotpink", foreground="#FF69B4", font=("Consolas", 10))  # smaller font
    text.tag_config("orange", foreground="orange", font=("Consolas", 15, "bold"))


    poll_queue()
    root.mainloop()

def network_error_fix(network_error, log_q):
    while True:
        try:
            try_again_loc = pyautogui.locateCenterOnScreen("network-error.png", confidence=0.8) 
            log_q.put(("Network Error Detected", "timestamp"))
            pyautogui.click(689, 652)
            time.sleep(10)
        except:
            network_error.value = False
            log_q.put(("No Network Error", "gray"))
        time.sleep(1)

def start_match(network_error, log_q):
    if network_error.value == False:
        while True:
            try:
                attack_button_loc = pyautogui.locateCenterOnScreen("builder-attack-button.png", confidence=0.8)
                log_q.put(("Starting Match", "blue"))
                pyautogui.click(attack_button_loc)
                time.sleep(0.5)
                find_now_button_loc = pyautogui.locateCenterOnScreen("find-now-button.png", confidence=0.8)
                pyautogui.click(find_now_button_loc)
            except:
                pass
            time.sleep(5)
    pass

def attack(network_error, log_q):
    if network_error.value == False:
        while True:
            try:
                battle_machine_loc = pyautogui.locateCenterOnScreen("battle-machine.png", confidence=0.99)
                log_q.put(("Attack - 1", "green"))
                pyautogui.click(384, 1022)
                time.sleep(0.1)
                pyautogui.click(183, 586)
                time.sleep(10)
                pyautogui.click(384 + 125, 1022)
                time.sleep(0.1)
                pyautogui.moveTo(183, 586)
                pyautogui.mouseDown()
                time.sleep(3)
                pyautogui.mouseUp()
                slots = [1, 2, 3, 4, 5, 6]  # Exclude slot 1 (already used)
                for slot in slots:
                    x = 384 + 125 * slot
                    pyautogui.click(x, 1022)
                    time.sleep(3)
                pyautogui.click(384, 1022)
            except:
                pass
                time.sleep(5)

def second_phase_attack(network_error, log_q):
    if network_error.value == False:
        while True:
            try:
                reinforcement_loc = pyautogui.locateCenterOnScreen("reinforcement.png", confidence=0.95)
                log_q.put(("Attack - 2", "green"))
                pyautogui.click(384, 1022)
                time.sleep(0.1)
                pyautogui.click(183, 586)
                time.sleep(0.1)
                pyautogui.click(384 + 125 + 750, 1022)
                time.sleep(0.1)
                pyautogui.moveTo(183, 586)
                pyautogui.mouseDown()
                time.sleep(3)
                pyautogui.mouseUp()
                time.sleep(5)
                for i in range(7, 9):  # Slots 7 and 8
                    x = 384 + 125 * i
                    pyautogui.click(x, 1022)
                    time.sleep(3)
            except: 
                pass
            time.sleep(5)

def end_game(network_error, log_q):
    if network_error.value == False:
        while True:
            try:
                end_game_loc = pyautogui.locateCenterOnScreen("builder-return-home.png", confidence=0.8)
                log_q.put(("Ending Game", "blue"))
                pyautogui.click(end_game_loc)
            except:
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
