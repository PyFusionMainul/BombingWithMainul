import pyautogui
import time
time.sleep(2)

count = 0;
while count<=1000:
    pyautogui.typewrite("Hello World!"+str(count))
    pyautogui.press("enter")
    count=count+1
