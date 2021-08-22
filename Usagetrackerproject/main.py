from modules import sign_up, find_all


while True:
    print("===================== main menu =====================")
    ask1 = input("What you want to do [r] [w] : ")
    if ask1 == "r":
        find_all()
    elif ask1 == "w":
        sign_up()
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

