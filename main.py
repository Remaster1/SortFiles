import shutil
import sys
from pathlib import *


path = ''
chars = '\"\'\+-/*!&$#?=@<>[]abcdefghijklmnopqrstuvwxyz1234567890'


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
                    if Path(path+char+"\\"+file.name).is_file() == True:
                        replace = str(input(f"Do you want to replace the file {file.name} in directory {path+char}  (y/n)? :"))
                        if replace == "y":
                            try:
                                Path(path+char+"\\"+file.name).unlink()
                                shutil.move(path+file.name,path+char)
                            except Exception as ex:
                                print(f"Error: {ex}")
                        elif replace == "n":
                            continue
                    else:
                        try:
                            shutil.move(path+file.name,path+char)
                            print(file.name,"moved to ",char) 
                        except Exception as ex:
                            print(f"Error: {ex}")
                else:
                    path_dir = path+char.upper()
                    Path(path_dir).mkdir()
                    try:
                        shutil.move(path+file.name,path+char)
                        print(file.name,"moved to",char)  
                    except Exception as ex:
                        print(f"Error: {ex}")
                    
                        
                    
if __name__ == "__main__":
    UserInput()
    SortFiles()
    exit = input('Press Enter to exit...')