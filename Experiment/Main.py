import Modules

print("========================== DEVICE USAGE TRACKER ==========================")
while True:
    opt1 = int(input("------ MENU - 1 ------\nSelect The Task You Wanna Perform: \n1) Register \n2) Login\nEnter Your Option [1]or[2]: "))
    if opt1 == 1:
        Modules.signup()
    elif opt1 == 2:
        Modules.login()
    opt2 = int(input("------------------------XXXXXXXXXXXXXXX------------------------\n1)Previous Menu\n2)Next Menu\nYour Option [1]or[2]: "))
    if opt2 == 1:
        continue
    elif opt2 == 2:
        break
id1 = input("Re-Enter Your ID: ")
while True:
    print("------------- HOME -------------")
    opt3 = int(input("Select The Task You Wanna Perform:\n1) Add Data \n2) View Data\nYour Option [1]or[2]: "))
    if opt3 == 1:
        while True:
            print("=========== Data Inserter/Creater ===========")
            opt4 = int(input("Select The Task you Wanna Perform:\n1)Insert Data Into A File\n2)Create A File\nYour Option [1]or[2]: "))
            if opt4 == 1:
                app_name = input("Enter the App Name For Which You Wanna Insert The Data(in lower case): ")
                Modules.datainserter(id1, app_name)
            elif opt4 == 2:
                print("Note: Only CSV Files Are Created")
                app_name = input("Enter the App Name For Which You Wanna Create Data(in lower case): ")
                Modules.csvfilecreate(id1, app_name)
            opt5 = int(input("Select The Task you Wanna Perform:\n1) Run 'Data Inserter/Creater' Again\n2) Exit 'Data Inserter/Creater'\nYour Option [1]or[2]: "))
            if opt5 == 1:
                continue
            elif opt5 == 2:
                break
