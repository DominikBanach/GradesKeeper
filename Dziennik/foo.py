#biblioteki
import os.path
from os import system

#------------------------------------------------------------------------------------------------------------------------
#przedmioty
subjects = ("matematyka","fizyka","geografia", "chemia", "biologia", "j.polski", "j.angielski",
              "j.niemiecki", "informatyka", "wos", "historia", "edb", "wf", "plastyka", "religia")

#dostępne oceny
acceptable_grades = ("1", "2", "3", "4", "5", "6", "1-", "1+", "2-", "0pkt", "1pkt", "2pkt", "3pkt",
                     "2+", "3-", "3+", "4-", "4+", "5-", "5+", "6-", "6+", "-", "+", "np")

#------------------------------------------------------------------------------------------------------------------------
#menu programu
def menu():
    print("--------------------            DZIENNIK OCEN             -------------------")
    print("--------------------  1 -> Zobacz oceny                   -------------------")
    print("--------------------  2 -> Dodaj oceny                    -------------------")
    print("--------------------  3 -> Wykres ocen                    -------------------")
    print("--------------------  4 -> Zeruj oceny                    -------------------")
    print("--------------------  5 -> Automatyczna aktualizacja      -------------------")
    print("--------------------  6 -> Przełącz konto w dzienniku     -------------------")
    print("--------------------  7 -> Wyjście                        -------------------")
    return input("Wybierz cyfrę:")

#------------------------------------------------------------------------------------------------------------------------
#resetowanie ocen
def reset():
    for i in range(len(subjects)):
        path = "oceny/" + subjects[i] + ".txt"
        file = open(path, "w")
        file.close()

#------------------------------------------------------------------------------------------------------------------------
#lista przedmiotów
def subjects_list():
    print("Oto lista przedmiotów:")
    for i,subject in enumerate(subjects):
        print(i+1,".",subject, sep='')

#------------------------------------------------------------------------------------------------------------------------
#pokazuje liste przedmiotów wraz z ocenami
def grades_list():

    print("Oto lista ocen:")
    for i, subject in enumerate(subjects):
        path = "oceny/" + subjects[i] + ".txt"
        file = open(path, "r")
        grades = file.readlines()

        for j, grade in enumerate(grades):
            grades[j] = grade.replace("\n","")

        print(subjects[i] + ":", grades, sep='')

        file.close()

#------------------------------------------------------------------------------------------------------------------------
#dodaj podaną ilość ocen do plików
def add_grades(ile):

    for i in range(ile):

        system("cls")
        subjects_list()

        #sprawdzenie czy podana wartosc to numer z oczekiwanego przedzialu
        try:

            nr = int(input("Wybierz numer przedmiotu do którego chcesz dodać ocenę:"))

            if int(nr) > len(subjects) or int(nr) < 1:
                input("Brak opcji o podanym numerze! ENTER by kontynuować...")
                continue

        except ValueError:
            input("Podana wartość nie jest numerem! ENTER by kontynuować...")
            continue

        grade = input("Podaj ocenę:")

        if grade in acceptable_grades:
            path = "oceny/" + subjects[nr-1] + ".txt"
            file = open(path,"a")
            file.write(grade)
            file.write("\n")
            file.close()

        if not grade in acceptable_grades:
            input("Nie można zapisać takiej oceny! ENTER by kontynuować...")
            continue

#------------------------------------------------------------------------------------------------------------------------
#tworzy pliki i folder oceny jesli nie istnieją
def create_files():

    if not os.path.isdir("oceny"):
        os.makedirs("oceny")

    for subject in subjects:
        name = subject + ".txt"
        path = "oceny/" + name

        if not os.path.isfile(path):
            open(path, "a+").close()
