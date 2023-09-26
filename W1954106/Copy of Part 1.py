# I declare that my work contains no examples of misconduct,such as plagiarism,or collusion
# Student ID-20221069|w1954106
# Date-2022/12
Progress_count = ModuleTrailer_count = ModuleRetriever_count = Exclude_count = Total = 0

def Outcomes():
    global Progress_count
    global ModuleTrailer_count
    global ModuleRetriever_count
    global Exclude_count
    
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
            break

        elif credit_pass_level == 100:
            ModuleTrailer_count = ModuleTrailer_count + 1
            print("Progress (module trailer)")
            break

        elif credit_pass_level + credit_defer_level <= 40:
            Exclude_count = Exclude_count + 1
            print("Exclude")
            break
        
        else:
            ModuleRetriever_count = ModuleRetriever_count + 1
            print("Do not Progress-Module Retreiver")
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


def QuitContinue():
    print("Would you like to enter another set of data?")
    selection = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
    if selection == "q":
        Histogram()
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

while True:
    if Option == 1:
        Outcomes()
        Histogram()
        break
    elif Option == 2:
        Outcomes()
        QuitContinue()
        break








      
