import itertools
import os
import time
import sys

# ================= BANNER ================= #

def banner():
    print("\033[1;32m")
    print(" ██████╗██╗   ██╗██████╗ ███████╗██████╗ ██╗  ██╗")
    print("██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝")
    print("██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝ ╚███╔╝ ")
    print("██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗ ██╔██╗ ")
    print("╚██████╗   ██║   ██████╔╝███████╗██║  ██║██╔╝ ██╗")
    print(" ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝")
    print("           CYBERX TOOLKIT")
    print("\033[0m")

banner()
print("OWNER CYBER X TEAM")
print("==== BY CYBER X ULTRA PRO WORDLIST GENERATOR ====\n")

# ================= INPUT ================= #
print("Enter Target Detials")
name = input("Name: ")
surname = input("Surname: ")
nickname = input("Nickname: ")
birth = input("Birth Year: ")
partner = input("Partner Name: ")
phone = input("Phone Number: ")
pet = input("Pet Name: ")
fav = input("Favorite Word: ")

# ================= WORD BUILD ================= #

words = [name, surname, nickname, partner, pet, fav]
words = [w.lower() for w in words if w]

# fallback words
if len(words) < 5:
    words.extend(["india","password","admin","user","king","queen","love"])

# variations
extra = []
for w in words:
    extra += [
        w+"123", w+"786", w+"007",
        w[::-1], w.capitalize()
    ]

words.extend(extra)
words = list(set(words))

# numbers
numbers = ["123","1234","111","000","007","786","999"]
if phone:
    numbers += [phone[-4:], phone[:4]]

# symbols
symbols = ["@", "#", "$", "_", ".", "!"]

# ================= SAFE LIMIT ================= #

while True:
    user_input = input("\nMax passwords (Enter = 500000): ").strip()
    if user_input == "":
        limit = 999999999
        break
    if user_input.isdigit():
        limit = int(user_input)
        break
    else:
        print("Invalid input!")

# ================= FILE ================= #

os.makedirs("wordlists", exist_ok=True)
file_path = f"wordlists/cyberx_{int(time.time())}.txt"

# ================= PROGRESS BAR ================= #

def progress(count, total):
    percent = int((count / total) * 100)
    bar_length = 50
    filled = int(bar_length * count // total)
    bar = "#" * filled + "-" * (bar_length - filled)

    sys.stdout.write(f"\r\033[1;32m[{bar}]\033[0m {percent}% | {count}/{total}")
    sys.stdout.flush()

# ================= GENERATION ================= #

print("\nGenerating... ⚡")

count = 0

with open(file_path, "w") as f:

    # 1️⃣ word + number
    for w in words:
        for n in numbers:
            pw = w + n
            f.write(pw + "\n")
            count += 1

            if count % 1000 == 0:
                progress(count, limit)

            if count >= limit:
                break
        if count >= limit:
            break

    # 2️⃣ word + symbol
    for w in words:
        for s in symbols:
            pw = w + s
            f.write(pw + "\n")
            count += 1

            if count % 1000 == 0:
                progress(count, limit)

            if count >= limit:
                break
        if count >= limit:
            break

    # 3️⃣ 2-word combos
    for combo in itertools.product(words, repeat=2):
        pw = combo[0] + combo[1]
        f.write(pw + "\n")
        count += 1

        if count % 1000 == 0:
            progress(count, limit)

        if count >= limit:
            break

    # 4️⃣ 3-word combos (ULTRA)
    for combo in itertools.product(words, repeat=3):
        pw = combo[0] + combo[1] + combo[2]
        f.write(pw + "\n")
        count += 1

        if count % 1000 == 0:
            progress(count, limit)

        if count >= limit:
            break

print("\n\n✅ DONE!")
print(f"📁 Saved: {file_path}")
print(f"🔥 Total passwords: {count}")
