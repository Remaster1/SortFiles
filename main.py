import shutil
import sys
from pathlib import *
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-l", help="sort files only on letters", action="store_true")
parser.add_argument("-s", help="sort files only on signs",  action="store_true")
parser.add_argument("-n", help="sort files only on numbers", action="store_true")
parser.add_argument("-m", help="sort files by massive chars")
parser.add_argument("-d", help="set directory to sort files")
parser.add_argument("-c", help="print sort logs on terminal", action="store_true")
args = parser.parse_args()


path = os.getcwd()
logs = False
chars = '\"\'\+-/*!&$#?=@<>[]{}abcdefghijklmnopqrstuvwxyz1234567890'


if args.c:
    logs = True
if args.l:
    chars = "abcdefghijklmnopqrstuvwxyz"
if args.s:
    chars = '\"\'\+-/*!&$#?=@<>[]{}'
if args.m:
    chars =  args.m
if args.n:
    chars = '1234567890'
if args.d:
    path = args.d

if sys.version_info > (3,0):
    print('Python 3.x has been detected')
else:
    exit("Please run in Python 3.x!")


def CheckCorrectDir():
    global path
    if Path(path).is_dir():
        print('Corrected directory!')
    else:
        print("Directory has not exsist")
        exit()

def SortFiles():
    global path
    files = Path(path).glob("*.*")
    path = path+"/"
    for file in files:
        for char in chars:
            if file.name[0].lower() == char:
                char = char.upper()
                if Path(path+char).is_dir():
                    if Path(path+char+"/"+file.name).is_file() == True:
                        replace = str(input(f"Do you want to replace the file {file.name} in directory {path+char}  (y/n)? :"))
                        if replace == "y":
                            try:
                                Path(path+char+"/"+file.name).unlink()
                                shutil.move(path+file.name,path+char)
                            except Exception as ex:
                                print(f"Error: {ex}")
                        elif replace == "n":
                            continue
                    else:
                        try:
                            shutil.move(path+file.name,path+char)
                            if logs:
                                print(f"{file.name} moved to {char}") 
                        except Exception as ex:
                            print(f"Error: {ex}")
                else:
                    path_dir = path+char.upper()
                    Path(path_dir).mkdir()
                    try:
                        shutil.move(path+file.name,path+char)
                        if logs:
                            print(f"{file.name} moved to {char}")  
                    except Exception as ex:
                        print(f"Error: {ex}")
                    
                        
                    
if __name__ == "__main__":
    CheckCorrectDir()
    SortFiles()
