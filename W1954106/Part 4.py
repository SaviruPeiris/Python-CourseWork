# I declare that my work contains no examples of misconduct,such as plagiarism,or collusion
# Student ID-20221069|w1954106
# Date-2022/12/

Progress_count = ModuleTrailer_count = ModuleRetriever_count = Exclude_count = Total = 0
total_list = []
conti_no='yes'
Dict = {}

def Outcomes():
    global Progress_count
    global ModuleTrailer_count
    global ModuleRetriever_count
    global Exclude_count

    Student_ID=input("Enter the Student ID:")
    while True:
        while True:
            try:
                credit_pass_level = int(input("Please enter your credits at pass: "))
                if credit_pass_level not in range(0, 121, 20):
                    print("Out of range")
                else:
                    break
            except ValueError:
                print("Integer required")
                continue
        while True:
            try:
                credit_defer_level = int(input("Please enter your credits at defer: "))
                if credit_defer_level not in range(0, 121, 20):
                    print("Out of range")
                else:
                    break
            except ValueError:
                print("Integer required")
                continue
        while True:
            try:
                credit_fail_level = int(input("Please enter your credits at fail: "))
                if credit_fail_level not in range(0, 121, 20):
                    print("Out of range")
                else:
                    break
            except ValueError:
                print("Integer required")
                continue

        if credit_pass_level + credit_defer_level + credit_fail_level != 120:
            print("Total incorrect")
            continue

        elif credit_pass_level == 120:
            Progress_count = Progress_count + 1
            print("Progress")
            line = "Progress" + " - " + str(credit_pass_level) + ' , ' + str(credit_defer_level) + ' , ' + str(
                credit_fail_level)
            total_list.append(line)
            Dict[Student_ID] = line
            break


        elif credit_pass_level == 100:
            ModuleTrailer_count = ModuleTrailer_count + 1
            print("Progress (module trailer)")
            line = "Progress (module trailer)" + " - " + str(credit_pass_level) + ' , ' + str(
                credit_defer_level) + ' , ' + str(credit_fail_level)
            total_list.append(line)
            Dict[Student_ID] = line
            break


        elif credit_pass_level + credit_defer_level <= 40:
            Exclude_count = Exclude_count + 1
            print("Exclude")
            line = "Exclude" + " - " + str(credit_pass_level) + ' , ' + str(credit_defer_level) + ' , ' + str(
                credit_fail_level)
            total_list.append(line)
            Dict[Student_ID] = line
            break

        else:
            ModuleRetriever_count = ModuleRetriever_count + 1
            print("Module retriever")
            line = "Module retriever" + " - " + str(credit_pass_level) + ' , ' + str(credit_defer_level) + ' , ' + str(
                credit_fail_level)
            total_list.append(line)
            Dict[Student_ID] = line
            break
        

def Histogram():
    Total = Progress_count + ModuleTrailer_count + ModuleRetriever_count + Exclude_count
    print("-" * 80)
    print("Histogram")
    print("Progress", Progress_count, "  :", '*' * Progress_count)
    print("Trailer", ModuleTrailer_count, "   :", '*' * ModuleTrailer_count)
    print("Retriever", ModuleRetriever_count, " :", '*' * ModuleRetriever_count)
    print("Excluded", Exclude_count, "  :", '*' * Exclude_count)
    print(Total, "outcomes in total.")
    print("-" * 80)


def lists():
    global total_list
    print("\nPart 2")
    for x in total_list:
        print(x)
    print('-' * 80)
    

def text_files():
    print("\nPart 3")
    global total_list
    A1 = open("Progression.txt", "w")  # opens file "Progression.txt" in write and read only
    for x in range(0, len(total_list)):
        A1.write(total_list[x])
        A1.write('\n')
        
    A1 = open("Progression.txt", "r")
    progression_file_content = A1.read()
    print(progression_file_content)
    A1.close()
    print('-' * 80)
    

# Part 4 - Dictionary (extension)
def Dictionary():
    print("\nPart 4")
    for key, value in Dict.items():
        print(key, ' : ', value)


def QuitContinue():
    print("Would you like to enter another set of data?")
    selection = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
    if selection == "q":
        Histogram()
        lists()
        text_files()
        Dictionary()

    elif selection == "y":
        Outcomes()
        QuitContinue()
    else:
        print('Invalid Option')
        QuitContinue()
        
        
Option = int(input('Enter "1" for Student or Enter "2" for Staff Member:'))
while Option != 1 and Option != 2:
    try:
        Option = int(input('Invalid Career Option\nEnter "1" for Student or Enter "2" for Staff Member:'))
    except ValueError:
        print("Interger Required")
        continue

    
'''def Student_ID():               ###
    global Student_ID
    Student_ID = input('Enter your Student ID:')
    if Student_ID in Dict:
        print('The Student ID is already exist do you wish to add another Students detail:')
        Answer=input('Enter "yes" or "No":').lower()
        if Answer=='yes':
            Outcomes()
        elif Answer=='no':
            Histogram()
            lists()
            text_files()
            Dictionary()
        else:
            print('Invalid Option')'''

while True:
    if Option == 1:
        Outcomes()
        Histogram()
        lists()
        text_files()
        Dictionary()
        break
    elif Option == 2:
        Outcomes()
        QuitContinue() 
        break

'''def Validation():
    while conti_no.lower()=='yes':
        ID = input('Enter your Student ID:')
        if ID in Dict:
            print('The student ID is already exist do you wish to add another Students detail:')
            Answer=input('Enter "yes" or "No":').lower()
            if Answer=='yes':
                Outcomes()
            elif Answer=='no':
                Histogram()
                lists()
                text_files()
                Dictionary()
            else:
                print('Invalid Option')'''
        
