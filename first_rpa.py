import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1
pyautogui.alert("Vai começar, aperte OK e não mexa em nada")
pyautogui.press("winleft")
pyautogui.write("internet")
pyautogui.press("enter")

link = "http://sp.gmes.lge.com/"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(7)