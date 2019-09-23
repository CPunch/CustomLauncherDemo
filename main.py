'''
FFR-CustomLauncher: Main.py
Author: CPunch
Desc: Made by reverse engineering web api in the launcher & client. Ability to run a custom client or even go to google.com lol :)

DEPS: colorama, requests
'''

import requests
import getpass
import os
from colorama import Fore, Back, Style 
from urllib.parse import quote

# CHANGE THIS, REPLACE THE *WHOLE* STRING WITH THE PATH TO Retro.exe 
LAUNCH_PATH =       "/home/cpunch/.wine32/drive_c/users/cpunch/Application Data/FusionFall Universe/"
LAUNCH_ARG =        "WINEARCH=win32 WINEPREFIX=~/.wine32 wine Games/Retro/Retro.exe"

print("\nFFR-ReLauncher - Made by Reverse Engineering the FFR client & launcher!")
print(Fore.GREEN + "https://github.com/CPunch/CustomLauncherDemo" + Style.RESET_ALL)

BASE_URL =          "https://www.fusionfalluniverse.com"
UPDATE_CHECK_URL =  BASE_URL + "/api/launcher/check_update/"
LOGIN_URL =         BASE_URL + "/api/launcher/login/"
TOKEN_URL =         BASE_URL + "/api/launcher/game_token/"

SPOOFED_CLIENT_VERSION = "1.0.5"
FAKE_MAC = "90:e7:fb:d7:28:2d" # for some reason the FFU launcher likes to send your mac address to the server

# keeps cookies & headers across api requests
launcherSession = requests.Session()

# mimic launcher headers
launcherSession.headers = {
    'User-Agent': 'ffu-launcher', 
    'Launcher-Version': 'ffu-1.0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,*',
    'Host': 'www.fusionfalluniverse.com'
}

# get cookie
launcherSession.post(UPDATE_CHECK_URL, data='current_version='+SPOOFED_CLIENT_VERSION)

# grab user creds and get session id
username = input("Username: ")
password = getpass.getpass("Password: ")
session = ''

# login :eyes:
res = launcherSession.post(LOGIN_URL, data='device=ffudevid-' + FAKE_MAC + '&remember_me=false&session&username='+quote(username)+'&password='+quote(password))
result = res.json()
if result['errc'] == 0:
    print(Fore.GREEN + "Logged in successfully!" + Style.RESET_ALL)
    session = result['session']
    print('Session Token:' + session)
else:
    print(Fore.RED + "Invalid username & password combo!" + Style.RESET_ALL)
    exit(0)

# grab game launch info: TODO


# grab game token
res = launcherSession.post(TOKEN_URL, data='game_id=1&session=' + session + '&username='+quote(username))
result = res.json()
if not result['errc'] == 0:
    print(Fore.RED + "Token api failed!" + Style.RESET_ALL)
    exit(0)

print("Game token: " + result['token'])

os.chdir(LAUNCH_PATH)
os.system(LAUNCH_ARG + " -username " + username + " -token " + result['token'] + " -url https://playclient.fusionfallretro.com")