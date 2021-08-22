from modules import sign_up, show_all_users

while True:
    print("===================== main menu =====================")
    ask1 = input("What you want to do [r] [w] : ")
    if ask1 == "r":
        show_all_users()
    elif ask1 == "w":
        id1 = input("Enter your id : ")
        name = input("Enter your name : ")
        password = input("Enter your Password : ")
        sign_up(id1, name, password)
    else:
        print("incorrect option")
        pass

    ask = input("do you want continue? [y] [n] : ")
    if ask == "y":
        pass
    elif ask == "n":
        break
    else:
        print("incorrect option")
        pass
