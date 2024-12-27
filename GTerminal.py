import os
import sys
import time
import webbrowser as wb

os.system("title GTerminal")
os.system("echo off")
with open ("config.cnf", "r") as config:
    os.system("color " + config.readline())
    config.close()
os.system("cls")
l = os.getlogin()

while True:
    cmd = input("$")
    if cmd == "exit":
        sys.exit()
    elif cmd == "TW":
        wb.open_new("https://turbowarp.org/")
    elif cmd == "Pack":
        wb.open_new("")
    elif cmd == "cnf edit":
        with open("config.cnf", "w", encoding='utf-8') as cnf:
            r = cnf.write(input())
    
    elif cmd == "config":
        f = open('config.txt', 'r')
        a = f.readline()
        f.close()
        print(a)
    elif cmd == "exe":
        print("Opening auto-py-to-exe")
        os.system("auto-py-to-exe")
    else:
        os.system(cmd)
