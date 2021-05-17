import pyautogui
import time

pyautogui.PAUSE = 1
time.sleep(5)

pyautogui.alert("Irei configurar o cooler para vc, não clique em nada")

# abrir speedfan
pyautogui.press("winleft")
pyautogui.write("speedfan")
pyautogui.press("enter")
time.sleep(15)

# chegar no campo e colocar o valor
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.write("65")
pyautogui.press("tab")
pyautogui.write("80")
pyautogui.press("tab")
pyautogui.write("75")
pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.alert(f"Cooler configurado, já pode utilizar o PC")
