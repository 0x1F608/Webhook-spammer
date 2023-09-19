import time
import requests
import os
import threading
from colorama import Fore
from pystyle import *

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()
print("-------------------------------------------------------")
print(Colorate.Horizontal(Colors.blue_to_cyan, "       0x1F608 super awesome webhook spammer!!"))
print("-------------------------------------------------------\n")

webhook = input("Webhook: ")
webhookname = input("Webhookname: ")
sleep = input("Delay: ")
count = input("Request number: ")
message = input("Message: ")
threadingoption = input("Threading? [y/n]: ")

if threadingoption == "y":
    threadingoption = "True"
elif threadingoption == "n":
    threadingoption = "False"

data = {
    "content" : message,
    "username" : webhookname
}
count = int(count)
sleep = int(sleep)

amountcount = 0

Write.Print("\nStarted spamming webhook!\n", Colors.blue_to_cyan)

print(threadingoption)
def spamwebhook():
    currenttime = time.strftime("%H:%M", time.localtime())  # Get current time here
    time.sleep(sleep)
    response = requests.post(webhook, data=data)
    if response.status_code == 200:
        print(f"{Fore.GREEN}[+]{Fore.RESET} [{currenttime}] | Successful requests sent!")  #| [{amountcount}/{count}]
    else:
        print(f"{Fore.RED}[+]{Fore.RESET} [{currenttime}] Failed to send webhook requests {response.status_code}")  #| [{amountcount}/{count}]

if threadingoption == "True":
    threads = []

    for i in range(count):
        t = threading.Thread(target=spamwebhook)
        t.daemon = True
        threads.append(t)

    for i in range(count):
        threads[i].start()
        
    for i in range(count):
        threads[i].join()

elif threadingoption == "False":
    for i in range(count):
        spamwebhook()
