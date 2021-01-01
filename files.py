#for working with files
import os.path
from os import system

#GradesKeeper store user's subjects names in this list - very important
subjects = []

def reset():
#this function makes all grades files empty | no returns, no arguments
    for i in range(len(subjects)):
        path = "oceny/" + subjects[i] + ".txt"
        file = open(path, "w")
        file.close()


def grades_list():
#this function prints grades lists for each subject | no returns, no arguments

    print("Oto lista ocen:")
    for i in range(len(subjects)):
        path = "oceny/" + subjects[i] + ".txt"
        file = open(path, "r")
        grades = file.readlines()

        for j, grade in enumerate(grades):
            grades[j] = grade.replace("\n","")

        print(subjects[i] + ":", grades, sep='')

        file.close()

def create_files():
#if files for saving grades don't exist, this function will create them | no returns, no arguments

    if not os.path.isdir("oceny"):
        os.makedirs("oceny")

    for subject in subjects:
        name = subject + ".txt"
        path = "oceny/" + name

        if not os.path.isfile(path):
            open(path, "a+").close()
