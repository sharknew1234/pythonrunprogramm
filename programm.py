import pyautogui
from time import sleep

pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True

print(pyautogui.position())

while 1<5:
    proggram = str(input('Введите имя программы:'))

    pyautogui.hotkey('ctrl', 'esc')

    pyautogui.typewrite(proggram, interval=0.1)
    pyautogui.press('enter')