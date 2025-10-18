import time
import pytesseract
from PIL import ImageGrab 
import keyboard
import os
from datetime import datetime 
import sys
# NEW IMPORT: Needed to focus the Roblox window
import pygetwindow as gw 

# === CONFIGURATION - ADJUST THESE 5 LINES! ===

# 1. THE NAMES YOU ARE SEARCHING FOR 
    # All Brainrots needed per rebirth:
        # Rebirth 01: Trippi Troppi, Gangster Footera
        # Rebirth 02: Brr Brr Patapim, Boneca Ambalabu
        # Rebirth 03: Trulimero Trulicina, Chimpanzini Bananini
        # Rebirth 04: Chef-Crabracadabra, Glorbo Fruttodrillo
        # Rebirth 05: Frigo Camelo, Orangutini Ananassini
        # Rebirth 06: Bombardiro Crocodilo
        # Rebirth 07: Bombombini Gusini
        # Rebirth 08: Te Te Te Sahur
        # Rebirth 09: Cocofanto Elefanto
        # Rebirth 10: Girafa Celestre
        # Rebirth 11: Tralalero Tralala
        # Rebirth 12: Odin Din Din Dun
        # Rebirth 13: Trenostruzzo Turbo 3000
        # Rebirth 14: Trippi Troppi Troppa Trippa
        # Rebirth 15: Pakrahmatmamat
        # Rebirth 16: Los Tralaleritos

TARGET_NAMES = ["Trippi Troppi", "Gangster Footera", "Secret", "M/s", "Odin Din", "Cocofanto", "Girafa"] # Brainrots to find

# 2. The location of Tesseract OCR on your PC (must be correct!)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 3. Location for saving files (Relative: [ScriptLocation]/Logs_Screenshots)
SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
STORAGE_FOLDER = os.path.join(SCRIPT_DIR, "Logs_Screenshots") # automated to the same location as the PY file

# 4. Name of the log file in the storage folder (ENABLED)
LOG_FILE = os.path.join(STORAGE_FOLDER, "Brainrot.log") # Name of the logfile (Bainrot.log = standard)

# 5. Screen coordinates for the scan (Keep the new region)
SCREEN_REGION = (704, 29, 1175, 375) # Pinpoint the region to the black part where brainrots appear

# === FUNCTIONS ===

def get_timestamp():
    """Gets the current time in HH:MM:SS format."""
    return datetime.now().strftime("%H:%M:%S")

def log_action(action):
    """Adds the current date, time, and the action to the log file."""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] {action}\n"
        with open(LOG_FILE, "a") as f:
            f.write(log_line)
    except Exception as e:
        # If the logging function fails, we only show the error on the console.
        print(f"[{get_timestamp()}] FATAL LOGGING ERROR: Cannot write to {LOG_FILE}. Error: {e}")

def press_e_for(duration_seconds):
    """Presses the 'E' key for the specified duration and logs it."""
    print(f"[{get_timestamp()}] ACTION: Pressing 'E' for {duration_seconds} seconds...")
    log_action(f"ACTION: Starting 'E' press for {duration_seconds}s.")
    keyboard.press('e')
    time.sleep(duration_seconds)
    keyboard.release('e')
    print(f"[{get_timestamp()}] Key 'E' released.")
    log_action("ACTION: Key 'E' released.")

def press_key_briefly(key, duration_seconds=0.1):
    """Presses any key briefly."""
    # This function does NOT log, to keep the log silent during the scan.
    print(f"[{get_timestamp()}] ACTION: Briefly pressing key '{key.upper()}'.")
    keyboard.press(key)
    time.sleep(duration_seconds)
    keyboard.release(key)

def activate_roblox_window():
    """Finds the Roblox window and brings it to the foreground."""
    try:
        # Search for windows whose title contains 'Roblox'
        roblox_windows = gw.getWindowsWithTitle('Roblox')
        if roblox_windows:
            roblox_window = roblox_windows[0]
            if not roblox_window.isActive:
                roblox_window.activate() # Brings the window to the front
                print(f"[{get_timestamp()}] WINDOW: 'Roblox' window activated.")
                log_action("WINDOW: 'Roblox' window activated for chat input.")
            else:
                print(f"[{get_timestamp()}] WINDOW: 'Roblox' window was already active.")
            time.sleep(0.5) # Give Windows time to change focus
            return True
        else:
            print(f"[{get_timestamp()}] FATAL ERROR: No window found with 'Roblox' in the title.")
            log_action("FATAL ERROR: Could not find 'Roblox' window for chat input.")
            return False
    except Exception as e:
        print(f"[{get_timestamp()}] FATAL ERROR DURING WINDOW FOCUS: {e}")
        log_action(f"FATAL ERROR DURING WINDOW FOCUS: {e}")
        return False

def execute_startup_chat(name_list):
    """Opens the chat with '/', types all searched names (separated by commas) and presses Enter."""
    names_string = ", ".join(name_list)
    
    # First, activate the window
    if not activate_roblox_window():
        return # Stop if the window cannot be activated

    print(f"[{get_timestamp()}] STARTUP ACTION: Entering the search names ({names_string}) into the Roblox chat...")
    log_action(f"STARTUP ACTION: Chat opened and search names ({names_string}) entered.")
    
    # 1. Open chat (/)
    keyboard.press('/')
    keyboard.release('/')
    time.sleep(0.1) 

    # 2. Type the names
    keyboard.write(names_string)
    time.sleep(1.0) # Longer pause for typing certainty
    
    # 3. Press Enter
    keyboard.press('enter')
    keyboard.release('enter')
    time.sleep(0.5) 
    
    print(f"[{get_timestamp()}] STARTUP ACTION: Chat message sent.")


# === INITIALIZATION ===

# Ensure that the relative storage folder is guaranteed to exist here.
try:
    os.makedirs(STORAGE_FOLDER, exist_ok=True)
except Exception as e:
    print(f"[{get_timestamp()}] FATAL STARTUP ERROR: Could not create the storage folder '{STORAGE_FOLDER}'. Check permissions. Error: {e}")
    exit() 

log_action("PROGRAM START: Brainrot Detector started.")

# *** CHAT ACTION EXECUTED ONCE HERE (Includes Window Focus) ***
execute_startup_chat(TARGET_NAMES) 

# Print the startup information
print("--- Brainrot Detector Started ---")
print(f"[{get_timestamp()}] Searching for: {TARGET_NAMES}")
print(f"[{get_timestamp()}] Screenshots & Log in folder: {STORAGE_FOLDER}")
print(f"[{get_timestamp()}] Scan frequency: 1.5 seconds per cycle.")
print(f"[{get_timestamp()}] Press Ctrl+C in the Command Prompt to stop.")
print("NOTE: Logbook ONLY records program start, successes, and errors.")

# === MAIN PROGRAM LOOP ===

while True:
    start_time = time.time()
    found_name = None
    
    try:
        # 1. Take screenshot (this always happens)
        img = ImageGrab.grab(bbox=SCREEN_REGION)
        
        # 2. Perform OCR
        text_recognized = pytesseract.image_to_string(img, config='--psm 6').strip()
        text_lower = text_recognized.lower()
        
        # 3. Check if one of the target names is found
        for name in TARGET_NAMES:
            if name.lower() in text_lower:
                found_name = name
                break # Stop at the first name we find
            
        if found_name:
            
            print(f"\n[{get_timestamp()}] =================================")
            print(f"[{get_timestamp()}] !!! TARGET FOUND: {found_name} !!!")
            
            # --- LOGGING & SCREENSHOT BEFORE ACTION (SUCCESS) ---
            log_action(f"SUCCESS: Target '{found_name}' FOUND. Recognized text: {text_recognized.replace('\n', ' ')}")
            
            # Save screenshot BEFORE the action (FOUND_BEFORE prefix)
            filename_clean = found_name.replace(' ', '_') 
            screenshot_name_before = datetime.now().strftime(f"FOUND_BEFORE_{filename_clean}_%Y%m%d_%H%M%S.png")
            path_full_before = os.path.join(STORAGE_FOLDER, screenshot_name_before)
            
            img.save(path_full_before)
            print(f"[{get_timestamp()}] FILE: BEFORE-action screenshot saved as {screenshot_name_before}.")
            log_action(f"FILE: BEFORE-action screenshot saved as {screenshot_name_before}.")
            
            # --- ORIGINAL E-ACTION ---
            # Ensure the Roblox window is focused BEFORE the E-action!
            activate_roblox_window()
            press_e_for(1.2) 
            press_e_for(2) 
            
            # Pause briefly (0.1s)
            time.sleep(0.1) 
            
            # --- LOGGING & SCREENSHOT AFTER ACTION ---
            
            # Take a new screenshot AFTER the action
            img_after = ImageGrab.grab(bbox=SCREEN_REGION)
            screenshot_name_after = datetime.now().strftime(f"FOUND_AFTER_{filename_clean}_%Y%m%d_%H%M%S.png")
            path_full_after = os.path.join(STORAGE_FOLDER, screenshot_name_after)
            
            img_after.save(path_full_after)
            print(f"[{get_timestamp()}] FILE: AFTER-action screenshot saved as {screenshot_name_after}.")
            log_action(f"FILE: AFTER-action screenshot saved as {screenshot_name_after}.")
            
            # Longer pause to allow the game to react
            time.sleep(2) 
            
        else:
            # Text not found (SILENT MODE)
            
            # Brief press of the 'tab' key (action happens but is not logged to the file)
            press_key_briefly('tab')
            
            # --- TIME CALCULATION FOR 1.5s CYCLE ---
            # Wait for the remaining part of the 1.5-second cycle
            elapsed_time = time.time() - start_time
            delay = 1.5 - elapsed_time 
            
            if delay > 0:
                time.sleep(delay)
            
    except Exception as e:
        # Error handling
        print(f"[{get_timestamp()}] FATAL ERROR DURING SCAN/STORAGE: {e}")
        log_action(f"FATAL ERROR IN LOOP: {e}")
        time.sleep(5)