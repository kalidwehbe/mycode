# ECOR 1042 Lab 3 - Individual submission for student_health_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Kalid Wehbe"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101259994"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-058"

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

        print(students)


student_health_list('student-mat.csv', 2)


# Do NOT include a main script in your submission
