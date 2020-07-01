from vulcan import Vulcan
import json, os

def new_acc(token, symbol, pin):

    if os.path.isfile("cert.json"): os.remove("cert.json")

    certificate = Vulcan.register(token, symbol, pin)
    with open("cert.json", "w") as f: json.dump(certificate.json, f) #do testów i zrobic te trzy stringi jako globalne w mainie to bedzie mozna sprawdzać czy są puste

def update_grades():

    with open("cert.json") as f:
        certificate = json.load(f)

    client = Vulcan(certificate)

    for grade in client.get_grades():

        #ocena
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

        #przedmiot
        if grade.subject.name == "Język angielski":             subject_to_add = "j.angielski"
        elif grade.subject.name == "Wiedza o społeczeństwie":     subject_to_add = "wos"
        elif grade.subject.name == "Plastyka":                    subject_to_add = "plastyka"
        elif grade.subject.name == "Matematyka":                  subject_to_add = "matematyka"
        elif grade.subject.name == "Religia":                     subject_to_add = "religia"
        elif grade.subject.name == "Chemia":                      subject_to_add = "chemia"
        elif grade.subject.name == "Historia":                    subject_to_add = "historia"
        elif grade.subject.name == "Język niemiecki":             subject_to_add = "j.niemiecki"
        elif grade.subject.name == "Fizyka":                      subject_to_add = "fizyka"
        elif grade.subject.name == "Informatyka":                 subject_to_add = "informatyka"
        elif grade.subject.name == "Wychowanie fizyczne":         subject_to_add = "wf"
        elif grade.subject.name == "Biologia":                    subject_to_add = "biologia"
        elif grade.subject.name == "Edukacja dla bezpieczeństwa": subject_to_add = "edb"
        elif grade.subject.name == "Język polski":                subject_to_add = "j.polski"
        elif grade.subject.name == "Geografia":                   subject_to_add = "geografia"
        else: continue

        #dodanie do pliku
        path = "oceny/" + subject_to_add + ".txt"
        file = open(path,"a")
        file.write(grade_to_add)
        file.write("\n")
        file.close()