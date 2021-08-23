import csv
file_path = "D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\project\data.csv"


def write_user(id1, name, password):
    with open(file_path, "a", newline="") as f:
        print("Data is ok")
        file = csv.writer(f)
        user_row = [id1, name, password]
        file.writerow(user_row)
        print("New User is created")


def sign_up(id1, name, password):
    ready = True
    file1 = open(file_path, 'r')
    reader = csv.reader(file1)
    for row in reader:
        if row[0] == id1:
            print("ERROR IN (same ID) ==> ", row)
            ready = False
        if row[1] == name:
            print("ERROR IN (same Name) ==> ", row)
            ready = False
    file1.close()
    if ready is True:            
        write_user(id1, name, password)


def show_all_users():
    file1 = open(file_path, 'r')
    reader = csv.reader(file1)
    for row in reader:
        print(row)
    file1.close()
