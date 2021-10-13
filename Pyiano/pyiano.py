from playsound import playsound
import keyboard

print("\nWelcome to Pyiano - A piano built with python\n")
print("Press a key out of these ['s', 'd', 'f', 'g', 'h', 'j', 'k']\n")

while True: 
    if keyboard.is_pressed('s'):
        playsound("sounds/do.wav", False)
    if keyboard.is_pressed('d'):
        playsound("sounds/re.wav", False)
    if keyboard.is_pressed('f'):
        playsound("sounds/mi.wav", False)
    if keyboard.is_pressed('g'):
        playsound("sounds/fa.wav", False)
    if keyboard.is_pressed('h'):
        playsound("sounds/sol.wav", False)
    if keyboard.is_pressed('j'):
        playsound("sounds/la.wav", False)
    if keyboard.is_pressed('k'):
        playsound("sounds/si.wav", False)
    
