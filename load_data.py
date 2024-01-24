# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Kalid, Caleb, Alexander, Illham"

# Update "" with your team (e.g. T102)
__team__ = "T058"

#==========================================#
# Place your student_school_list function after this line

def student_school_list(file_name, school_name):
    
    """
    Puts all the students in the school into a list from the excel file
    
    Precondition: excel file ==  file_name and school_name == type string
    
    Examples:
    
    >>> student_school_list('student-mat.csv','GP')
    
    [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3, 'Absences': 6,
    
    'G1' : 5, 'G2' : 6, 'G3': 6}, {next student} ... {last student} ]
    
    """
    
    students = []
    


    with open(file_name, 'r') as f:
        
        lines = f.readlines()

        header = lines[0].strip().split(',')

        for line in lines[1:]:

            row = line.strip().split(',')

            if row[0] == school_name:

                student = {}

                for i in range(1, len(row)):

                    student[header[i]] = (row[i])

                students.append(student)
                
                for student in students:

                    student["Age"] = int(student["Age"])
                    student["StudyTime"] = int(student["StudyTime"])
                    student["Failures"] = int(student["Failures"])
                    student["Health"] = int(student["Health"])
                    student["Absences"] = int(student["Absences"])
                    student["G1"] = int(student["G1"])
                    student["G2"] = int(student["G2"])
                    student["G3"] = int(student["G3"])

        return students


#==========================================#
# Place your student_health_list function after this line

def student_health_list(file_name, health_score):
    
    """
    Puts all the students with the same health score into a list from the excel file
    
    Precondition: excel file ==  file_name and health_score == type int
    
    Examples:
    
    >>> student_health_list('student-mat.csv', 2)
    
    [ {'School': 'MS', 'Age': 20, 'StudyTime': 1.2, 'Failures': 1, 'Absences': 10,
    
    'G1': 9, 'G2': 11, 'G3': 7}, {another element}, ...]

    """
    
    students = []

    with open(file_name, 'r') as f:

        lines = f.readlines()

        header = lines[0].strip().split(',')

        for line in lines[1:]:

            row = line.strip().split(',')

            if int(row[4]) == health_score:

                student = {}

                for i in range(len(row)):

                    if header[i] == "Health":

                        i = i + 1

                    else:

                        student[header[i]] = row[i]

                students.append(student)
                
                student["Age"] = int(student["Age"])
                student["StudyTime"] = int(student["StudyTime"])
                student["Failures"] = int(student["Failures"])
                student["Absences"] = int(student["Absences"])
                student["G1"] = int(student["G1"])
                student["G2"] = int(student["G2"])
                student["G3"] = int(student["G3"])                

        return students

#==========================================#
# Place your student_age_list function after this line

def student_age_list(file_name, age):

    """
    Puts all the students with the same age into a list from the excel file
    
    Precondition: excel file ==  file_name and age == type int
    
    Examples:
    
    >>> student_age_list('student-mat.csv', 15)
    
    [ {'School': 'GP', 'StudyTime': 4.2, 'Failures': 3, 'Health': 3, 'Absences': 6,
    
    'G1': 7, 'G2': 8, 'G3': 10}, {another element}, ... ]


    """
    
    students = []

    with open(file_name, 'r') as f:

        lines = f.readlines()
        


        header = lines[0].strip().split(',')

        for line in lines[1:]:

            row = line.strip().split(',')

            if int(row[1]) == age:

                student = {}

                for i in range(len(row)):

                    if header[i] == "Age":

                        i = i + 1

                    else:

                        student[header[i]] = row[i]

                students.append(student)

                student["StudyTime"] = int(student["StudyTime"])
                student["Failures"] = int(student["Failures"])
                student["Health"] = int(student["Health"])
                student["Absences"] = int(student["Absences"])
                student["G1"] = int(student["G1"])
                student["G2"] = int(student["G2"])
                student["G3"] = int(student["G3"])                

        return students

#==========================================#
# Place your student_failures_list function after this line

def student_failures_list(file_name, failures):
    
    """
    Puts all the students with the same amount of failures into a list from the excel file
    
    Precondition: excel file ==  file_name and failures == type int
    
    Examples:
    
    >>> student_school_list('student-mat.csv', 0)
    
    [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7,
    
    'G1': 12, 'G2': 13, 'G3': 14}, {another element}, ... ]
    
    """
    students = []

    with open(file_name, 'r') as f:

        lines = f.readlines()

        header = lines[0].strip().split(',')

        for line in lines[1:]:

            row = line.strip().split(',')

            if int(row[3]) == failures:

                student = {}

                for i in range(len(row)):

                    if header[i] == "Failures":

                        i = i + 1

                    else:

                        student[header[i]] = row[i]

                students.append(student)

                student["Age"] = int(student["Age"])
                student["StudyTime"] = int(student["StudyTime"])
                student["Health"] = int(student["Health"])
                student["Absences"] = int(student["Absences"])
                student["G1"] = int(student["G1"])
                student["G2"] = int(student["G2"])
                student["G3"] = int(student["G3"])

        return students
    

#==========================================#
# Place your load_data function after this line

def load_data(file_name, tup_category: tuple):


    """
    Based on user input the function displays the students that follow the 
    
    specific filters that the user inputs
    
    Preconditions: (allows to assume from lab) file_name == student-mat.csv
    
    Examples:
    
     >>> load_data('student-mat.csv', (‘Failures’, 0))

     [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3,
     
     'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}, {another element}, ... ] 
    
    
    >>> load_data('student-mat.csv', (‘All’, -1)) [ {'School': 'GP', 'Age': 18, 
    
    'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 12, 
    
    'G2': 13, 'G3': 14}, {another element}, ...] 
    
    """

    students = []

    
    if tup_category[0] == "All":
        
        with open(file_name, 'r') as f:
            
            lines = f.readlines()
    
            header = lines[0].strip().split(',')

            for line in lines[1:]:

                row = line.strip().split(',')

                student = {}

                for i in range(len(row)):

                    
                    student[header[i]] = row[i]

                students.append(student)


                student["Age"] = int(student["Age"])
                student["StudyTime"] = int(student["StudyTime"])
                student["Health"] = int(student["Health"])
                student["Failures"] = int(student["Failures"])
                student["Absences"] = int(student["Absences"])
                student["G1"] = int(student["G1"])
                student["G2"] = int(student["G2"])
                student["G3"] = int(student["G3"])


            



    elif tup_category[0] == "School":

        students = student_school_list(file_name, tup_category[1])



    elif tup_category[0] == "Age":

        students = student_age_list(file_name, int(tup_category[1]))



    elif tup_category[0] == "Failures":

        students = student_failures_list(file_name, int(tup_category[1]))



    elif tup_category[0] == "Health":

        students = student_health_list(file_name, int(tup_category[1]))

    else:

        print("Invalid value") # message on the termnal asked for in the lab

    return students

# user input

#==========================================#
# Place your add_average function after this line

def add_average(students):
    
    """
    Takes the average of the grades G1 G2 and G3 and adds it to the dictionary
    
    Preconditions: list of student dictionaries == type class list
    
    Examples: 
    
    >>> add_average([ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 
    
    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6},
    
    {another element},  ... ] )
 
    [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 
    
    'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67 }, 
    
    {another element}, ...]
    
    
    """
    
    if len(students) == 0:

        return []

    for student in students:
        
        avg_grade = (student['G1'] + student['G2'] + student['G3']) / 3

        student['G_avg'] = round(avg_grade, 2)
        if "Age" in students:
            student["Age"] = int(student["Age"])
        if "StudyTime" in students:
            student["StudyTime"] = int(student["StudyTime"])
        if "Failures" in students:
            student["Failures"] = int(student["Failures"])
        if "Health" in students:
            student["Health"] = int(student["Health"])
        
        student["Absences"] = int(student["Absences"])
        student["G1"] = int(student["G1"])
        student["G2"] = int(student["G2"])
        student["G3"] = int(student["G3"])
        student["G_avg"] = float(student["G_avg"])

    return students
    
