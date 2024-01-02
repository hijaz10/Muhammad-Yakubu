import pyautogui as spam
import time

msg = input("Message you want to send: ")
num_times = int(input("Enter the number of times to send the message: "))

time.sleep(5)

for i in range(num_times):
    spam.typewrite(msg) 
    time.sleep(1)             
    spam.press("Enter")
    time.sleep(1)
