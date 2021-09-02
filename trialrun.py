# Trial Running of Single programs
from os import system
from time import sleep
system("")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{bcolors.FAIL} Error test {bcolors.ENDC}")

print("\033[1;32m This text is Bright Green {bcolors.ENDC} \n")

# print t.red('This is red.')
# print t.bold_bright_red_on_black('Bright red on black')

# system("color 4")
# print("hii")
# sleep(10)
# system("color 7")
# print("hii")

