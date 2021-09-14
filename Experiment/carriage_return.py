from os import system as cmd
from time import sleep

from termcolor import colored

cmd("start cd ..")
cmd("cd 'D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\Discord\BKRP'")
cmd("venv\scripts\Activate")
cmd("python 'D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\Discord\BKRP\main.py'")


def color(text):
    color_text = colored(text, 'cyan')
    return color_text


print("\rwvwrvwbewbewbw", end="")
sleep(2)
print("\rhello", end="")
sleep(5)

# ============  Way 1 ======================
print("\rhello i am harsh", end="")
sleep(2)
print("\ri am actually nishanth", end="")
sleep(2)
print("\rUff i am suraj why don;t u understand", end="")

print("after returning the courser the second think must be Greater than first")
x = 0

while x < 100000:
    print('{}'.format(x), end='\r')
    x += 1
