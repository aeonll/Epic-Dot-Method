import subprocess
import time
import os
import sys
import random
import threading

import pyautogui
from itertools import combinations
import pygetwindow as gw

USED_EMAILS_FILE = "used_emails.txt"
LAST_USED_EMAIL_FILE = "last_used_email.txt"

epic_launcher_path = "C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win64\EpicGamesLauncher.exe"
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

chrome_url = "https://mail.google.com"
process_name = "FortniteClient-Win64-Shipping.exe"
res = pyautogui.size()

adjectives = [
    "Quick", "Bright", "Brave", "Calm", "Eager", "Fancy", "Gentle", "Happy",
    "Jolly", "Kind", "Lively", "Merry", "Nice", "Proud", "Shiny", "Witty",
    "Bold", "Clever", "Fierce", "Grim", "Keen", "Loyal", "Mighty", "Noble",
    "Serene", "Valiant", "Fearless", "Graceful", "Radiant", "Swift", "Daring",
    "Quiet", "Silent", "Stormy", "Vibrant", "Majestic", "Mystic", "Vigilant",
    "Steady", "Rugged", "Sleek", "Vivid", "Frosty", "Luminous", "Glorious",
    "Timeless", "Epic", "Regal", "Wise","Ethereal", "Blazing", "Heroic",
    "Arcane", "Mystical", "Stalwart", "Zealous", "Frosty", "Gritty", "Mysterious",
    "Nimble", "Omniscient", "Resolute", "Tenacious", "Unyielding", "Venerable", "Greasy",
    "Petite", "Hard", "Radical", "Wiggly", "Rigid", "Squeaky", "Spiteful", "Rotund"
]


nouns = [
    "Lion", "Tiger", "Eagle", "Panther", "Dragon", "Wolf", "Falcon", "Phoenix",
    "Knight", "Warrior", "Hunter", "Ranger", "Sage", "Wizard", "Monarch",
    "Guardian", "Champion", "Vanguard", "Sentinel", "Paladin", "Seeker", "Nomad",
    "Voyager", "Explorer", "Conqueror", "Scholar", "Architect", "Artisan", "Alchemist",
    "Gladiator", "Behemoth", "Cyclone", "Titan", "Tempest", "Revenant", "Juggernaut",
    "Berserker", "Samurai", "Ronin", "Corsair", "Marauder", "Sorcerer", "Pioneer",
    "Outlaw", "Mercenary", "Strategist", "Enchanter", "Invoker", "Shark",
    "Oracle", "Prophet", "Harbinger", "Mystic", "Shadow", "Specter", "Phoenix",
    "Valkyrie", "Warlock", "Warlord", "Emissary", "Pilgrim", "Wanderer", "Plaza", "Noodle",
    "Goober", "Rombus", "Aarush", "Shufflebottom", "Top", "Bottom", "Prisoner", "Victim", "Scoundrel",
    "Spazz", "Feet", "Foot", "Toe", "Breast", "Rack", "Slave", "Prefect", "Sun", "Moon", "Flame"
]

# Opens epic launcher
subprocess.Popen([epic_launcher_path])
time.sleep(2)

try:
    #maximizes and "clicks on" epic launcher
    epic_window = gw.getWindowsWithTitle('Epic Games Launcher')[0]
    epic_window.maximize() 
    epic_window.activate()
except IndexError:
    print("Epic Games Launcher window not found.")
    subprocess.Popen([epic_launcher_path])
    epic_window = gw.getWindowsWithTitle('Epic Games Launcher')[0]
    epic_window.maximize() 
    epic_window.activate()

def terminate_script():
    sys.exit()

def generate_username():

    while True:
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        k = random.randint(3, 5)
        numbers = ''.join(random.choices('0123456789', k=k))

        username = f"{adjective}{noun}{numbers}"
        if len(username) <= 16:
            return username

def initialize_files():
    if not os.path.exists(USED_EMAILS_FILE):
        open(USED_EMAILS_FILE, 'w').close()
    if not os.path.exists(LAST_USED_EMAIL_FILE):
        open(LAST_USED_EMAIL_FILE, 'w').close()

def load_used_emails():
    if os.path.exists(USED_EMAILS_FILE):
        with open(USED_EMAILS_FILE, 'r') as file:
            return set(line.strip() for line in file)
    return set()

def save_used_email(email):
    with open(USED_EMAILS_FILE, 'a') as file:
        file.write(email + '\n')

def load_last_used_email():
    if os.path.exists(LAST_USED_EMAIL_FILE):
        with open(LAST_USED_EMAIL_FILE, 'r') as file:
            return file.read().strip()
    return ""

def save_last_used_email(email):
    with open(LAST_USED_EMAIL_FILE, 'w') as file:
        file.write(email)

def generate_email_combinations(email):
    local, domain = email.split("@")
    combos = []

    for i in range(1, len(local)+1):
        for indices in combinations(range(1, len(local)), i):
            modified_local = local
            for index in sorted(indices, reverse=True):
                modified_local = modified_local[:index] + "." + modified_local[index:]

            modified_email = modified_local + "@" + domain
            combos.append(modified_email)

    return combos

def sleep(x):
    time.sleep(x)

# Opens chrome to get 2fa code on 2560 x 1440p
def open_chrome2560():

    sleep(.4)

    print("Opening Chrome ...")

    try:
        chrome_window = gw.getWindowsWithTitle('Google Chrome')[0]
        chrome_window.maximize() 
        chrome_window.activate()

        sleep(1)

        pyautogui.moveTo(170,61)
        pyautogui.click()
        pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
        pyautogui.press("enter")

        sleep(3)

    except IndexError:
        print("Chrome window not found.\nTrying again ...")

        pyautogui.press("winleft")
        sleep(.2)
        pyautogui.write("chrome")
        sleep(.2)
        pyautogui.press("enter")

        sleep(1)

        chrome_window = gw.getWindowsWithTitle('Google Chrome')[0]
        chrome_window.maximize() 
        chrome_window.activate()


        sleep(1)

        pyautogui.moveTo(170,61)

        pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
        pyautogui.press("enter")

        sleep(3)

    print("Chrome opened ...")
    print("Getting 2fa code ...")

    pyautogui.moveTo(118,248)
    pyautogui.click()

    sleep(2)

    pyautogui.moveTo(345, 181)
    pyautogui.doubleClick()

    sleep(15)
    pyautogui.click()
    sleep(.1)

    pyautogui.moveTo(res.width / 2, 543)
    pyautogui.click()

    sleep(1)

    pyautogui.scroll(-100000) 


    sleep(.6)

    pyautogui.moveTo(1393,652)
    pyautogui.doubleClick()

    pyautogui.keyDown("ctrl")
    pyautogui.press('c')
    pyautogui.keyUp("ctrl")

#TODO - have it do 2fa for 1080p
def open_chrome1920():

    try:
        chrome_window = gw.getWindowsWithTitle('Google Chrome')[0]
        chrome_window.maximize() 
        chrome_window.activate()


    except IndexError:
        print("Chrome window not found.")
        exit()

    pyautogui.moveTo(100,245)
    pyautogui.click()

    pyautogui.moveTo(343,174)
    pyautogui.click()

    sleep(15)

    pyautogui.click()

    sleep(.1)

    pyautogui.moveTo(767,541)
    pyautogui.click()

    sleep(1)

    pyautogui.scroll(-100000) 

    sleep(.6)

    pyautogui.moveTo(1073,292)
    pyautogui.doubleClick()

    pyautogui.keyDown("ctrl")
    pyautogui.press('c')
    pyautogui.keyUp("ctrl")

 # connects to and disconnects a lego account (if you are already logged in) for the lego skin on 2560 x 1440p
def lego_skin2560():
    sleep(5)

    print("Getting Lego skin")

    pyautogui.moveTo(2259,71)
    pyautogui.click()

    pyautogui.moveTo(1956,380)
    pyautogui.click()

    sleep(7)

    pyautogui.moveTo(805,731)
    pyautogui.click()

    sleep(3)

    pyautogui.moveTo(1145,1067)
    pyautogui.click()

    sleep(3)
    #connect acc
    pyautogui.moveTo(1369,871)
    pyautogui.click()

    sleep(3)

    pyautogui.moveTo(1276,850)
    pyautogui.click()

    sleep(3)

    pyautogui.moveTo(1145,1067)
    pyautogui.click()

    sleep(2)

    pyautogui.moveTo(1277,839)
    pyautogui.click()

    sleep(1)

    print("Lego skin owned ...")

    pyautogui.keyDown("ctrl")
    pyautogui.press('w')
    pyautogui.keyUp("ctrl")

 #TODO - connects to and disconnects a lego account (if you are already logged in) for the lego skin on 1920 x 1080p
def lego_skin1920():

    var = 1

def get_fort2560():

    print("Getting Fortnite ...")
    sleep(2)
    #click on library
    pyautogui.moveTo(109,233)
    pyautogui.click()

    sleep(1)
    #click on fort (may have to add 300 to x val)
    pyautogui.moveTo(574,711)
    pyautogui.click()

    sleep(2)
    #click on get
    pyautogui.moveTo(2126,797)
    pyautogui.click()

    sleep(1.5)
    #Check box to agree to TOS
    pyautogui.moveTo(821,1210)
    pyautogui.click()


    sleep(.5)
    #agree to TOS
    pyautogui.moveTo(1651,1211)
    pyautogui.click()

    sleep(2)
    #place order
    pyautogui.moveTo(1687,577)
    pyautogui.click()

    sleep(7.5)

    print("Fortnite owned ...")

    #view in library
    pyautogui.moveTo(1419,861)
    pyautogui.click()

    sleep(3)
    #open fort
    pyautogui.moveTo(591,658)
    pyautogui.click()

    sleep(1)
    #agree to more stuff
    pyautogui.moveTo(1054,1218)
    pyautogui.click()
    #agree
    pyautogui.moveTo(1284,1261)
    pyautogui.click()

    print("Opening Fortnite ...")

def sign_out2560():
    
    print("Checking for launcher ...")

    try:
        #maximizes and "clicks on" epic launcher
        print("Launcher found ...\nSigning out ...")
        epic_window = gw.getWindowsWithTitle('Epic Games Launcher')[0]
        epic_window.maximize() 
        epic_window.activate()

        pyautogui.moveTo(2261,72)
        pyautogui.click()
        sleep(.2)
        pyautogui.moveTo(1954,616)
        pyautogui.click()


    except IndexError:
        print("Epic Games Launcher window not found.")

#closes fort
def close_fort():

    sleep(2)

    print("Checking if Fortnite is open ...")
    try:
        subprocess.run(["taskkill", "/F", "/IM", process_name], check=True)
        print(f"{process_name} AKA 'Fortnite' has been closed.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to close {process_name} AKA 'Fortnite'. ")
        print(e)

def equip_lego():

    print("Equipping Lego skin ...")
    pyautogui.moveTo(836,966)
    pyautogui.click()
    sleep(.5)

    pyautogui.moveTo(1479,1302)
    for i in range(5):
        if i < 5:
            pyautogui.click()

    pyautogui.click()

    sleep(.2)

    pyautogui.scroll(10)

    sleep(1)

    pyautogui.moveTo(509,95)
    pyautogui.click()

    sleep(.7)

    pyautogui.moveTo(650,525)
    pyautogui.click()

    sleep(.7)

    pyautogui.moveTo(1763,629)
    pyautogui.click()

    sleep(.2)

    pyautogui.moveTo(1923,629)
    pyautogui.click()

    sleep(.8)

    pyautogui.moveTo(1523,413)
    pyautogui.click()

    sleep(.4)

    print("Lego skin equipped ...")

    pyautogui.press("esc")
    pyautogui.press("esc")
    pyautogui.press("esc")

    print("Adjusting Volume ...")

    sleep(1)

    pyautogui.moveTo(1759,1068)
    pyautogui.click()

    sleep(.4)

    pyautogui.moveTo(831,65)
    pyautogui.click()

    sleep(.25)

    pyautogui.moveTo(853,460)
    pyautogui.doubleClick()

    print("Music muted ...")
    

def main(email, username, password):

    GENNERATED_NAME = generate_username()

    used_emails = load_used_emails()  # Load the used emails
    last_used_email = load_last_used_email()
    
    combos = generate_email_combinations(email)
    remaining_combos = [email for email in combos if email not in used_emails]
    
    if not remaining_combos:
        print("No unused emails left. Enter new email")
        return

    email_to_use = remaining_combos[0]
    
    save_used_email(email_to_use)
    save_last_used_email(email_to_use)
    print(f"Using email: {email_to_use}")

    close_fort()
    sign_out2560()


    #path for 2560 x 1440p
    if res.width == 2560 and res.height == 1440:
        print(f"User resolution = {res.width}x{res.height}")
        
        time.sleep(2)

        pyautogui.moveTo(1231, 1117)

        pyautogui.click()

        sleep(1)

        # months
        pyautogui.moveTo(res.width / 2.25, res.height / 2)
        pyautogui.click()
        pyautogui.moveTo(res.width / 2.25, (res.height / 2) + 100)
        pyautogui.click()

        sleep(.15)

        # day
        pyautogui.moveTo(res.width / 2,res.height / 2)
        pyautogui.click()
        pyautogui.moveTo(res.width / 2, (res.height / 2) + 100)
        pyautogui.click()

        sleep(.15)

        # year
        pyautogui.moveTo(res.width / 1.85,res.height / 1.95 - 50)
        pyautogui.click()
        pyautogui.write("2000")

        sleep(.2)

        # continue to sign in
        pyautogui.moveTo(res.width / 2, res.height / 1.78)
        pyautogui.click()

        # write email
        sleep(.3)
        pyautogui.moveTo(res.width / 2,res.height / 2.68)
        pyautogui.click()
        pyautogui.write(email_to_use)

        sleep(.15)

        var = random.randint(1,2)

        if var == 1:

            #writes first name
            pyautogui.moveTo(res.width / 2.2, res.height / 2.34)
            pyautogui.click()
            pyautogui.write("Pornelius")

            sleep(.15)
            #writes lastname
            pyautogui.moveTo(res.width / 1.8, res.height / 2.34)
            pyautogui.click()
            pyautogui.write("Hubert")
        elif var == 2:
        #writes first name
            pyautogui.moveTo(res.width / 2.2, res.height / 2.34)
            pyautogui.click()
            pyautogui.write("Ferret")

            sleep(.15)
            #writes lastname
            pyautogui.moveTo(res.width / 1.8, res.height / 2.34)
            pyautogui.click()
            pyautogui.write("Damian")

        sleep(.15)

        #writes username
        pyautogui.moveTo(res.width / 2.2, res.height / 2.03)
        pyautogui.click()
        pyautogui.write(GENNERATED_NAME)
        pyautogui.write(username)

        sleep(.15)
        #writes password
        pyautogui.moveTo(res.width / 2.2, res.height / 1.9)
        pyautogui.click()
        pyautogui.write(password)
  
        sleep(.15)
        #clicks on something idk what
        pyautogui.moveTo(res.width / 2.3, res.height / 1.58)
        pyautogui.click()

        sleep(.15)
        #idfk
        pyautogui.moveTo(res.width / 2, res.height / 1.44)
        pyautogui.click()

        # Continue to get 2fa code


        #captcha completion time
        #sleep(10)
        sleep(.6)
        open_chrome2560()
    
        sleep(.5)
    
        #re-fullscreens epic launcher
        epic_window.activate()

        #pastes 2fa code into launcher
        pyautogui.moveTo(1123,712)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')


        lego_skin2560()

        #re-opens epic launcher
        epic_window.activate()

        get_fort2560()

        sleep(55)
        print("Hopefully Fortnite loaded, if not, adjust sleep time above")
        equip_lego()

    #TODO - finish 1920x1080p support
    #path for 1920x1080
    elif res.width == 1920 and res.height == 1080:

        print(f"User resolution = {res.width}x{res.height}")

        sleep(2)
        pyautogui.moveTo(898, 935) 
        pyautogui.click()

        sleep(1)

        # months
        pyautogui.moveTo(827,526)
        pyautogui.click()
        pyautogui.moveTo(821,589)
        pyautogui.click()

        sleep(.15)

        # day
        pyautogui.moveTo(958, 542)
        pyautogui.click()
        pyautogui.moveTo(945, 627)
        pyautogui.click()

        sleep(.15)

        # year
        pyautogui.moveTo(1066, 529)
        pyautogui.click()
        pyautogui.write("2000")

        sleep(.15)

        # continue to sign in
        pyautogui.moveTo(961, 633)
        pyautogui.click()

        # writes email
        sleep(.5)
        pyautogui.moveTo(res.width / 2,res.height / 2.68)
        pyautogui.click()
        pyautogui.write(email_to_use)

        sleep(.15)
        #writes firstname
        pyautogui.moveTo(res.width / 2.2, res.height / 2.34)
        pyautogui.click()
        pyautogui.write("Buy")

        sleep(.15)
        #writes lastname
        pyautogui.moveTo(res.width / 1.8, res.height / 2.34)
        pyautogui.click()
        pyautogui.write("fourteenfourtymf")
        

        sleep(.15)
        #Writes username
        pyautogui.moveTo(res.width / 2.2, res.height / 2.03)
        pyautogui.click()
        pyautogui.write(username)

        sleep(.15)
        #writes password
        pyautogui.moveTo(828, 635)
        pyautogui.click()
        pyautogui.write(password)

        sleep(.15)
        #clicks something idk what
        pyautogui.moveTo(res.width / 2, res.height / 1.44)
        pyautogui.click()

        sleep(.15)
        #idfk
        pyautogui.moveTo(944, 842)
        pyautogui.click()


        #remove if no captcha
        sleep(15)



        open_chrome1920()

        #re-fullscreens epic launcher
        epic_window.activate()

        #pastes 2fa code into launcher
        pyautogui.moveTo(799,532)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        lego_skin1920()

    

    else:
        print("Resolution not supported:  Please use 1440 or 1080")
        return
    
    os.system("taskkill /f /im chrome.exe")

    

if __name__ == "__main__":
    initialize_files() 
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <email> <password> <username>")
        sys.exit(1)

    email = sys.argv[1]
    password = sys.argv[2]
    username = sys.argv[3]

    main(email, username, password)

    print("Terminating script ...")
