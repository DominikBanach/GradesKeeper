from files import subjects

from vulcan import Vulcan
import json, os

def new_acc(token, symbol, pin):
#this function connect GradesKeeper with user's Vulcan account | 3 arguments, no returns

    if os.path.isfile("cert.json"): os.remove("cert.json")

    certificate = Vulcan.register(token, symbol, pin)
    with open("cert.json", "w") as f: json.dump(certificate.json, f)


def fill_subjects_list():
#this function uses grades list to fill "subjects" list with user's subjects name

    with open("cert.json") as f:
        certificate = json.load(f)

    client = Vulcan(certificate)

    for grade in client.get_grades():
        if not grade.subject.name in subjects:
            subjects.append(grade.subject.name)


def update_grades():
#this function downloads grades from connected account | no arguments, no returns

    with open("cert.json") as f:
        certificate = json.load(f)

    client = Vulcan(certificate)

    for grade in client.get_grades():

        #grade_to_add
        if grade.weight == 0.0: continue
        elif grade.content == "":   grade_to_add = "np"
        elif grade.content == "1":  grade_to_add = "1"
        elif grade.content == "1+": grade_to_add = "1+"
        elif grade.content == "2":  grade_to_add = "2"
        elif grade.content == "2+": grade_to_add = "2+"
        elif grade.content == "2-": grade_to_add = "2-"
        elif grade.content == "3":  grade_to_add = "3"
        elif grade.content == "3+": grade_to_add = "3+"
        elif grade.content == "3-": grade_to_add = "3-"
        elif grade.content == "4":  grade_to_add = "4"
        elif grade.content == "4-": grade_to_add = "4-"
        elif grade.content == "4+": grade_to_add = "4+"
        elif grade.content == "5":  grade_to_add = "5"
        elif grade.content == "5-": grade_to_add = "5-"
        elif grade.content == "5+": grade_to_add = "5+"
        elif grade.content == "6":  grade_to_add = "6"
        elif grade.content == "6-": grade_to_add = "6-"
        elif grade.content == "+":  grade_to_add = "+"
        elif grade.content == "-":  grade_to_add = "-"
        else: continue

        #subject_to_add
        subject_to_add = grade.subject.name

        #add grade to file
        path = "oceny/" + subject_to_add + ".txt"
        file = open(path,"a")
        file.write(grade_to_add)
        file.write("\n")
        file.close()