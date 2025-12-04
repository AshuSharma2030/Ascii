🎨 ASCII  (With Text & Background Colors)

A menu-driven Python console application that generates large ASCII art for:

✅ Single characters

✅ Words

✅ Only alphabets

✅ Only numbers

✅ Alphabet ranges


📌 Features

✅ One Character ASCII Art

✅ Word ASCII Art (Max 15 Characters)

✅ Only Alphabet Mode

✅ Only Number Mode

✅ Alphabet Range Mode (Example: A-D)

✅ Text Color Selection

✅ Background Color Selection


🧠 How the Project Works

The ASCII patterns are stored inside a data table of 5 rows

Each character is printed using a 6-column wide slice

Using ord() calculation, the program finds the correct portion of the ASCII design

Colors are applied using ANSI escape sequences

Output is displayed with both:

🎨 Text Color

🎨 Background Color

🎨 Color Support
✅ Supported Text & Background Colors

Red

Green

Yellow

Blue

Magenta

Cyan

White


User selects both colors separately from the menu.

📂 Project Files
Ascii/
├── ascii.py
└── README.md

⚙️ Installation
1️⃣ Install Python

Download from:

https://www.python.org

2️⃣ Clone the Repository
git clone https://github.com/YOUR-USERNAME/Ascii.git

3️⃣ Open Project Folder
cd Ascii

4️⃣ Run the Program
python asciiartproject.py

▶ Usage

After running the program, you will see:

******** ASCII  ********

0. Choose Text & Background Color
1. One Character
2. Words
3. Only Alphabets
4. Only Numbers
5. Alphabet Range
6. Exit


Use number keys to select any option.

🖼 Example Input & Output
Input:
A

Output:
 ***  
*   * 
***** 
*   * 
*   * 


(Displayed with selected text and background colors)

⚠ Notes

🔹 This project is Windows-specific because it uses:

msvcrt.getch()

os.system("cls")

🔹 Works best on:

✅ Windows Terminal

✅ VS Code Terminal

✅ PowerShell

🔹 Maximum Input Limit: 15 Characters

🔹 Alphabet Range must be in this format:

A-D
---
