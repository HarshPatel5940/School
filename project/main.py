from modules import *

while True:
    print("===================== main app menu =====================")
    ask1 = input("1) login\n2)register (signup)\n3) Close App\nWhat you want to do [1] [2] [3]: ")
    if ask1 == "1":
        id1 = login()
        while True:
            print("===================== main User menu =====================")
            task = input("1) create new app tracking\n2) Add tracking data to an existing app\n3)read tacking data of an app\n4)logout User")
            if task == "1":
                app = input("enter the name of the app you want to create")
                app_data_create(id1, app)
            elif task == "2":
                app = input("enter the name of the app")
                app_data_inserter(id1, app)
            elif task == "3":
                app = input("enter the name of the app")
                app_data_read(id1, app)
            elif task == "4":
                print("Logging out")
                break
    elif ask1 == "2":
        sign_up()
    elif ask1 == "3":
        break
    else:
        print("incorrect option")
        pass
