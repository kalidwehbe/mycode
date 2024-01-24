# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = ""

# Update "" with your student number (e.g., 100100100)
__student_number__ = ""

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = ""

#==========================================#
# Place your script for your batch_UI after this line

import string
import load_data as ld
import sort as st
import curve_fit as cr
import histogram as hs

lst_file = []

file_name = input("Please enter the name of the file where your commands are stored: ")

file = open(file_name, "r")

for line in file:
    
    file_line = line.strip('\n').split(";")
    
    
    
    lst_file.append(file_line)
    

    

    
if "L" == lst_file[0][0]:
    
    file_name = lst_file[0][1]
    
    attribute = lst_file[0][2]
    
    value = lst_file[0][3]
    
    tup_category = (attribute, value)
    
    data = ld.load_data(file_name, (attribute, value))
    
    print("Data loaded")
    
    for i in range(1,len(lst_file)):
    
        if "S" == lst_file[i][0]:
            
            attribute = lst_file[i][1]
            
            order = lst_file[i][2]
            
            sorted_data = st.sort(data, order, attribute)
            
            print("Data sorted. ")
            
            if "Y" == lst_file[i][3]:
                
                print(sorted_data)
            
        if "H" == lst_file[i][0]:
            
            attribute = lst_file[i][1]
            
            hs.histogram(data, attribute)
            
        if "C" == lst_file[i][0]:  
            
            attribute = lst_file[i][1]
            
            order = lst_file[i][2]
            
            cr.curve_fit(data,attribute, order)
        
