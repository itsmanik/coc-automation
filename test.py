import pyautogui
import time

print("Move your mouse to the 'Try Again' button. Press Ctrl+C to stop.\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Mouse Position: X={x} Y={y}     ", end='\r')  # Overwrites the same line
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nTracking stopped.")
