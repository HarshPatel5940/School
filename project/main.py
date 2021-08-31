from modules import *

while True:
    print("===================== main app menu =====================")
    ask1 = input("1) login as user (normal member)\n2) Login as super user (admin)\n3) register (signup)\n4) Close App\nWhat you want to do [1] [2] [3] [4] : ")
    if ask1 == "1":
        id1 = login()
        while True:
            print("===================== main User menu =====================")
            task = input("1)Show all apps\n2) create new app tracking\n3) Add tracking data to an existing app\n4)read tacking data of an app\n5)logout User\nWhat you want to do [1] [2] [3] [4] : ")
            if task == "1":
                apps_count(id1)
            elif task == "2":
                app = input("enter the name of the app you want to create")
                app_data_create(id1, app)
            elif task == "3":
                app = input("enter the name of the app")
                app_data_inserter(id1, app)
            elif task == "4":
                app = input("enter the name of the app")
                app_data_read(id1, app)
            elif task == "5":
                print("Logging out")
                break
    elif ask1 == "2":
        tup = admin_login()
        id1 = tup[0]
        power = tup[1]

        if power == "3":
            while True:
                print("================= Authorised owner menu! ==============")
                ask1 = input("1) add admin\n2) remove admin\n3) Show all users data\n4) update user password\n5) Show app tracked for the user\n6)logout\nWhat you want to do [1] [2] [3] [4] [5] : ")
                if ask1 == "1":
                    add_admin()
                elif ask1 == "2":
                    remove_admin()
                elif ask1 == "3":
                    user_count()
                    show_all_users()
                elif ask1 == "4":
                    update_user_data()
                elif ask1 == "5":
                    try:
                        id1 = int(input("Enter the user id you want to show apps"))
                        apps_count(id1)
                    except ValueError:
                        print("Invalid id")
                elif ask1 == "6":
                    break
                else:
                    print("Invalid option")
                    pass

        elif power == "2":
            while True:
                print("================= Authorised admin menu! ==============")
                ask1 = input("1) Show all users data\n2) update user password\n\3) Show all Apps for a user \n4)logout\nWhat you want to do [1] [2] [3] : ")
                if ask1 == "1":
                    user_count()
                    show_all_users()
                elif ask1 == "2":
                    update_user_data()
                elif ask1 == "3":
                    try:
                        id1 = int(input("Enter the user id you want to show apps"))
                        apps_count(id1)
                    except ValueError:
                        print("Invalid id")
                elif ask1 == "4":
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
