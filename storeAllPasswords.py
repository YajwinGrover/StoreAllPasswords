#!/usr/bin/env python3

from ast import For
from operator import ge, sub
from cryptography.fernet import Fernet
import json
import subprocess
import sys
import getpass
import random
import os

def setup():
    print('''          _____                    _____                    _____          
         /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \        
       /::::\    \              /::::\    \              /::::\    \       
      /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
    \:::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \   
  ___\:::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \  
 /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\ 
/::\   \:::\   \:::\____\/:::/  \:::\   \:::\____\/:::/  \:::\   \:::|    |
\:::\   \:::\   \::/    /\::/    \:::\  /:::/    /\::/    \:::\  /:::|____|
 \:::\   \:::\   \/____/  \/____/ \:::\/:::/    /  \/_____/\:::\/:::/    / 
  \:::\   \:::\    \               \::::::/    /            \::::::/    /  
   \:::\   \:::\____\               \::::/    /              \::::/    /   
    \:::\  /:::/    /               /:::/    /                \::/____/    
     \:::\/:::/    /               /:::/    /                  ~~         
      \::::::/    /               /:::/    /                               
       \::::/    /               /:::/    /                                
        \::/    /                \::/    /                                 
         \/____/                  \/____/                                  
                                                                           ''')

    print("Welcome to StoreAllPasswords, or SAP")
    print("Since this is you first time using this, lets get you set up")
    masterPass = input('Please enter the master password (can be changed later). Please keep in mind that if you are to forget this password, all stored data will be lost: ')
    setupFile = open('.important.txt','x')
    setupFile.close()
    fernetKey = Fernet.generate_key()
    fer = Fernet(fernetKey)
    with open('.important.txt','w+') as a:
        a.write(fernetKey.decode('utf-8') + "\n")
        a.write(fer.encrypt(masterPass.encode('utf-8')).decode('utf-8'))
    jsonFile = open('.store.json', 'w+')
    jsonFile.write("{}")
    jsonFile.close()

if not os.path.exists('.important.txt'):
    setup()
importantFile = open('.important.txt', 'r+')
importantThings = importantFile.readlines()
key = importantThings[0]
key = bytes(key,'utf-8')
ranArray = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '$', '?']
fernet = Fernet(key)


def read(site,thing, reveal):
    if site in thing:
        dicti =  thing[site]
        usrnm = dicti[0]
        pwd = dicti[1]
    
        print("Your username is: " + fernet.decrypt(usrnm.encode('utf-8')).decode('utf-8'))
        if(reveal):
            print("Password has be copied to clipboard")
            subprocess.run('pbcopy',universal_newlines=True, input=fernet.decrypt(pwd.encode('utf-8')).decode('utf-8'),shell=True)
        else:
            print("Your password is: " + fernet.decrypt(pwd.encode('utf-8')).decode('utf-8'))
    else:
        print("You do not have any entries for this site")



def write(site,usrnm ,pwd, thing):

    info = {
        site : [fernet.encrypt(usrnm.encode('utf-8')).decode('utf-8'), fernet.encrypt(pwd.encode('utf-8')).decode('utf-8')]
    }

    thing.update(info)

    with open('.store.json','w') as f:
        json.dump(thing, f)

def remove(site,thing):
    thing.pop(site)
    with open('.store.json','w') as f:
        json.dump(thing,f)


def get_sorted(thing):
    newThing = []
    for key in thing:
        newThing.append(key)

    newThing.sort()

    return newThing

def list_sites(thing):

    for key in get_sorted(thing):
        print(key);

def completer(text, keys):
    completed = []
    for key in keys:
        if key.startswith(text):
            completed.append(key)
    return completed

def gen_password():
    gend = ''
    for i in [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,0,0]:
        choice = random.choice(ranArray)
        gend += choice
    
    return gend



with open('.store.json','r') as file:
    json_diction = json.load(file)


def get_autocompleted(site):
    list = completer(site, get_sorted(json_diction))
    if len(list) == 1:
        print("Password for the site " + list[0])
        read(list[0].lower(),json_diction,True)
    elif len(list) == 0:
        print("No entries sorry.")
    else:
        for i in list:
            print(i," ")
        choice = input("Which site is it? (0-" + str(len(list) -1) + "): ")
        return list[int(choice)].lower()
    return "bleh"


print('''          _____                    _____                    _____          
         /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \        
       /::::\    \              /::::\    \              /::::\    \       
      /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
    \:::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \   
  ___\:::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \  
 /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\ 
/::\   \:::\   \:::\____\/:::/  \:::\   \:::\____\/:::/  \:::\   \:::|    |
\:::\   \:::\   \::/    /\::/    \:::\  /:::/    /\::/    \:::\  /:::|____|
 \:::\   \:::\   \/____/  \/____/ \:::\/:::/    /  \/_____/\:::\/:::/    / 
  \:::\   \:::\    \               \::::::/    /            \::::::/    /  
   \:::\   \:::\____\               \::::/    /              \::::/    /   
    \:::\  /:::/    /               /:::/    /                \::/____/    
     \:::\/:::/    /               /:::/    /                  ~~         
      \::::::/    /               /:::/    /                               
       \::::/    /               /:::/    /                                
        \::/    /                \::/    /                                 
         \/____/                  \/____/                                  
                                                                           ''')
print("Welcome back to SAP, what would you like to do?")
print('''
    [0] Get password
    [1] Add password
    [2] Remove password
    [3] List all stored passwords
    [4] Generate random password
    [5] Change master password
    [6] Learn about SAP!
''')
choice = int(input())

if choice == 0:
    passwrd = getpass.getpass()
    realPass = fernet.decrypt(importantThings[1].encode('utf-8')).decode('utf-8')
    if passwrd != realPass:
        print("Wrong password")
    else:
        site = get_autocompleted(input("Look up password for what site: ").lower())
        if not (site  == 'bleh'):   
            read(site,json_diction,True)

elif choice == 1:
    site = input("What is the password for: ")
    usr = input("What is the username: ")
    passwrd = input("What is the password: ")
    write(site.lower(),usr,passwrd,json_diction)
    subprocess.run("clear")
    print("Password added")

elif choice == 2:
    passwrd = getpass.getpass()
    realPass = fernet.decrypt(importantThings[1].encode('utf-8')).decode('utf-8')
    if passwrd != realPass:
        print("Wrong password")
    else:
        site = get_autocompleted(input("What is the site name that you want to remove: "))
        if not (site == 'bleh'):
            remove(site.lower(),json_diction)
            print("password removed")

elif choice == 3:
    if json_diction == {}:
        print("There are no passwords")
    
    list_sites(json_diction)

elif choice == 4:
    passwad = gen_password()
    subprocess.run('pbcopy',universal_newlines=True, input=passwad,shell=True)
    print(passwad)
    print("password saved to clipboard as well")
    answer = input("Add new password entry? Y/n")
    if(answer == 'Y'):
        site = input("What is the password for: ")
        usr = input("What is the username: ")
        passwrd = passwad
        write(site.lower(),usr,passwrd,json_diction)
        print("Password added")

elif choice == 5:
    newPass = input("Enter new master password: ")
    with open('.important', 'w+') as f:
        f.write(key.decode('utf-8'))
        f.write(fernet.encrypt(newPass.encode('utf-8')).decode('utf-8'))
        f.close()

elif choice == 6:
    print("StoreAllPasswords(SAP) is a CLI tool used to store passwords on your local machine. The passwords are encrypted using the Fernet library. Thanks for choosing SAP")



#TODO: Work on searching for if pwd is added