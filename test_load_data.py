# ECOR 1042 Lab 4 - team submission

#import check module here

import check

#import load_data module here

import load_data

# Update "" with your the name of the active members of the team
__author__ = "Kalid, Alexander, Caleb, Ilham"

# Update "" with your student number (e.g., 100100100)

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-058"

#==========================================#

# Place test_return_list function here 
def test_return_list():
    #Complete the function with your test cases
    
    #test that student_school_list returns a list (3 different test cases required)

    check.equal(isinstance(load_data.student_school_list("student-test.csv", "GP"), list), True)
    
    # checking for GP
    
    check.equal(isinstance(load_data.student_school_list("student-test.csv", "MB"), list), True)

    # checking for MB

    check.equal(isinstance(load_data.student_school_list("student-test.csv", "GH"), list), True)
    
    # checking for a school that isn't present in the excel sheet
    
    #test that student_age_list returns a list (3 different test cases required)
    
    check.equal(isinstance(load_data.student_age_list("student-test.csv", 15), list), True)
    
    # checking for when age is 15

    check.equal(isinstance(load_data.student_age_list("student-test.csv", 18), list), True)

    # checking for when age is 18

    check.equal(isinstance(load_data.student_age_list("student-test.csv", 17), list), True)

    # checking for when age is 17
    
    #test that student_health_list returns a list (3 different test cases required)

    check.equal(isinstance(load_data.student_health_list("student-test.csv", 1), list), True)

    # checking for when health score is 1
    
    check.equal(isinstance(load_data.student_health_list("student-test.csv", 3), list), True)

    # checking for when health score is 3

    check.equal(isinstance(load_data.student_health_list("student-test.csv", 5), list), True)

    # checking for when health score is 5
    
    
    #test that student_failures_list returns a list (3 different test cases required)
    
    check.equal(isinstance(load_data.student_failures_list("student-test.csv", 3), list), True)
    
    # checking for when failures is 3
    
    check.equal(isinstance(load_data.student_failures_list("student-test.csv", 2), list), True)

    # checking for when failures is 2

    check.equal(isinstance(load_data.student_failures_list("student-test.csv", 1), list), True)

    # checking for when failures is 1
    
    
    #test that load_data returns a list (6 different test cases required)

    check.equal(isinstance(load_data.load_data("student-test.csv", ("All", -1)), list), True)

    # testing ALL list

    check.equal(isinstance(load_data.load_data("student-test.csv", ("School", "GP")), list), True)
    
    # testing school list
    
    check.equal(isinstance(load_data.load_data("student-test.csv", ("Age", "19")), list), True)

    # testing age list

    check.equal(isinstance(load_data.load_data("student-test.csv", ("Failures", "0")), list), True)

    # testing failures list
    
    check.equal(isinstance(load_data.load_data("student-test.csv", ("Health", "4")), list), True)

    # testing health list

    check.equal(isinstance(load_data.load_data("student-test.csv", ("School", "GL")), list), True)

    # testing empty list non found school in excel sheet

    #test that add_average returns a list (3 different test cases required)
    
    check.equal(isinstance(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}]), list), True)
    
    # a student with these stats

    check.equal(isinstance(load_data.add_average([{'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}]), list), True)

    # another student

    check.equal(isinstance(load_data.add_average([]), list), True)

    # a empty list
  

    check.summary()

# Place test_return_list_correct_lenght function here


def test_return_list_correct_lenght():
    #Complete the function with your test cases
    
    #test that student_school_list returns a list with the correct lenght (3 different test cases required)

    check.equal(len(load_data.student_school_list("student-test.csv", "GP")), 3)
    
    check.equal(len(load_data.student_school_list("student-test.csv", "MS")), 4)

    check.equal(len(load_data.student_school_list("student-test.csv", "BD")), 3)

    #test that student_age_list returns a list  with the correct lenght (3 different test cases required)

    check.equal(len(load_data.student_age_list("student-test.csv", 14)), 0)

    check.equal(len(load_data.student_age_list("student-test.csv", 18)), 4)

    check.equal(len(load_data.student_age_list("student-test.csv", 17)), 6)

    #test that student_health_list returns a list  with the correct lenght (3 different test cases required)

    check.equal(len(load_data.student_health_list("student-test.csv", 2)), 0)

    check.equal(len(load_data.student_health_list("student-test.csv", 1)), 1)

    check.equal(len(load_data.student_health_list("student-test.csv", 3)), 8)

    #test that student_failures_list returns a list   with the correct lenght(3 different test cases required)

    check.equal(len(load_data.student_failures_list("student-test.csv", 1)), 1)

    check.equal(len(load_data.student_failures_list("student-test.csv", 3)), 1)

    check.equal(len(load_data.student_failures_list("student-test.csv", 5)), 0)
    
    #test that load_data returns a list  with the correct lenght (6 different test cases required)

    check.equal(len(load_data.load_data("student-test.csv", ("All",))), 15)

    check.equal(len(load_data.load_data("student-test.csv", ("School", "GP"))), 3)

    check.equal(len(load_data.load_data("student-test.csv", ("Age", 15))), 3)

    check.equal(len(load_data.load_data("student-test.csv", ("Failures", 0))), 11)

    check.equal(len(load_data.load_data("student-test.csv", ("Health", 2))), 0)

    check.equal(len(load_data.load_data("student-test.csv", ("School", "CF"))), 3)

     #test that add_average returns a list   with the correct lenght (3 different test cases required)

    check.equal(len(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures':

    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}])), 1)

    check.equal(len(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures':

    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])), 3)

    check.equal(len(load_data.add_average([])), 0)

    check.summary()


#Place test_return_correct_dict_inside_list function here

def test_return_correct_dict_inside_list():
    #Complete the function with your test cases
    #test that student_school_list returns a correct dictionary inside the list (3 different test cases required)

    check.equal(load_data.student_school_list("student-test.csv", "GP")[0], {'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})

    check.equal(load_data.student_school_list("student-test.csv", "GP")[-1], {'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})

    check.equal(load_data.student_school_list("student-test.csv", "MS")[0], {'Age': 17, 'StudyTime': 1, 'Failures': 0, 'Health': 4, 'Absences': 8, 'G1': 11, 'G2': 10, 'G3': 10})

    #test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)

    check.equal(load_data.student_age_list("student-test.csv", 15)[0], {'School': 'GP', 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})

    check.equal(load_data.student_age_list("student-test.csv", 15)[-1], {'School': 'CF', 'StudyTime': 5, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7})
    
    check.equal(load_data.student_age_list("student-test.csv", 18)[0], {'School': 'GP', 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})

    #test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
    
    check.equal(load_data.student_health_list("student-test.csv", 3)[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})

    check.equal(load_data.student_health_list("student-test.csv", 3)[-1], {'School': 'BD', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12})

    check.equal(load_data.student_health_list("student-test.csv", 1)[0], {'School': 'MS', 'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9})
    
    #test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    
    check.equal(load_data.student_failures_list("student-test.csv", 0)[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})

    check.equal(load_data.student_failures_list("student-test.csv", 0)[-1], {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})

    check.equal(load_data.student_failures_list("student-test.csv", 1)[0], {'School': 'CF', 'Age': 16, 'StudyTime': 2, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12})
    
    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
    
    check.equal(load_data.load_data("student-test.csv", ("All", -1))[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    
    check.equal(load_data.load_data("student-test.csv", ("All", -1))[-1], {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})

    check.equal(load_data.load_data("student-test.csv", ("School", "GP"))[-1], {'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})

    check.equal(load_data.load_data("student-test.csv", ("Age", 17))[0], {'School': 'GP', 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6})
    
    check.equal(load_data.load_data("student-test.csv", ("Health", 1))[-1], {'School': 'MS', 'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9})

    check.equal(load_data.load_data("student-test.csv", ("Failures", 2))[-1], {'School': 'CF', 'Age': 17, 'StudyTime': 1, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0})
    
    #test that add_average returns a lcorrect dictionary inside the list  (3 different test cases required)

    check.equal(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures':

    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}])[0], {'School': 'GP', 'Age': 18, 'StudyTime': 6, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6, 'G_avg': 5.67})

    check.equal(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures':

    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])[-1], {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8, 'G_avg': 8.33})

    check.equal(load_data.add_average([{'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}])[0], {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5, 'G_avg': 5.0})
    
    check.summary()
    
    

# Do NOT include a main script in your submission


#Place test_add_average function here

def test_add_average():
    #Complete the function with your test cases

    #test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)

    check.equal(len(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures':

    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}])), len([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures':

    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}]))

    check.equal(len(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures':

    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])), len([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures':

    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}]))

    check.equal(len(load_data.add_average([{'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}])), len([{'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}]))

    check.equal(len(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])), len([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}]))
    
    check.equal(len(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])), len([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}]))    

    #test that the function returns an empty list when it is called whith an empty list

    check.equal(load_data.add_average([]), [])

    #test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)
    
    check.equal(len(load_data.add_average([{'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}])[0]), len([{'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}][0]) + 1)
    
    check.equal(len(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures':

    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])[0]), len([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures':

    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}][0]) + 1)
    
    check.equal(len(load_data.add_average([{'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}])[-1]), len([{'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}][-1]) + 1)
    
    check.equal(len(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures':

    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])[-1]), len([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures':

    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}][-1]) + 1)

    check.equal(len(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures':

    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])[1]), len([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures':

    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}][1]) + 1)       

    #test that the G_Avg value is properly calculated  (5 different test cases required)
    
    check.equal(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

        'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}])[0]["G_avg"], 5.67)

    check.equal(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

        'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}])[0]["G_avg"], 5.67)

    check.equal(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

        'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}])[-1]["G_avg"], 5.0)

    check.equal(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

        'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])[-1]["G_avg"], 8.33)

    check.equal(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

        'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,

    'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5,

    'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])[1]["G_avg"], 5.0)

    check.summary()

# Do NOT include a main script in your submission
