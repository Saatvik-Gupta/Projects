import os

print("Initialising Robo Speaker Version 1.11")

while True:

    text = input("Tell me what to speak: ")

    if text.lower() == "exit":
        break

    command = f'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
              f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'

    os.system(command)