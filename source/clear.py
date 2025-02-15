from os import name, system

def cls():
    if name == "nt":
        system("cls")
    else:
        system("clear")