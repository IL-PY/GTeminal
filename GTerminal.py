import os
import sys
import time
import webbrowser as wb


l = os.getlogin()
os.system(f"title GTerminal/{l}")
os.system("echo off")
with open ("config.cnf", "r") as config:
    os.system("color " + config.readline())
    config.close()
os.system("cls")
print("GTerminal is loaded")
time.sleep(0.5)
os.system('cls')
print("G")
time.sleep(0.1)
os.system('cls')
print("Go")
time.sleep(0.1)
os.system('cls')
print("Goo")
time.sleep(0.1)
os.system('cls')
print("Good")
time.sleep(0.1)
os.system('cls')

print("Good l")
time.sleep(0.1)
os.system('cls')
print("Good lu")
time.sleep(0.1)
os.system('cls')
print("Good luc")
time.sleep(0.1)
os.system('cls')
print("Good luck")
time.sleep(2)
os.system('cls')




while True:
    cmd = input("$")
    if cmd == "exit":
        sys.exit()
    elif cmd == "TW":
        wb.open_new("https://turbowarp.org/")

    elif cmd == "cnf edit":
        with open("config.cnf", "w", encoding='utf-8') as cnf:
            r = cnf.write(input())
    elif cmd == "config":
        f = open('config.cnf', 'r')
        a = f.readline()
        f.close()
        print(a)
    elif cmd == "exe":
        print("Opening auto-py-to-exe")
        os.system("auto-py-to-exe")
    else:
        os.system(cmd)
