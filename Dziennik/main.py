from files import *
from plots import *
from api import *

from os import system
from os import path
from vulcan._utils import VulcanAPIException

def menu():
    print("--------------------            DZIENNIK OCEN                -------------------")
    print("--------------------  1 -> Zobacz oceny w formie tekstu      -------------------")
    print("--------------------  2 -> Zobacz wykresy ocen               -------------------")
    print("--------------------  3 -> Zeruj stan zapisu                 -------------------")
    print("--------------------  4 -> Automatyczna aktualizacja ocen    -------------------")
    print("--------------------  5 -> Przełącz konto w dzienniku        -------------------")
    print("--------------------  6 -> Wyjście                           -------------------")
    return input("Wybierz cyfrę:")


connection = False
if os.path.isfile("cert.json"): connection = True

create_files()

if connection == False:

    print("Witaj w aplikacji GradesKeeper!")
    print("Połącz swoje konto w dzienniku Vulcan z aplikacją. W tym celu kieruj się poniższą instrukcją:")
    print("1) Wejdź w dzienniku w zakładkę dostęp mobilny i wygeneruj kod.")
    print("2) Jeśli jest już tam dodane 'Vulcan API' to usuń urządzenie o tej nazwie.")
    print("3) Przepisz dokładnie trzy ważne ciągi znaków: TOKEN, SYMBOL i PIN.")

    token   =  input("wpisz token:")
    symbol  =  input("wpisz symbol:")
    pin     =  input("wpisz PIN:")

    try: 
        new_acc(token, symbol, pin)
        connection = True
        reset()
        update_grades()

    except VulcanAPIException:
        print("Błędne dane lub problem z internetem!")

    input("Enter by kontynuować...")



while True:

    system("cls")
    w = menu()

    if w == "1":
        grades_list()
        input("Enter by kontynuować...")


    if w == "2":
        print("--------------------WYKRESY OCEN -------------------------------------")
        print("--------------------1.Podsumowanie wszystkich ocen -------------------")
        print("--------------------2.Wykresy przedmiotowe ---------------------------")
        w2 = input("Wybierz numer:")

        if w2 == "1":
            count()
            summary_graph()

        if w2 == "2":
            splitted_graph()

        if not w2 in ("1", "2"):
            print("Brak wybranej opcji!")
        
    
    if w == "3":
        reset()
        input("Wyzerowano stan ocen! Enter by kontynuować...")

    #
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

    
    if w == "5":

        system("cls")

        print("Witaj w aplikacji GradesKeeper!")
        print("Połącz swoje konto w dzienniku Vulcan z aplikacją. W tym celu kieruj się poniższą instrukcją:")
        print("1) Wejdź w dzienniku w zakładkę dostęp mobilny i wygeneruj kod.")
        print("2) Jeśli jest już tam dodane 'Vulcan API' to usuń urządzenie o tej nazwie.")
        print("3) Przepisz dokładnie trzy ważne ciągi znaków: TOKEN, SYMBOL i PIN.")

        token   =  input("wpisz token:")
        symbol  =  input("wpisz symbol:")
        pin     =  input("wpisz PIN:")

        system("cls")

        try: 
            new_acc(token, symbol, pin)
            connection = True
            reset()
            update_grades()

        except VulcanAPIException:
            print("Błędne dane lub problem z internetem!")

        input("Enter by kontynuować...")

    if w == "6":
        break

    if not w in ["1", "2", "3", "4", "5", "6"]:
        input("Brak podanej opcji! Enter by kontynuować...")