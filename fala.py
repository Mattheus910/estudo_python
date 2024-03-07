import pyttsx3

engine = pyttsx3.init()
engine.say('Qual o seu nome? ')
engine.runAndWait()

nome = str(input('Qual o seu nome? '))

engine.say(f'Olá {nome}, tudo bem ?')
engine.runAndWait()






