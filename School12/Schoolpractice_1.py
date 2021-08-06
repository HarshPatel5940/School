# QUESTION 1 (14/06/2021)

# --->write a program that accepts a number between 1 and 365 and get the day of 1 from the user. And then print which day that number is.

Names = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

print("Project Done By HARSH N PATEL \nclass - 12A")

# Trying/practising error Handling
Num_1 = int(input("Enter day number: "))

if Num_1 < 1 or Num_1 > 365:
    print("Invalid Input \nPlease enter within range 1-365")
    Num_1 = int(input("Enter day number: "))

    if Num_1 < 1 or Num_1 > 365:
        print("USER IS DUMB \nSHUTTING DOWN...")

    else:
        print("Number accepted \n")
        firstDay = input("First day of year: ")

        if firstDay not in Names:
            print(
                f"please say any Valid day Name. Giving List of Valid Day Names \n{Names}")  # Using Functional String to make work easier
            firstDay = "First day of year: "

            if firstDay not in Names:
                print("USER IS DUMB \nSHUTTING DOWN...")
            else:
                print("Day Name Accepted")
                if Num_1 == 1:
                    print(firstDay)
                else:
                    startDay = Names.index(str.upper(firstDay))
                    currDay = Num_1 % 7 + startDay - 1

                    if currDay >= 7:
                        currDay = currDay - 7

                    print("Day on day number", Num_1, ":", Names[currDay])

        else:
            print("Day Name Accepted \n")

            if Num_1 == 1:
                print(firstDay)
            else:
                startDay = Names.index(str.upper(firstDay))
                currDay = Num_1 % 7 + startDay - 1

                if currDay >= 7:
                    currDay = currDay - 7

                print("Day on day number", Num_1, ":", Names[currDay])
else:
    print("Number accepted \n")

    firstDay = input("First day of year: ")

    if firstDay not in Names:
        print(f"please say any Valid day Name. Giving List of Valid Day Names \n {Names}")
        firstDay = "First day of year: "

        if firstDay not in Names:
            print("USER IS DUMB \nSHUTTING DOWN...")

        else:
            print("Day Name Accepted")
            if Num_1 == 1:
                print(firstDay)
            else:
                startDay = Names.index(str.upper(firstDay))
                currDay = Num_1 % 7 + startDay - 1

                if currDay >= 7:
                    currDay = currDay - 7

                print("Day on day number", Num_1, ":", Names[currDay])

    else:
        print("Day Name Accepted \n")

        if Num_1 == 1:
            print(firstDay)
        else:
            startDay = Names.index(str.upper(firstDay))
            currDay = Num_1 % 7 + startDay - 1

            if currDay >= 7:
                currDay = currDay - 7

            print("Day on day number", Num_1, ":", Names[currDay])

# QUESTION 2 (14/06/2021)

# ---> write a program that inputs an integer in range 0-999 and then prints if the integer entered is a 1/2/3 digit numbers (using elif)

Number = input("Please Enter a Number between 1- 999")

if len(Number) == 1:
    print(Number, "is a Single digit Number")

elif len(Number) == 2:
    print(Number, "is a Double digit Number")

elif len(Number) == 3:
    print(Number, "is a Trible digit Number")

else:
    print("Number is not between 1 - 999")

# QUESTION 3 (14/06/2021)

num = int(input("Enter a number: "))
if num >= 10:
    if num >= 100:
        if num >= 1000:
            print("Number is invalid")
        else:
            print("Three digits")
    else:
        print("Two digits")
else:
    print("One digit")

# Ending Part 1
print("Completed Executing Program. \ndate : 14/06/21 \nDone by : HARSH N PATEL\nClass : XII - A")

# Sorting
# Bubble Sorting Lesson

l1 = [42, 29, 74, 11, 65, 59]
n = len(l1)
print("Original list", l1)
for i in range(n - 1):
    for j in range(n - i - 1):
        if l1[j] > l1[j + 1]:
            l1[j], l1[j + 1] = l1[j + 1], l1[j]
        print("sorted list", l1)

# QUESTION 6 (19/06/21)
# Write a python script to input a number and count the occurrence of that given number in the given list,

L1 = [10, 20, 30, 40, 10, 50, 10, 10, 20, 30, 40, 10, 50, 10, 10, 20, 30, 40, 10, 50, 10, 10, 20, 30, 40, 10, 50, 10,
      10, 20, 30, 40, 10, 50, 10, 10, 20, 30, 40, 10, 50, 10, 10, 20, 30, 40, 10, 50, 10, 10, 20, 30, 40, 10, 50, 10]
a = int(input("Pls enter number u want to find the recurrence of : "))

print(f"The Number of Times {a} is used is - ", L1.count(a))

# Question 7 (21/06/21)
# Write a Python Program INput any two tuples and swap there Values

a = tuple()
n = int(input("number of values"))
for i in range(n):
    a = input("enter elements")
    a = a + (a,)

b = tuple()
m = int(input("number of values"))
for i in range(m):
    a = input("enter elements")
    b = b + (a,)
print("before swapping", a, b)

a, b = b, a

print("after swapping", a, b)

# QUESTION 8 (22/06/21)
# Input a dictionary from users of different sections and show the Output

# -----------using while
my_dic = {}
n = int(input("Enter the Number of sections we have"))
a = 1
while a <= n:
    x, y = input("Enter the section and subject separated by (--) :").split("--")
    my_dic[x] = y
    a += 1

for i in my_dic:
    print("Section ", i, ' : ', my_dic[i])

# -----------Using for
my_dic2 = {}
n = int(input("Enter number of sections: "))

for x in range(n):
    a, b = input("Enter the section and subject sepereated by (--) :").split("--")
    my_dic2[a] = b

for i in my_dic2:
    print("Section ", i, ' : ', my_dic2[i])

# QUESTION 9 (22/06/21)
# Write a program to store stuent information like admission number like
# Admission number, roll no,  name , Marks (Adminssion number should be Key)

n = 1
Students_no = int(input("Number Of student's data u want to add in the database : "))
data = {}

while n <= Students_no:
    admission_no = int(input("Enter ur admission number : "))
    lst = []
    roll_no = int(input("Enter ur roll number : "))
    name = input("Enter Your Full name : ")
    marks = float(input("Enter ur Average marks in all Subjects : "))
    lst.append(roll_no)
    lst.append(name)
    lst.append(marks)
    data[admission_no] = lst

    print("\nData has been accepted !\n")
    n += 1
print(f"-------- \n{data}\n----------\nexecution completed")

# Just Trying to learn to import Files
import functions as fnc

print(fnc.areaCircle(10))
print(fnc.areaRectangle(10, 20))
print(fnc.areaCylinder(10, 7))

# ==== display the size of the file in bytes f= .read > len(f)
# ==== display number of lines  f = .headlines > len(f)

# Practice Question | 14/7/2021

stu1 = int(input("Number of Students of data u want to enter"))
f = open("data.txt", "w")
for i in stu1:
    roll = int(input("Enter the roll number : "))
    name = input("Enter the name of the student : ")
    english = float(input("Enter English Marks : "))
    maths = float(input("Enter your maths marks : "))
    science = float(input("enter Your science marks : "))
    tamil = float(input("enter Your tamil marks : "))
    hindi = float(input("enter Your hindi marks : "))

    r = f"{roll},{name},{english},{maths},{science},{tamil},{hindi} \n "
    f.write(r)
f.close()

f = open("data.txt", "r")
for line in f.readline():
    print(f)
f.close()

# ==========================================================================================
# Practice Question | 20/7/2021
import pickle


def b_write():
    file_1 = open('emp.dat', 'wb')
    data1 = ["1. python", "2, java", "3. C++", "4. vb", "5. Oracle"]
    try:
        pickle.dump(data1, file_1)
    except EOFError:
        file_1.close()


def b_read():
    file_1 = open('emp.dat', 'rb')
    try:
        data1 = pickle.load(file_1)
        print(data1)
    except EOFError:
        file_1.close()


b_write()
b_read()
print("Data read successfully... ")

# ========================================================================================
import pickle


def file_write(emp_no):
    file_2 = open('emp.dat', 'ab')
    n1 = 1
    while n1 <= emp_no:
        name1 = input("enter your name : ")
        try:
            salary = int(input("enter your Salary : "))
            l1 = {"Name": name1, "salary": salary}
            try:
                pickle.dump(l1, file_2)
            except EOFError:
                file_2.close()
            n1 += 1
        except ValueError:
            print("There was ValueError pls enter again")


def file_find_same(sal):
    f1 = open("D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\Programs\School 12\emp.dat", "rb")
    try:
        while True:
            data1 = pickle.load(f1)
            if data1["salary"] == sal:
                print("==> ", data1["Name"])
    except EOFError:
        f1.close()


def file_show():
    f1 = open("D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\Programs\School 12\emp.dat", "rb")
    try:
        while True:
            data1 = pickle.load(f1)
            if data1["salary"] >= 0:
                print("==> ", data1["Name"], "-", data1["salary"])
    except EOFError:
        f1.close()


while True:
    print("==================================== New Block ====================================\n")
    Ask_action = input("==> [r] = read\n=> [a]= write/append \nWhat do you want to do? [r] or [a] : ")

    if Ask_action.lower() == "a":
        try:
            temp_no = int(input("Number of employees data you want to enter : "))
            file_write(temp_no)
        except ValueError:
            print("There was ValueError pls enter again")

    elif Ask_action.lower() == "r":
        read_action = input("find by salary [fs] \n find all [fa]")
        if read_action.lower() == "fs":
            try:
                temp_sal = int(input("For Which salary u want find : "))
                file_find_same(temp_sal)
            except ValueError:
                print("There was a ValueError PLs enter a Valid Salary")
        elif read_action.lower() == "fa":
            file_show()
    else:
        print("Invalid Option")
        pass
    Ask_2 = input("=> [y] = yes\n=> [n] = no\nWould you like to continue? : ")

    if Ask_2.lower() == "n":
        break
    elif Ask_2.lower() == "y":
        pass
    else:
        pass
