import os

def pause():
    os.system("pause")
def clear(type):
    if type=="cmd":
        os.system("cls")
    if type=="python":
        print(''*100)
