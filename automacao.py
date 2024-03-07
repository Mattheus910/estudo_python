import pyautogui
import pyperclip
from time import sleep

def moveAndClick(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    sleep(2)

def texto(texto):
    pyperclip.copy(texto)
    pyautogui.hotkey("ctrl", "v")

pyautogui.press('win')
sleep(1)
pyautogui.write('chrome')
sleep(1)
pyautogui.press('enter')

sleep(1)

pyautogui.write('https://www.linkedin.com')

pyautogui.press('enter')

sleep(3)

moveAndClick(615, 110)

moveAndClick(615, 200)

texto('''Esta publicação foi feita utilizando automação com Python!!!

Recentemente, tenho estudado Python, e estou cada vez mais fascinado com as possibilidades que essa linguagem nos oferece. Hoje, mergulhei no estudo da automação e utilizei:

PyAutoGUI: Para controlar o mouse, realizar cliques e simular digitações automáticas.
Pyperclip: Para copiar o texto, especialmente aqueles com caracteres especiais, facilitando a manipulação de dados.
Time Sleep: Para incluir pausas entre as ações, garantindo a sincronização adequada das operações automatizadas.
É incrível como podemos transformar nossas ideias em código de forma tão simples e eficaz!'''
)

sleep(1)

moveAndClick(1000, 675)






