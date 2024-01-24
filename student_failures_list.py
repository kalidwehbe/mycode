# ECOR 1042 Lab 3 - Individual submission for student_failures_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Kalid Wehbe"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101259994"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-058"

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

        print(students)


student_failures_list('student-mat.csv', 0)

# Do NOT include a main script in your submission
