import shutil
import sys
from pathlib import *
path = ''
chars = '\"\'+-/*!&$#?=@<>[]abcdefghijklmnopqrstuvwxyz1234567890'
if sys.version_info > (3,0):
    print('Python 3.x has been detected')
else:
    exit("Please run in Python 3.x!")
def UserInput():
    global path
    while True:
        try:
            path = str(input("Select path:"))
        except ValueError:
            print("Please enter a valid value")
        else:
            if Path(path).is_dir():
                print('Corrected directory!')
                break
            else:
                print("Directory has not exsist")    
def SortFiles():
    global path
    path = path+"\\"
    files = Path(path).glob("*.*")
    for file in files:
        for char in chars:
            if file.name[0].lower() == char:
                if Path(path+char).is_dir():
                    shutil.move(path+file.name,path+char)
                    print(file.name,"moved to ",char)
                else:
                    path_dir = path+char
                    Path(path_dir).mkdir()
                    shutil.move(path+file.name,path+char)
                    print(file.name,"moved to",char)  
                    
            

UserInput()
SortFiles()
exit = input('Press Enter to exit...')

