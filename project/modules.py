import csv
from pandas import DataFrame as Df

user_file_path = "D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\project\data.csv"
admin_file_path = "D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\project\data_admin.csv"
app_data_path = "D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\project\data"


def write_user(id11, name, password):
    with open(user_file_path, "a", newline="") as f:
        print("Data is ok")
        file = csv.writer(f)
        user_row = [id11, name, password]
        file.writerow(user_row)
        print("New User is created")


def show_all_users():
    file1 = open(user_file_path, 'r')
    reader = csv.reader(file1)
    print(Df(reader, ))
    file1.close()


def app_data_create(id1, app_name):
    fname = f"User{id1}-{app_name}.csv"  # For a custom file name
    f = open(f"{app_data_path}/{fname}", 'w', newline="")
    fw = csv.writer(f)
    column = ["Week Number", "Usage Duration(mins)", "Battery Consumptions(%)", "Data Consumption(in MB)",
              "Times Opened"]
    fw.writerow(column)
    print("File Successfully Created! ")


def app_data_inserter(id1, app_name):
    fname = f"User{id1}-{app_name}.csv"
    f = open(f"{app_data_path}/{fname}", 'a', newline="")
    fw = csv.writer(f)
    week_no = int(input("Enter The Week Number: "))

    try:
        usage_time = int(input(f"Enter the Usage Duration Of {app_name} for Week{week_no} (in minutes): "))
        battery_consumption = int(input(f"Enter the Battery Consumed by {app_name} for Week{week_no}: "))
        data_consumption = int(input(f"Enter the Data Consumed by {app_name} for Week{week_no} (in Megabites): "))
        times_opened = int(input(f"Enter How Many Times You Opened {app_name} in Week{week_no}: "))
        row = [f"Week{week_no}", usage_time, battery_consumption, data_consumption, times_opened]
        fw.writerow(row)
    except ValueError:
        print("there was a value error")

    print(f"\n-----Data for Week{week_no} Has Been Successfully Added!-----\n")


def app_data_read(id1, app_name):
    file_name = f"User{id1}-{app_name}.csv"
    found = False
    try:
        file_open = open(f"{app_data_path}/{file_name}", 'r')
        file_reader = csv.reader(file_open)
        opt = input(
            "Select The Task\n1) Read Full Data\n2) Read Particular Week\nYour Option [1]or[2]")
        if opt == "1":
            print(Df(file_reader, ))
        elif opt == "2":
            week_number = input("Enter the Week for which you want to view the data  : ")
            header = ["Week Number", "Usage Duration(mins)", "Battery Consumptions(%)", "Data Consumption(in MB)",
                      "Times Opened"]
            for row in file_reader:
                if f"Week{week_number}" == row[0]:
                    print(Df(row, header))
                    found = True
            if found is False:
                print("no such app found")
        else:
            print("invalid option")
    except FileNotFoundError:
        print("No Such App was Found")


def login():
    while True:
        f = open(user_file_path, 'r')
        id1 = input("Enter Your ID: ")
        password = input("Enter Your Password: ")
        fr = csv.reader(f)
        auth = False
        for row in fr:
            if id1 in row and password in row:
                print(f"You are Authorized with id {id1}!")
                auth = True
                break
        if auth is True:
            break
        if auth is False:
            print("You Credentials Are Wrong!\nTRY AGAIN")
            chance = input("do you want leave login page? [y] [n] : ")
            if chance == "y":
                break
            else:
                print("invalid option! continuing login process")
    return id1


def admin_login():
    while True:
        f = open(admin_file_path, 'r')
        id1 = input("Enter Your ID: ")
        password = input("Enter Your Password: ")
        fr = csv.reader(f)
        power = 1
        auth = False

        for row in fr:
            if id1 in row and password in row:
                power = row[2]
                print(f"You are Authorized as {power}!")
                auth = True
                break
        if auth is True:
            break
        if auth is False:
            print("You Credentials Are Wrong!\nTRY AGAIN")
            chance = input("do you want leave login page? [y] [n] : ")
            if chance == "y":
                break
            else:
                print("continuing login process")
    return id1, power


def sign_up():
    while True:
        details_ok = True
        id1 = input("Enter your id : ")
        name = input("Enter your name : ")
        password = input("Enter your Password : ")

        file1 = open(user_file_path, 'r')
        reader = csv.reader(file1)

        for row in reader:
            if row[0] == id1:
                print("ERROR IN (same id1) ==> ", row)
                details_ok = False
            if row[1] == name:
                print("ERROR IN (same Name) ==> ", row)
                details_ok = False
        file1.close()

        if details_ok is True:
            write_user(id1, name, password)
            break
        if details_ok is False:
            print("\nInvalid details provided! \n")
            chance = input("do you want leave sign-up page? [y] [n] : ")
            if chance == "y":
                break
            else:
                print("invalid option! continuing Sign-up process")


def add_admin():
    id1 = int(input("enter user id : "))
    pwd = input("enter user password : ")
    power = "2"
    lst = [id1, pwd, power]

    f = open(admin_file_path, "a", newline="")
    file = csv.writer(f)
    file.writerow(lst)
    f.close()
    print(f"New Admin user with id {id1} has been added! ")


def remove_admin():
    id1 = input("enter id of the admin u wanna remove : ")
    before = []

    with open(admin_file_path, "r", newline="") as f:
        file = csv.reader(f)

        for row in file:
            if row[0] != id1:
                before.append(row)

    with open(admin_file_path, "w", newline="") as f:
        file = csv.writer(f)
        file.writerows(before)


def update_user_data():
    id1 = input("enter id of the admin u wanna remove : ")
    pwd = input("enter the new password for the user : ")
    before = []

    with open(admin_file_path, "r", newline="") as f:
        file = csv.reader(f)

        for row in file:
            if row[0] == id1:
                row[2] = pwd
                before.append(row)

    with open(user_file_path, "w", newline="") as f:
        file = csv.writer(f)
        file.writerows(before)

