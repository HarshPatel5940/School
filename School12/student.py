import csv


def find_all():
    file_name = open("D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\School12\student.csv", "r")
    reader = csv.reader(file_name)
    for row in reader:
        print(row)


find_all()
