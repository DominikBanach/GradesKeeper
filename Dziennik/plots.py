#list with subjects names
from files import subjects

#for plots
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')

#this list store how many grades are in each category
categories = [0,0,0,0,0,0,0,0,0] 

#labels for plots
labels = ("|1, 1+|", "|2, 2-, 2+|", "|3, 3-, 3+|", "|4, 4-, 4+|", "|5, 5-, 5+|", "|6-, 6|")
labels2 = ("PLUSY [+]", "MINUSY [-]", "NP")
labels3 =("|1|", "|2|", "|3|", "|4|", "|5|", "|6|", "|+|", "|-|", "NP") 

#colors for plots
colors1 = ['red', 'blueviolet', 'gold', 'deepskyblue', 'limegreen', 'forestgreen'] 
colors2 = ['limegreen', 'crimson', 'navy'] 
colors3 = ['red', 'blueviolet', 'gold', 'deepskyblue', 'limegreen', 'forestgreen', 'limegreen', 'crimson', 'navy'] 


def count():
#this function fills "categories" list
    for i in range(9):
        categories[i] = 0 

    for i in range(len(subjects)):

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


def summary_graph():
#this function generate and show two plots about how many grades from each category user has
    win1 = plt.figure(figsize = (11,6), dpi = 100)
    win1.suptitle("Podsumowanie ocen", fontsize = 10, fontweight = "bold", y = 1)

    #1st plot
    plt.subplot(1,2,1)
    plt.title("Kołowy wykres wszystkich ocen podzielonych na kategorie:", fontsize = "small", fontweight = "semibold")
    plt.tight_layout()
    plt.axis('equal')

    plt.pie(categories[0:6], 
            colors = colors1, 
            autopct = '%1.1f%%', 
            shadow = True,
            counterclock = False)

    plt.legend(labels, loc = "lower left", title = "Oznaczenia:")

    #2nd plot
    plt.subplot(1,2,2)
    plt.title("Słupkowy wykres minusów, plusów i nieprzygotowań:", fontsize = "small", fontweight = "semibold")
    plt.ylabel("Ilość")
    plt.bar(labels2, [categories[6], categories[7], categories[8]], color = colors2)

    plt.show()

def splitted_graph():
#this functiion generate and show barplots for every subject grades
    if len(subjects) > 15:
        hs = 0.75
        height = 4
    else:
        hs = 0.41
        height = 3

    win2 = plt.figure(figsize = (12,7), dpi = 100)
    win2.suptitle("Szczegółowe wykresy ocen", fontsize = 10, fontweight = "bold", y = 1)
    plt.subplots_adjust(top = 0.95, left = 0.08, wspace = 0.29, hspace = hs, bottom = 0.05)

    for i in range(len(subjects)):

        for n in range(9):
            categories[n] = 0 

        path = "oceny/" + subjects[i] + ".txt"
        file = open(path, "r")
        grades = file.readlines()
        file.close()

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
        
        plt.subplot(5, height, i+1)
        plt.bar(labels3, categories, color = colors3)

        if len(subjects) > 15: plt.xlabel(subjects[i], fontsize = "small", fontweight = "semibold")
        else:                  plt.ylabel(subjects[i], fontsize = "x-small", fontweight = "semibold")

        if max(categories) != 0: plt.ylim(0, max(categories))
        plt.yticks(np.arange(0, max(categories) + 1, step = 1))

    plt.show()