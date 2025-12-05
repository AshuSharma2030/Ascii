import os
import msvcrt as msv

# ---------------- COLORS ----------------
TEXT_COLORS = {
    "0": "\033[0m",    # Reset
    "1": "\033[31m",   # Red
    "2": "\033[32m",   # Green
    "3": "\033[33m",   # Yellow
    "4": "\033[34m",   # Blue
    "5": "\033[35m",   # Magenta
    "6": "\033[36m",   # Cyan
    "7": "\033[37m",   # White
}

BG_COLORS = {
    "0": "\033[0m",
    "1": "\033[41m",
    "2": "\033[42m",
    "3": "\033[43m",
    "4": "\033[44m",
    "5": "\033[45m",
    "6": "\033[46m",
    "7": "\033[47m",
}

text_color = TEXT_COLORS["0"]
bg_color = BG_COLORS["0"]

# ---------------- ASCII DATA ----------------
data = [
" ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***  ****   **** ***** *   * *   * *   * *   * *   * ***** ",
"*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     * ",
"*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   * ****  *****   *   *   * *   * * * *   *     *     * ",
"***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   * *  *      *   *   *   *  * *  ** **  * *    *    * ",
"*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      ***  *   * ****    *   *****   *   *   * *   *   *   ***** "
]

# ---------------- FUNCTIONS ----------------

def chooseColorsStart():
    """ Ask color at program start """
    global text_color, bg_color
    os.system("cls")
    print("Choose TEXT Color:")
    print("1.Red 2.Green 3.Yellow 4.Blue 5.Magenta 6.Cyan 7.White")
    t = input("Enter Text Color Number: ")
    text_color = TEXT_COLORS.get(t, "\033[0m")

    print("\nChoose BACKGROUND Color:")
    print("1.Red 2.Green 3.Yellow 4.Blue 5.Magenta 6.Cyan 7.White 0.No Color")
    b = input("Enter Background Color Number: ")
    bg_color = BG_COLORS.get(b, "\033[0m")


def printAscii(text):
    for row in data:
        for ch in text:
            n = ((ord(ch.upper()) - 64) - 1) * 6
            print(text_color + bg_color + row[n:n+6] + "\033[0m", end="")
        print()


def oneCharacter():
    os.system("cls")
    ch = input("Enter One Character: ")
    printAscii(ch)


def words():
    os.system("cls")
    text = input("Enter Word (Max 15): ")
    printAscii(text)


def onlyAlpha():
    os.system("cls")
    text = input("Only Alphabets: ")
    if text.isalpha():
        printAscii(text)
    else:
        onlyAlpha()


def onlyNum():
    os.system("cls")
    text = input("Only Numbers: ")
    if text.isnumeric():
        printAscii(text)
    else:
        onlyNum()


def smallLetters():
    os.system("cls")
    text = input("Enter Small Letters (a-z): ")
    if text.isalpha():
        printAscii(text.lower())
    else:
        smallLetters()


def alphaRange():
    os.system("cls")

    while True:
        r = input("Enter Range (Example: A-D): ").upper()

        # ❌ Only single alphabet or incorrect format
        if len(r) != 3 or r[1] != "-" or not r[0].isalpha() or not r[2].isalpha():
            print("\nInvalid input! Please enter a valid range like A-D.\n")
            continue

        start = ord(r[0]) - 64
        end = ord(r[2]) - 64

        # ❌ Wrong order (ex: D-A)
        if start > end:
            print("\nInvalid Range! Starting letter must be smaller. Example: A-D\n")
            continue

        # ✔ Correct input → print ASCII
        for row in data:
            for i in range(start, end + 1):
                n = (i - 1) * 6
                print(text_color + bg_color + row[n:n+6] + "\033[0m", end="")
            print()

        break


# ---------------- MAIN MENU ----------------

def mainUI():
    os.system("cls")
    print("\n******** ASCII ********\n")
    print("0. Change Text & Background Color")
    print("1. One Character")
    print("2. Words")
    print("3. Only Alphabets")
    print("4. Only Numbers")
    print("5. Alphabet Range")
    print("6. Small Letters (a-z)")
    print("7. Exit")

    print("\nEnter Choice: ", end="")
    ch = msv.getch().decode()

    if ch == "0":
        chooseColorsStart()
    elif ch == "1":
        oneCharacter()
    elif ch == "2":
        words()
    elif ch == "3":
        onlyAlpha()
    elif ch == "4":
        onlyNum()
    elif ch == "5":
        alphaRange()
    elif ch == "6":
        smallLetters()
    elif ch == "7":
        exit()

    print("\n\nPress Y To Continue...")
    if msv.getch().decode().lower() == "y":
        mainUI()


# ---------- Program Starts ----------
chooseColorsStart()
mainUI()
