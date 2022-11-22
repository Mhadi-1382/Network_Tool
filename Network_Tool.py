
# Network Tool
# Built by Mahdi Rabiee
# Created: Thursday, October 27, 2022


from getmac import get_mac_address as GetMAC
from colorama import Fore
from requests import *
import socket
import os


# Clear Screen
os.system("cls")


# Internet Status
def Status():
    url = "https://google.com"
    timeout = 3
    try:
        # requesting URL
        get(url, timeout=timeout)
        print("Status: Online")
    
    # catching exception
    except (ConnectionError, Timeout):
        print("Status: Offline")


# Splash Screen
SplashScreen = """
    ////
    //   N E T W O R K  T O O L
    /
"""
print(Fore.BLUE + SplashScreen + Fore.WHITE)

print("-" * 50)
print("System Name: " + socket.gethostname())
Internet = Status()
print("-" * 50 + "\n")

print("[1] NETSTAT - Troubleshooting and Network Analysis")
print("[2] Get Site IP (Hostname) Address")
print("[3] Get Public IP Address")
print("[4] Get Local IP Address")
print("[5] Show Password WIFI")
print("[6] Get MAC Address")
print("[7] Ping URL or IP")
print("[8] Exit The App \n")


# Input command
def Input_command():
    query = int(input(">>> "))
    return query

# Output command
def Output_command(output):
    print("<<< " + output)


# Commands
while True:
    
    query = Input_command()


    if query == int(1):
        os.system("netstat")

    elif query == int(2):
        HostnameAddress = input("<<< Enter Your Address (Google.com, etc.): ")
        IPAddress = socket.gethostbyname(HostnameAddress)
        Output_command("Site IP Address is: " + IPAddress)

    elif query == int(3):
        IPAddressPublic = get('https://api.ipify.org').text
        Output_command("Your Public IP Address is: " + IPAddressPublic)

    elif query == int(4):
        HostnamePC = socket.gethostname()
        IPAddressLocal = socket.gethostbyname(HostnamePC)
        Output_command("Your Local IP Address is: " + IPAddressLocal)

    elif query == int(5):
        os.system("netsh wlan export profile folder=C:\\Users\\{0}\\Desktop\\ key=clear".format(socket.gethostname()))

    elif query == int(6):
        Output_command("Your MAC Address is: " + GetMAC())

    elif query == int(7):
        Inp_ping = input("<<< URL or IP: ")
        os.system("ping {0}".format(Inp_ping))

    elif query == int(8):
        exit()
    
    else:
        Output_command(Fore.YELLOW + f"Recipe {query} Not Found." + Fore.WHITE)