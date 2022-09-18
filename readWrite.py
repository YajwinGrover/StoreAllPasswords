#!/usr/bin/env python3

from operator import ge, sub
from cryptography.fernet import Fernet
import json
import subprocess
import sys
import getpass

importantFile = open('/Users/yajwingrover/Desktop/DO_NOT_DELETE/important.txt')
importantThings = importantFile.readlines()
key = importantThings[0]
key = bytes(key,'utf-8')

fernet = Fernet(key)

filename = '__encryptStore__.txt'
file2 = '__usrStore__.txt'

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

    with open('/Users/yajwingrover/Desktop/DO_NOT_DELETE/store.json','w') as f:
        json.dump(thing, f)

def remove(site,thing):
    thing.pop(site)
    with open('/Users/yajwingrover/Desktop/DO_NOT_DELETE/store.json','w') as f:
        json.dump(thing,f)


def list_sites(thing):
    newThing = []
    for key in thing:
        newThing.append(key)

    newThing.sort()

    for key in newThing:
        print(key);

fullDict = {}
with open('/Users/yajwingrover/Desktop/DO_NOT_DELETE/store.json','r') as file:
    json_diction = json.load(file)





args = sys.argv
if(len(args) == 1):
    print("Please provide some input.")
    print('''if you want to add password run sap -a 
if you want to get password run sap -g 
if you want to remove password run sap -r 
if you want to list all sites with passwords run sap -l''')

elif(args[1] == '-a'):
    site = input("What is the password for: ")
    usr = input("What is the username: ")
    passwrd = input("What is the password: ")
    write(site.lower(),usr,passwrd,json_diction)
    subprocess.run("clear")
    print("Password added")
elif(args[1] == '-g'):
    passwrd = getpass.getpass()
    if passwrd != importantThings[1]:
        print("Wrong password")
    else:
        site = input("Look up password for what site: ")
        read(site.lower(),json_diction,True)
elif(args[1] == '-r'):
    passwrd = getpass.getpass()
    if passwrd != importantThings[1]:
        print("Wrong password")
    else:
        site = input("What is the site name that you want to remove: ")
        remove(site.lower(),json_diction)
        print("password removed")

elif(args[1] == '-l'):
    if json_diction == {}:
        print("There are no passwords")
    
    list_sites(json_diction)


#TODO: Work on searching for if pwd is added