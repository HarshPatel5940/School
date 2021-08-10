import csv


def find_all():
    file_name = open("D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\School12\student.csv", "r")
    reader = csv.reader(file_name)
    for row in reader:
        print(row)


def find_by_number():
    print("did not do anything yet")


def find_by_name():
    print("did not do anything yet")


def find_by_marks():
    print("did not do anything yet")


def get_help():
    print("did not do anything yet")


find_all()
