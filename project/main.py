from modules import *

while True:
    print("===================== main app menu =====================")
    ask1 = input("1) login as user (normal member)\n2) Login as super user (admin)\n3) register (signup)\n4) Close App\nWhat you want to do [1] [2] [3] [4] : ")
    if ask1 == "1":
        id1 = login()
        while True:
            print("===================== main User menu =====================")
            task = input("1) create new app tracking\n2) Add tracking data to an existing app\n3)read tacking data of an app\n4)logout User\nWhat you want to do [1] [2] [3] [4] : ")
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
        tup = admin_login()
        id1 = tup[0]
        power = tup[1]

        if power == "3":
            while True:
                print("================= Authorised owner menu! ==============")
                ask1 = input("1) add admin\n2) remove admin\n3) Show all users data\n4) update user password\n5)logout\nWhat you want to do [1] [2] [3] [4] [5] : ")
                if ask1 == "1":
                    add_admin()
                elif ask1 == "2":
                    remove_admin()
                elif ask1 == "3":
                    show_all_users()
                elif ask1 == "4":
                    update_user_data()
                elif ask1 == "5":
                    break
                else:
                    print("Invalid option")
                    pass

        elif power == "2":
            while True:
                print("================= Authorised admin menu! ==============")
                ask1 = input("1) Show all users data\n2) update user password\n3)logout\nWhat you want to do [1] [2] [3] : ")
                if ask1 == "1":
                    show_all_users()
                elif ask1 == "2":
                    update_user_data()
                elif ask1 == "3":
                    break
                else:
                    print("Invalid option")
                    pass
        else:
            print("invalid power")
    elif ask1 == "3":
        sign_up()
    elif ask1 == "4":
        break
    else:
        print("incorrect option")
        pass
