import pyautogui
import time
import keyboard
import sys

# Seznam pozic pro klikání – přidej nebo odeber dle potřeby
positions = [
    (500, 500),
    (500, 600),
    (300, 700),
]

# Interval mezi kliky (v sekundách)
interval = 5.0

running = False

def start():
    global running
    if not running:
        running = True
        print("Klikač spuštěn...")

def stop():
    global running
    if running:
        running = False
        print("Klikač zastaven.")
        sys.exit()  # Ukončí celý program

# Registrace klávesových zkratek
keyboard.add_hotkey('s', start)
keyboard.add_hotkey('d', stop)

print("Stiskni s pro start a d pro stop.")
print(f"Načteno {len(positions)} pozic: {positions}")

try:
    while True:
        if running:
            for x, y in positions:
                if not running:
                    break
                pyautogui.click(x, y)
                print(f"Klik na pozici ({x}, {y})")

                # Čekání s možností přerušení
                slept = 0.0
                step = 0.01
                while slept < interval:
                    time.sleep(step)
                    slept += step
                    if not running:
                        break
        else:
            time.sleep(0.1)
except KeyboardInterrupt:
    print("Ukončeno uživatelem.")

# musíš pak killnout terminál ručně (košem)