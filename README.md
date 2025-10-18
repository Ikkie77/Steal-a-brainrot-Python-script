# Brainrot Detector 🤖 Setup Guide

This guide details all necessary software and steps to get the Brainrot Detector script running on your Windows PC.

## 1. Prerequisites (What You Need)

To run the script, you must have the following software installed and configured on your **Windows PC**:

### A. Python Environment

* **Python:** The script requires Python 3.x.
* **External Libraries:** You must install the following packages using pip via your Command Prompt or PowerShell:
    
    pip install pytesseract pillow keyboard pygetwindow
    

### B. Tesseract OCR

The script relies on **Tesseract** to read text from the game screen.

* **Tesseract Installer:** Download and install the Tesseract OCR software on your PC.
* **Configuration:** You **must** confirm and update the Tesseract path inside the Python script to match the exact location of your `tesseract.exe` file. (The default path is set to `C:\Program Files\Tesseract-OCR\tesseract.exe`).

### C. Game Window

* **Roblox Window Title:** The script uses the title **"Roblox"** to automatically focus the game window. Ensure the Roblox game window is titled exactly that for the automation to work correctly.

---

## 2. Configuration Steps (Mandatory Changes)

Before running the Python file, make sure you configure the following three lines inside the script to match your setup:

1.  **`TARGET_NAMES`:** 📝
    * Set the list of names you want the script to look for.

    TARGET_NAMES = ["Crabracadabra", "Fruttodrillo", "Secret", "M/s", "Cocofanto", "Girafa"] 
    

2.  **`pytesseract.pytesseract.tesseract_cmd`:** 🛠️
    * Set the correct path to your Tesseract installation.

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
    

3.  **`SCREEN_REGION`:** 🖼️
    * Verify and adjust the coordinates `(left, top, right, bottom)` to perfectly frame the area on your screen where the names appear. **This is crucial for OCR accuracy.**

    SCREEN_REGION = (704, 129, 1075, 375)
    

---

## 3. How to Run the Script

1.  Save the Python code (e.g., as `detector.py`). The folder you save your Python file will also contain the logfile.
2.  Open your **Command Prompt** (CMD) or **PowerShell** window.
3.  Navigate to the directory where your Python script is saved.
4.  Execute the script:
    
    python detector.py
    
5.  The script will first **focus the Roblox window** and send the target names to the chat. It will then begin the continuous scan loop (presses 'Tab' briefly every 1.5s to keep the game active).
6.  When a target name is detected, it automatically focuses the window, presses 'E' twice, takes success screenshots, and pauses.
7.  To stop the program, return to the Command Prompt and press **Ctrl + C** or Hardclose it.
