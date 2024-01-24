# ECOR 1042 Lab 3 - Individual submission for student_school_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Kalid Wehbe"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101259994"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-058"

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

        print(header)

        for line in lines[1:]:

            print(lines)

            row = line.strip().split(',')

            if row[0] == school_name:

                student = {}

                for i in range(1, len(row)):

                    student[header[i]] = (row[i])

                students.append(student)

        print(students)


student_school_list('student-mat.csv', 'GP')
# Do NOT include a main script in your submission
