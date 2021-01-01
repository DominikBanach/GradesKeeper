from files import subjects

from plots import average_grade_history_graph

from vulcan import Vulcan
import json, os
from datetime import date, timedelta

def change_this(string):
    changes = [['ą','a'], ["ę","e"], ['ń','n'], ['ć','c'], ['ż','z'], ['ł','l'], ['ś','s'], ['ó','o'], ['ź','z'],
                ['Ą','A'], ["Ę","E"], ['Ń','N'], ['Ć','C'], ['Ż','Z'], ['Ł','L'], ['Ś','S'], ['Ó','O'], ['Ź','Z']]   
    for change in changes: string = string.replace(change[0], change[1], string.count(change[0]))
    return string

def new_acc(token, symbol, pin):
#this function connect GradesKeeper with user's Vulcan account | 3 arguments, no returns

    if os.path.isfile("cert.json"): os.remove("cert.json")

    certificate = Vulcan.register(token, symbol, pin)
    with open("cert.json", "w") as f: json.dump(certificate.json, f)


def fill_subjects_list():
#this function uses grades list to fill "subjects" list with user's subjects name | no arguments, no returns

    with open("cert.json") as f:
        certificate = json.load(f)

    client = Vulcan(certificate)

    for grade in client.get_grades():
        if not grade.subject.short in subjects:
            subjects.append(grade.subject.short)


def update_grades():
#this function downloads grades from connected account | no arguments, no returns

    #prepare connection with Vulcan account
    with open("cert.json") as f:
        certificate = json.load(f)

    client = Vulcan(certificate)

    for grade in client.get_grades():

        #grade_to_add
        if grade.weight == 0.0: continue
        elif grade.content == "np":   grade_to_add = "np"
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
        subject_to_add = grade.subject.short

        #add grade to file
        path = "oceny/" + subject_to_add + ".txt"
        file = open(path,"a")
        file.write(grade_to_add)
        file.write("\n")
        file.close()

def prepare_average_grade_graph():
#this function prepares data for this plot and calls function for api.py to make it | no arguments, no returns

    #prepare connection with Vulcan account
    with open("cert.json") as f:
        certificate = json.load(f)

    client = Vulcan(certificate)

    values = [] 
    dates = []
    components = []
    weights = []

    for grade in client.get_grades():

        if ((grade.weight == 0.0) or (grade.value == None) or (grade.value == 0.0)): continue
        else: 
            components.append(grade.value * grade.weight)
            weights.append(grade.weight)
            values.append(round(sum(components) / sum(weights), 2))
            dates.append(str(grade.date.month) + "." + str(grade.date.day))

    average_grade_history_graph(dates, values)

def update_mailbox():
#this function updates data about recived messages | no arguments, no returns

    if os.path.isdir("messages"):
        for file in os.listdir("messages"):
            os.remove(f"messages/{file}")
        os.rmdir("messages")

    if not os.path.isdir("messages"):
        os.makedirs("messages")

    with open("cert.json") as f:
        certificate = json.load(f)

    client = Vulcan(certificate)

    for msg in client.get_messages():
        teacher = msg.sender
        content = change_this(msg.content)
        title = change_this(msg.title)
        date = str(msg.sent_date) + " " + str(msg.sent_time).replace(":", ".", 3)
        try: teacher_name = change_this(teacher.first_name) + " " + change_this(teacher.last_name)
        except AttributeError: continue
        
        path = "messages/" + date + ".txt"
        file = open(path,"a")
        try: file.write(f"'{title}'\nOd: {teacher_name}\n{date}\n\n{content}")
        except UnicodeEncodeError: continue
        file.close()

def prepare_exams():
#this function prepares txt file with exams info inside | no arguments, no returns

    #prepare connection with Vulcan account
    with open("cert.json") as f:
        certificate = json.load(f)

    client = Vulcan(certificate)

    exams = []

    for i in range(18):
        for exam in client.get_exams(date.today() + timedelta(i)):
            exams.append(exam)

    file = open("exams.txt","w")
    file.write("Najblizsze sprawdziany:\n")  

    for exam in exams:

        name = change_this(exam.subject.name)
        description = change_this(exam.description)

        file.write(f"    -{name}, dnia {exam.date}: {description}\n")
        
    file.close()

def prepare_plan():
#this function prepares txt files with plans for days of the week inside | no arguments, no returns

    if os.path.isdir("plan"):
        for file in os.listdir("plan"):
            os.remove(f"plan/{file}")
        os.rmdir("plan")

    if not os.path.isdir("plan"):
        os.makedirs("plan")   

    #prepare connection with Vulcan account
    with open("cert.json") as f:
        certificate = json.load(f)

    client = Vulcan(certificate)

    last_num = 0
    data = ""
    day_name = ""

    for i in range(7):

        free = True
        data = date.today() + timedelta(i)
        
        if data.weekday() == 0: day_name = "poniedzialek"
        if data.weekday() == 1: day_name = "wtorek"
        if data.weekday() == 2: day_name = "sroda"
        if data.weekday() == 3: day_name = "czwartek"
        if data.weekday() == 4: day_name = "piatek"
        if data.weekday() in (5,6): continue

        file = open(f"plan/{day_name}.txt","w+")
        file.write(f"Plan na {day_name}:") 

        for lesson in client.get_lessons(data):

            free = False

            if ((last_num == 0) and (lesson.number > 1)): last_num = lesson.number - 1

            lesson_name = change_this(lesson.subject.name)
            teacher_name = change_this(lesson.teacher.short) 

            if lesson.number != last_num: 
                file.write(f"\n{lesson.number}. {lesson_name} ({teacher_name})")
                last_num += 1
            
            else: 
                file.write(f" / {lesson_name} ({teacher_name})")
            
        last_num = 0

        file.close()

        if free: 
            new_file = open(f"plan/{day_name}.txt","w")
            new_file.write(f"Brak lekcji na {day_name}!!! WOLNE!!!")
            new_file.close()
            