# ECOR 1042 Lab 3 - Individual submission for student_age_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Kalid Wehbe"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101259994"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-058"

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

        print(students)


# Do NOT include a main script in your submission
