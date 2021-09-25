# Trial Running of Single programs
from os import system as cmd

# this works unexpectedly well Lol

f = open("./wat the.py", "a")
f.write('print("Hello World")\n')
f.close()
cmd('python "wat the.py"')
