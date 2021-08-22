from csv import reader

fh = open("School12/student.csv","r")
filereader = reader(fh)
rollno = input("Enter the Week: ")
for n in filereader:
    n = list(n)
    if n[0] == rollno:
        print(f"{n[1]}\n{n[2]}")