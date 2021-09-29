#Ainda testando o envio para o Git
import pyautogui
import time


# time.sleep(2)
# print(pyautogui.position())
# time.sleep(10)


# Alterna abas antes de começar o código
pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')

for i in range(16):
    # 1 segundos de espera para começar o código
    #time.sleep(1)
    pyautogui.press('tab')


def presencial():
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space')


def remoto():
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('right')


def grupo_a_presencial():
    presencial()
    presencial()
    presencial()
    presencial()
    remoto()
    presencial()
    presencial()
    presencial()
    presencial()
    remoto()
    remoto()
    remoto()
    presencial()
    remoto()
    remoto()
    remoto()
    remoto()
    remoto()
    remoto()
    remoto()
    remoto()
    presencial()
    remoto()
    remoto()
    remoto()
    remoto()
    presencial()
    remoto()
    remoto()
    remoto()
    presencial()
    remoto()
    remoto()
    remoto()



def grupo_b_presencial():
    remoto()
    remoto()
    remoto()
    remoto()
    remoto()
    remoto()
    remoto()
    remoto()
    remoto()
    remoto()
    presencial()
    presencial()
    remoto()
    presencial()
    presencial()
    presencial()
    remoto()
    presencial()
    remoto()
    presencial()
    remoto()
    remoto()
    presencial()
    presencial()
    presencial()
    remoto()
    presencial()
    presencial()
    remoto()
    remoto()
    remoto()
    presencial()
    remoto()
    presencial()


grupo_b_presencial()