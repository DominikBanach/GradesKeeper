#import
from foo import *
from foo2 import *
from foo3 import *
from os import system
from vulcan._utils import VulcanAPIException

connection = False

#tworzy pliki jesli nie istnieją----------------------------------------------------------------------
create_files()

if os.path.isfile("cert.json"): 
    connection = True

else: 
    print("jeśli używasz aplikacji po raz pierwszy i/lub nie połączyłeś jej ze swoim dziennikiem możesz to zrobić wybierając opcję nr6")
    print("w przeciwnym wypadku nie będzie możliwe pobieranie ocen")
    input("Enter by kontynuować...")

while True:

    system("cls")

    #--- menu wyboru ---------------------------------------------------------------------------------------------------
    w = menu()

    #--- wypisanie ocen ------------------------------------------------------------------------------------------------
    if w == "1":
        grades_list()
        input("Enter by kontynuować...")

    #--- dodawanie ocen ------------------------------------------------------------------------------------------------
    if w == "2":

        try:
            x = int(input("Ile ocen zamierzasz dodać:"))
            add_grades(x)

        except ValueError:
            input("Podana wartość nie jest numerem! ENTER by kontynuować...")
            continue


    #--- wykresy -------------------------------------------------------------------------------------------------------
    if w == "3":
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
        
    #--- zerowanie ocen ------------------------------------------------------------------------------------------------
    if w == "4":
        reset()
        input("Wyzerowano stan ocen! Enter by kontynuować...")

    #--- automatyczna aktualizacja -------------------------------------------------------------------------------------
    if w == "5":
        print("Pobieranie ocen z dziennika...")

        if connection:

            reset()

            try: 
                update_grades()
                print("Pobieranie zakończone sukcesem!")

            except VulcanAPIException: print("Błąd pobierania - prawdopodobnie nie połączyłeś swojego konta z aplikacją (możliwe przy pomocy opcji nr6)")
            

        else: print("Błąd pobierania - prawdopodobnie nie połączyłeś swojego konta z aplikacją (możliwe przy pomocy opcji nr6)")

        input("Enter by kontynuować...")

    #--- zmiana konta-------------------------------------------------------------------------------------------------------
    if w == "6":

        system("cls")

        print("zgodnie z instrukcją dodaj aplikację jako urządzenie mobilne:")
        print("1.Wejdź w dzienniku w zakładkę dostęp mobilny i wygeneruj kod")
        print("1.2 Jeśli jest już tam dodane Vulcan API to usuń urządzenie o tej nazwie")
        print("2.przepisz dokładnie trzy ważne ciągi znaków: TOKEN, SYMBOL i PIN")
        input("Enter by kontynuować...")

        system("cls")

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
            print("Podano błędne dane!")

        input("Enter by kontynuować...")

    #--- wyjście -------------------------------------------------------------------------------------------------------
    if w == "7":
        print("Koniec działania programu...")
        break

    #--- brak wybranej opcji -------------------------------------------------------------------------------------------
    if not w in ["1", "2", "3", "4", "5", "6", "7"]:
        input("Brak podanej opcji! Enter by kontynuować...")