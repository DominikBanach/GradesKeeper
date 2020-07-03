#functions for working with files
from files import reset, grades_list, create_files

#functions for generating plots
from plots import splitted_graph, summary_graph, count

#functions for working with Vulcan
from api import new_acc, update_grades, fill_subjects_list
from vulcan._utils import VulcanAPIException

from os import system, path

def menu():
#this function prints menu and returns choosen option | no arguments, 1 return
    print("--------------------            DZIENNIK OCEN                -------------------")
    print("--------------------  1 -> Zobacz oceny w formie tekstu      -------------------")
    print("--------------------  2 -> Zobacz wykresy ocen               -------------------")
    print("--------------------  3 -> Zeruj stan zapisu                 -------------------")
    print("--------------------  4 -> Automatyczna aktualizacja ocen    -------------------")
    print("--------------------  5 -> Przełącz konto w dzienniku        -------------------")
    print("--------------------  6 -> Wyjście                           -------------------")
    return input("Wybierz cyfrę:")


connection = False

if path.isfile("cert.json"): 
#this statement is active when user have connected his Vulcan account yet, it only check user's subjects and check if files are okay
    connection = True
    fill_subjects_list()
    create_files()

if connection == False:
#this statement is active when user haven't connected his Vulcan account yet, user will connect his account here
    print("Witaj w aplikacji GradesKeeper!")
    print("Połącz swoje konto w dzienniku Vulcan z aplikacją. W tym celu kieruj się poniższą instrukcją:")
    print("1) Wejdź w dzienniku w zakładkę dostęp mobilny i wygeneruj kod.")
    print("2) Jeśli jest już tam dodane 'Vulcan API' to usuń urządzenie o tej nazwie.")
    print("3) Przepisz dokładnie trzy ważne ciągi znaków: TOKEN, SYMBOL i PIN.")

    token   =  input("Wpisz token:")
    symbol  =  input("Wpisz symbol:")
    pin     =  input("Wpisz PIN:")

    try: 
        new_acc(token, symbol, pin)
        connection = True
        fill_subjects_list()
        create_files()
        reset()
        update_grades()
        print("Udało się połączyć z dziennikiem! (oceny również zostały pobrane)")

    except VulcanAPIException:
        print("Błędne dane lub problem z internetem!")

    input("Enter by kontynuować...")


while True:
#main loop - every time it is taking number of choosen option using main(), "w" is var used to store this number

    system("cls")

    if connection == False: 
    #if account isn't connected user can't use GradesKeeper
        input("Twoje konto Vulcan nie jest połączone - uruchom program ponownie i połącz konto.\nEnter by kontynuować...")
        break

    #get option number
    w = menu()

    #1 -> Zobacz oceny w formie tekstu
    if w == "1":
        grades_list()
        input("Enter by kontynuować...")

    #2 -> Zobacz wykresy ocen
    if w == "2":
        print("--------------------            WYKRESY OCEN                  ------------------")
        print("--------------------  1 -> Podsumowanie wszystkich ocen       ------------------")
        print("--------------------  2 -> Wykresy przedmiotowe               ------------------")
        w2 = input("Wybierz numer:") 

        if w2 == "1":
            count()
            summary_graph()

        if w2 == "2":
            splitted_graph()

        if not w2 in ("1", "2"):
            print("Brak wybranej opcji!")
        
    #3 -> Zeruj stan zapisu
    if w == "3":
        reset()
        input("Wyzerowano stan ocen! Enter by kontynuować...")

    #4 -> Automatyczna aktualizacja ocen
    if w == "4":
        print("Pobieranie ocen z dziennika...")

        if connection:

            reset()

            try: 
                update_grades()
                print("Pobieranie zakończone sukcesem!")

            except VulcanAPIException: print("Błąd pobierania!")
            

        else: print("Błąd pobierania!")

        input("Enter by kontynuować...")

    #5 -> Przełącz konto w dzienniku
    if w == "5":

        system("cls")

        print("Połącz swoje konto w dzienniku Vulcan z aplikacją. W tym celu kieruj się poniższą instrukcją:")
        print("1) Wejdź w dzienniku w zakładkę dostęp mobilny i wygeneruj kod.")
        print("2) Jeśli jest już tam dodane 'Vulcan API' to usuń urządzenie o tej nazwie.")
        print("3) Przepisz dokładnie trzy ważne ciągi znaków: TOKEN, SYMBOL i PIN.")

        token   =  input("Wpisz token:")
        symbol  =  input("Wpisz symbol:")
        pin     =  input("Wpisz PIN:")

        system("cls")

        try: 
            new_acc(token, symbol, pin)
            connection = True
            fill_subjects_list()
            create_files()
            reset()
            update_grades()
            print("Udało się połączyć z dziennikiem! (oceny również zostały pobrane)")

        except VulcanAPIException:
            print("Błędne dane lub problem z internetem!")

        input("Enter by kontynuować...")

    #6 -> Wyjście 
    if w == "6": break

    #if there is no option connected with given number
    if not w in ["1", "2", "3", "4", "5", "6"]: input("Brak podanej opcji! Enter by kontynuować...")