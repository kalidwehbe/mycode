# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Kalid Alex Alham Caleb"

# Update "" with your team (e.g. T102)
__team__ = "T058"

#==========================================#
# Place your sort_students_age_bubble function after this line

def sort_students_age_bubble(students: list, order) -> list:


    """
    
    This function sorts students list in ascending or descending order based on there Age. 
    
    If the Age key is not in the dictionary the function will print out a statement.
    
    Preconditions: order = A or D
    
    Examples:
    
    >>> sort_students_age_bubble([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "D")


    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]
    
    >>> sort_students_age_bubble([{"Age":20,"School":"GP"},{"Age":19,"School":"MS"}], "A")


    [{"Age": 19, "School":"MS"}, {"Age":20, "School":"GP"}]
    
    
    >>> sort_students_age_bubble([{"School":"GP"}, {"School":"MS"}], "D")
    
    "Age" key is not present.
    
    [{"School":"GP"}, {"School":"MS"}]


    """

    n = len(students)

    while True:
        
        swapped = False

        for i in range(n-1):
            
            if "Age" in students[i] and "Age" in students[i+1]:

                if order == "A":
                    
                    if students[i]["Age"] > students[i+1]["Age"]:

                        students[i], students[i+1] = students[i+1], students[i]

                        swapped = True
                        
                elif order == "D":

                    if students[i]["Age"] < students[i+1]["Age"]:
                        
                        students[i], students[i + 1] = students[i + 1], students[i]
                        
                        swapped = True
                else:
                    print("Invalid order parameter. Please enter 'A' for ascending or 'D' for descending.")
                    return students
            else:
                print("Error: key 'Age' not found in the list of students")
                
                return students
            
        if not swapped:
            
            break
        
    return students

#==========================================#
# Place your sort_students_time_selection function after this line

def sort_students_time_selection(students_list: list, order: str) -> list:

    for i in range(len(students_list)):
      
        if "StudyTime" in students_list[i]:
         
            for j in range(i + 1, len(students_list)):
            
                if "StudyTime" in students_list[j]:
               
                    if order == "A":
                  
                        if students_list[j]["StudyTime"] < students_list[i]["StudyTime"]:
                              
                            students_list[i], students_list[j] = students_list[j], students_list[i]
                                              
                        elif order == "D":
                            
                            if students_list[j]["StudyTime"] > students_list[i]["StudyTime"]:
                                        
                                    students_list[i], students_list[j] = students_list[j], students_list[i]
                                                 
                            else:
                                       
                                    print("Invalid order parameter. Please enter 'A' for ascending or 'D' for descending.")
                                                 
                                    return students_list
                        else:
                            print("StudyTime key is not present.")
                            return students_list
                
                return students_list
      


#==========================================#
# Place your sort_students_g_avg_insertion function after this line
def sort_students_g_avg_insertion(list_of_students: list, order_type:str) -> list:

    """
    Sorts list using insertion sort
    
    Precondition order = A or D
    
    Example: 
    
    >>>sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}], "D")
    [{"G_Avg": 9.1, "School":"MS"}, {"G_Avg":7.2, "School":"GP"}]
    """
    m = len(list_of_students)
    for i in range(0, m):
        if 'G_Avg' not in list_of_students[i]:
            print('the key is not in the dictionary')        
        else:
            if order_type == 'D':
                if (n := len(list_of_students)) <= 1:
                    return
                for i in range(1, n):             
                    key = list_of_students[i]['G_Avg']
                    j = i-1
                    while j >=0 and key > (list_of_students[j]['G_Avg']):
                        list_of_students[j+1]['G_Avg'] = list_of_students[j]['G_Avg']
                        j -= 1  
                        list_of_students[j+1]['G_Avg'] = key
                
            if order_type == 'A':
                if (n := len(list_of_students)) <= 1:
                    return 
                for i in range(1, n):             
                    key = list_of_students[i]['G_Avg']
                    j = i-1 
                    while j >=0 and key < (list_of_students[j]['G_Avg']):
                        list_of_students[j+1]['G_Avg'] = list_of_students[j]['G_Avg']
                        j -= 1
                        list_of_students[j+1]['G_Avg'] = key  

    return list_of_students  

#==========================================#
# Place your sort_students_failures_bubble function after this line

def sort_students_failures_bubble(students: list, order) -> list:
    """

    This function sorts students list in ascending or descending order based on there Age. 
    
    If the Age key is not in the dictionary the function will print out a statement.
    
    Preconditions: order = A or D
    
    Examples:
    
   


    """

    n = len(students)

    while True:
        
        swapped = False

        for i in range(n-1):
            
            if "Failures" in students[i] and "Failures" in students[i + 1]:

                if order == "A":
                    
                    if students[i]["Failures"] > students[i + 1]["Failures"]:

                        students[i], students[i+1] = students[i+1], students[i]

                        swapped = True
                        
                elif order == "D":

                    if students[i]["Failures"] < students[i + 1]["Failures"]:
                        
                        students[i], students[i + 1] = students[i + 1], students[i]
                        
                        swapped = True
                else:
                    print("Invalid order parameter. Please enter 'A' for ascending or 'D' for descending.")
                    return students
            else:
                print("Error: key 'Failures' not found in the list of students")
                
                return students
            
        if not swapped:
            
            break
        
    return students

#==========================================#
# Place your sort function after this line

def sort(student_list: list, order: str, sorting_type: str) -> list:
    
    """
    Lets the user decide what to sort in the list of dictionaries
    
    Precondition: order = A or D 
    
    Examples:
    
    >>>sort([{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}],"D","Age")
    
    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]
    
    >>>sort([{"School":"GP"},{"School":"MS"}], "D", "School")
    
    Cannot be sorted by "School"
    
    [{"School":"GP"}, {"School":"MS"}]
    
    """
    
    if sorting_type == "Age":
        
        sort_students_age_bubble(student_list, order)
        
    elif sorting_type == "Failures":
    
        sort_students_failures_bubble(student_list, order)
    
    elif sorting_type == "G_avg":
        
        sort_students_g_avg_insertion(student_list, order)
        
    elif sorting_type == "StudyTime":
        
        sort_students_time_selection(student_list, order)
        
    else:
        
        print('Cannot be sorted by "'+ sorting_type + '"')
        
    return student_list        

# Do NOT include a main script in your submission
