import time
import requests
import os
import threading
from colorama import Fore
from pystyle import *

if os.name == "nt":
    os.system("title Made with love by 0x1F608")
else:
    pass

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

madeby = "Made by https://github.com/0x1F608"

clear()
#print("-------------------------------------------------------")
#print(Colorate.Horizontal(Colors.blue_to_cyan, "       0x1F608 super awesome webhook spammer!!"))
#print("-------------------------------------------------------\n")
print(Colorate.Horizontal(Colors.blue_to_cyan, f"""   ____      ______________ ____  ____                                                   
  / __ \_  _<  / ____/ ___// __ \( __ )   _________  ____ _____ ___  ____ ___  ___  _____
 / / / / |/_/ / /_  / __ \/ / / / __  |  / ___/ __ \/ __ `/ __ `__ \/ __ `__ \/ _ \/ ___/
/ /_/ />  </ / __/ / /_/ / /_/ / /_/ /  (__  ) /_/ / /_/ / / / / / / / / / / /  __/ /    
\____/_/|_/_/_/    \____/\____/\____/  /____/ .___/\__,_/_/ /_/ /_/_/ /_/ /_/\___/_/     
                                           /_/   
{madeby}\n                                  
"""))




webhook = input(f"{Fore.LIGHTBLUE_EX}Webhook:{Fore.RESET} ")
webhookname = input(f"{Fore.LIGHTBLUE_EX}Webhookname:{Fore.RESET} ")
sleep = input(f"{Fore.LIGHTBLUE_EX}Delay:{Fore.RESET} ")
count = input(f"{Fore.LIGHTBLUE_EX}Request number:{Fore.RESET} ")
message = input(f"{Fore.LIGHTBLUE_EX}Message:{Fore.RESET} ")
threadingoption = input(f"{Fore.LIGHTBLUE_EX}Threading? [y/n]:{Fore.RESET} ")

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



Write.Print("\nStarted spamming webhook!\n", Colors.blue_to_cyan)
print("")

goodreqs = 0
failedreqs = 0

start_time = time.time()

def spamwebhook():
    global goodreqs, failedreqs
    
    currenttime = time.strftime("%H:%M", time.localtime())  # Get current time here
    time.sleep(sleep)
    response = requests.post(webhook, data=data)
    if response.status_code == 200:
        print(f"{Fore.GREEN}[+]{Fore.RESET} [{currenttime}] | Successful request sent!")
        goodreqs += 1
    else:
        print(f"{Fore.RED}[-]{Fore.RESET} [{currenttime}] Failed to send webhook {response.status_code}")
        failedreqs += 1

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

end_time = time.time()
elapsed_time = end_time - start_time

Write.Print(f"\nFinished spamming webhook!\n", Colors.blue_to_cyan)
print(f"{Fore.LIGHTBLUE_EX}Successful requests:{Fore.RESET} {goodreqs}\n{Fore.LIGHTBLUE_EX}Failed requests:{Fore.RESET} {failedreqs}\n{Fore.LIGHTBLUE_EX}Elapsed time:{Fore.RESET} {elapsed_time:.2f} seconds\n")
