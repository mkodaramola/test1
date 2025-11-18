import pyautogui
import time

# Number of times to scroll
scroll_count = 50  

#abcdefghijk

for i in range(scroll_count):
    pyautogui.scroll(-400)  # Negative value scrolls down
    time.sleep(30)           # Wait 2 seconds before next scroll 1234
