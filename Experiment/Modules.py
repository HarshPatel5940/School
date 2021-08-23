import csv


def signup():
    f = open("registry.csv", "a", newline='')
    id1 = input("Create Your ID: ")
    name = input("Enter Your Name: ")
    password = input("Create Your Password: ")
    user1 = [id1, name, password]
    fwriter = csv.writer(f)
    fwriter.writerow(user1)
    print("User Created! ")


def login():
    while True:
        f = open("registry.csv", 'r')
        id1 = input("Enter Your ID: ")
        name = input("Enter your Name: ")
        password = input("Enter Your Password: ")
        fr = csv.reader(f)
        auth = False
        for row in fr:
            if id1 in row and password in row:
                print("You are Authorized!")
                auth = True
                break
        if auth:
            break
        if not auth:
            print("You Credentials Are Wrong!\nTRY AGAIN")
            continue


def datainserter(id1, appname):
    fname = f"User{id1}-{appname}.csv"  # To open the required file
    f = open(fname, 'a', newline="")
    fw = csv.writer(f)
    weekn = int(input("Enter The Week Number: "))
    while weekn <= 5:
        try:
            usagetime = int(input(f"Enter the Usage Duration Of {appname} for Week{weekn} (in minutes): "))
            batteryconsump = int(input(f"Enter the Battery Consumed by {appname} for Week{weekn}: "))
            dataconsump = int(input(f"Enter the Data Consumed by {appname} for Week{weekn} (in Megabites): "))
            timesopened = int(input(f"Enter How Many Times You Opened {appname} in Week{weekn}: "))
            row = [f"Week{weekn}", usagetime, batteryconsump, dataconsump, timesopened]
            fw.writerow(row)
        except ValueError:
            print("there was a value error")

        print(f"-----Data for Week{weekn} Has Been Successfully Added!-----\n.\n.\n.")
        weekn += 1
        opt = int(input(
            f"Select the Task You Wanna Perform\n1) Continue To Insert For Week{weekn + 1}\n2) Stop Inserting\nYour option[1]or[2]: "))
        if opt == 1:
            continue
        elif opt == 2:
            break
    if weekn == 5:
        print("Maximum Weeks Reached!")


def csvfilecreate(id1, appname):
    fname = f"User{id1}-{appname}.csv"  # For a custom file name
    f = open(fname, 'w')
    fw = csv.writer(f)
    column = ["Week Number", "Usage Duration(mins)", "Battery Condumptions(%)", "Data Consumption(in MB)",
              "Times Opened"]
    fw.writerow(column)
    print("yay!! File Successfully Created! ")
