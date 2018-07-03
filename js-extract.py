#!/usr/bin/python3

from bs4 import BeautifulSoup
import sys, os


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if (len(sys.argv) > 1):
        if (os.path.isfile(sys.argv[1]) == True):
                with open(sys.argv[1],"r") as file:
                        html = file.read()

                soup = BeautifulSoup(html,"lxml")
                scripts = soup.findAll("script")

                if (len(scripts) > 0):
                        print("[+] Scripts have been found in this html.")
                        for iter in range(0,(len(scripts))):
                                try:
                                        print(colors.OKGREEN + str('script #') + str((iter+1)) + str(' of ') + str(len(scripts)) + colors.ENDC)
                                        print(colors.OKBLUE + str(scripts[iter]) + '\n' + colors.ENDC)
                                except:
                                        continue
                else:
                        print("[-] No scripts found on page")
        else:
                print(colors.FAIL + '\n\t' + '[!] Invalid parameter' + '\n\t' + colors.BOLD + 'Usage:  ' + str(sys.argv[0]) + ' <input file>' + colors.ENDC + '\n')
else:
        print(colors.FAIL + '\n\t' + '[!] Missing parameter' + '\n\t' + colors.BOLD + 'Usage:  ' + str(sys.argv[0]) + ' <input file>' + colors.ENDC + '\n')
