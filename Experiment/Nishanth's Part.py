import csv
from os import listdir as Ld

user_file_path = "D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\project\data.csv"
admin_file_path = "D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\project\data_admin.csv"
app_data_path = "D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\project\data"

def app_data_create(id1, app_name):

    file_list = Ld(app_data_path)

    fname = f"User{id1}-{app_name}.csv"

    if fname in file_list:
        opt = input("WARNING!!\n-----The App Data For The Current User Has Already Been Created/Existing.\n-----Creating it Again Leads to Loss of Data\nDo you want to continue?[y]or[n] ")
    
        if opt == 'y':
            f = open(f"{app_data_path}/{fname}", 'w', newline="")
            fw = csv.writer(f)
            column = ["Week Number", "Usage Duration(mins)", "Battery Consumptions(%)", "Data Consumption(in MB)",
                    "Times Opened"]
            fw.writerow(column)
            print("File Successfully Created! ")

        else:
            print("--File Was Not Created--")

    elif fname not in file_list:
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

    while week_no <= 5:
        try:
            usagetime = int(input(f"Enter the Usage Duration Of {app_name} for Week{week_no} (in minutes): "))
            batteryconsump = int(input(f"Enter the Battery Consumed by {app_name} for Week{week_no}: "))
            dataconsump = int(input(f"Enter the Data Consumed by {app_name} for Week{week_no} (in Megabites): "))
            timesopened = int(input(f"Enter How Many Times You Opened {app_name} in Week{week_no}: "))
            row = [f"Week{week_no}", usagetime, batteryconsump, dataconsump, timesopened]
            fw.writerow(row)
        except ValueError:
            print("there was a value error")

        print(f"-----Data for Week{week_no} Has Been Successfully Added!-----\n.\n.\n.")
        week_no += 1
        opt = int(input(
            f"Select the Task You Wanna Perform\n1) Continue To Insert For Week{week_no + 1}\n2) Stop Inserting\nYour option[1]or[2]: "))
        if opt == 1:
            continue
        elif opt == 2:
            break
    if week_no == 5:
        print("Maximum Weeks Reached!")


    print(f"\n-----Data for Week{week_no} Has Been Successfully Added!-----\n")

def user_count():
    f = open(user_file_path,"r")
    fr = csv.reader(f)
    users = 0
    for row in fr:
        users += 1
    return users

def apps_count(id):
    userfilelist = []
    appslist = []
    file_list = Ld(app_data_path)
    for data in file_list:
        if f"User{id}" in data:
            userfilelist.append(data)
    for data in userfilelist:
        data.replace(f"User{id}-",'')
        appslist.append(data)
    print(f"Apps Tracked For User{id} = {appslist}")

#usercount and apps tracked added : )
