#!/usr/bin/python3
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, Back, Style
from socket import gethostbyaddr
from os import system, name, mkdir
from os.path import exists as File_exists

# Create Folder
try:
    mkdir("Results")
except:
    pass

if name == "nt":
    system("cls")
else:
    system("clear")


def ip_domain(val):
    try:
        with open("Results/domain.txt", "a") as ip:
            ip.write(gethostbyaddr(val))
            ip.writelines("\n")
    except:
        pass


def main():
    print(f"""
                                                
ooo.                          o       o  .oPYo. 
8  `8.                                8  8    8 
8   `8 .oPYo. ooYoYo. .oPYo. o8 odYo. 8 o8YooP' 
8    8 8    8 8' 8  8 .oooo8  8 8' `8 8  8      
8   .P 8    8 8  8  8 8    8  8 8   8 8  8      
8ooo'  `YooP' 8  8  8 `YooP8  8 8   8 8  8
    
    {Fore.WHITE + Back.RED + "[+] Ip To domain by ./Mrmad" + Style.RESET_ALL}
""")
    val = input("List : ")
    ThreadVal = input("Threads : ")
    if File_exists(val):
        with open(val, "r") as r:
            read = r.read()
            l_ = read.split("\n")
            with ThreadPool(int(ThreadVal)) as Th:
                print(Fore.YELLOW + "[+] Processing ...." + Style.RESET_ALL)
                Th.map(ip_domain, l_)
                Th.close()
                Th.join()
                print(Fore.GREEN + "[+] Done Thanks" + Style.RESET_ALL)
    else:
        print(Fore.RED + "[!] File Not Found")


if __name__ == "__main__":
    main()
