#biblioteki
from foo import subjects
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')

categories = [0,0,0,0,0,0,0,0,0] 

labels = ("|1, 1+|", "|2, 2-, 2+|", "|3, 3-, 3+|", "|4, 4-, 4+|", "|5, 5-, 5+|", "|6-, 6|")
labels2 = ("PLUSY [+]", "MINUSY [-]", "NP")
labels3 =("|1|", "|2|", "|3|", "|4|", "|5|", "|6|", "|+|", "|-|", "NP") 

colors1 = ['red', 'blueviolet', 'gold', 'deepskyblue', 'limegreen', 'forestgreen'] 
colors2 = ['limegreen', 'crimson', 'navy'] 
colors3 = ['red', 'blueviolet', 'gold', 'deepskyblue', 'limegreen', 'forestgreen', 'limegreen', 'crimson', 'navy'] 

#------------------------------------------------------------------------------------------------------------------------
def count():

    for i in range(9):
        categories[i] = 0 

    for i, subject in enumerate(subjects):

        path = "oceny/" + subjects[i] + ".txt"
        file = open(path, "r")
        grades = file.readlines()

        for j, grade in enumerate(grades):
            grades[j] = grade.replace("\n","") 
            if grades[j] in ["1", "1+"]:       categories[0] += 1
            if grades[j] in ["2-", "2", "2+"]: categories[1] += 1
            if grades[j] in ["3-", "3", "3+"]: categories[2] += 1
            if grades[j] in ["4-", "4", "4+"]: categories[3] += 1
            if grades[j] in ["5-", "5", "5+"]: categories[4] += 1
            if grades[j] in ["6", "6-"]:       categories[5] += 1
            if grades[j] == '+':               categories[6] += 1
            if grades[j] == '-':               categories[7] += 1
            if grades[j] == 'np':              categories[8] += 1
        
        file.close()


#------------------------------------------------------------------------------------------------------------------------
def summary_graph():
    #front główny
    okno = plt.figure(figsize = (11,6), dpi = 100)
    okno.suptitle("Podsumowanie ocen", fontsize = 10, fontweight = "bold", y = 1)

    #KOŁOWY
    #nagłówek
    plt.subplot(1,2,1)

    #front
    plt.title("Kołowy wykres wszystkich ocen podzielonych na kategorie:", fontsize = "small", fontweight = "semibold")
    plt.tight_layout()
    plt.axis('equal')

    #back
    plt.pie(categories[0:6], 
            colors = colors1, 
            autopct = '%1.1f%%', 
            shadow = True,
            counterclock = False)

    plt.legend(labels, loc = "lower left", title = "Oznaczenia:")

    #SŁUPKOWY
    #nagłówek
    plt.subplot(1,2,2)

    #front
    plt.title("Słupkowy wykres minusów, plusów i nieprzygotowań:", fontsize = "small", fontweight = "semibold")
    plt.ylabel("Ilość")

    #back
    plt.bar(labels2, [categories[6], categories[7], categories[8]], color = colors2)
    
    #show
    plt.show()

#------------------------------------------------------------------------------------------------------------------------
def splitted_graph():

    #front główny
    okno2 = plt.figure(figsize = (12,6), dpi = 100)
    okno2.suptitle("Szczegółowe wykresy ocen", fontsize = 10, fontweight = "bold", y = 1)
    plt.subplots_adjust(top = 0.95, left = 0.08, wspace = 0.29, hspace = 0.41, bottom = 0.05)

    for i in range(len(subjects)):

        for n in range(9):
            categories[n] = 0 

        path = "oceny/" + subjects[i] + ".txt"
        file = open(path, "r")
        grades = file.readlines()

        #liczenie
        for j, grade in enumerate(grades):
            grades[j] = grade.replace("\n","")
            if grades[j] in ["1", "1+"]:       categories[0] += 1
            if grades[j] in ["2-", "2", "2+"]: categories[1] += 1
            if grades[j] in ["3-", "3", "3+"]: categories[2] += 1
            if grades[j] in ["4-", "4", "4+"]: categories[3] += 1
            if grades[j] in ["5-", "5", "5+"]: categories[4] += 1
            if grades[j] in ["6", "6-"]:       categories[5] += 1
            if grades[j] == '+':               categories[6] += 1
            if grades[j] == '-':               categories[7] += 1
            if grades[j] == 'np':              categories[8] += 1

        file.close()
        
        plt.subplot(5, 3, i+1)
        plt.bar(labels3, categories, color = colors3)
        plt.ylabel(subjects[i], fontsize = "small", fontweight = "semibold")
        plt.ylim(0, max(categories))
        plt.yticks(np.arange(0, max(categories) + 1, step = 1))

    plt.show()
