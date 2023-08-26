#IMPORTACION DE LIBRERIAS
import os
import subprocess

#FUNCIONES
def random():
    os.system("ifconfig wlo1 down")
    os.system("macchanger -r wlo1")
    os.system("ifconfig wlo1 up")

def manual():
    macd = input("mac: ")
    os.system("ifconfig wlo1 down")
    os.system("macchanger -m " + macd + " wlo1")
    os.system("ifconfig wlo1 up")

def perm():
    os.system("ifconfig wlo1 down")
    os.system("macchanger -p wlo1")
    os.system("ifconfig wlo1 up")

def showp():
    os.system("macchanger -s wlo1 | grep Permanent")

def showa():
    os.system("macchanger -s wlo1 | grep Current")

#MAIN CODE
ask1 = input("Random -r- |  Manual -m- | Permanent -p- | Show perm MAC -sp- | Show actual mac -sa- : ")

if (ask1 == "r"):
    random()

if (ask1 == "m"):
    manual()

if (ask1 == "p"):
    perm()

if (ask1 == "sp"):
    showp()

if (ask1 == "sa"):
    showa()
