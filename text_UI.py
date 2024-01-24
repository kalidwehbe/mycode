# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "caleb kooy "

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101265469"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-058"

#==========================================#
# Place your script for your text_UI after this line
import load_data as ld
import sort as st
import curve_fit as cr
import histogram as hs


def main():
    
    
    
    command = ''

    print("The available commands are:")
    print("L)oad Data")
    print("S)ort Data")
    print("C)urve Fit")
    print("H)istogram")
    print("E)xit")
    command = (input("Please type your command: "))
    command = command.upper()
    
    while command != "L":
        
        if command == "S" or command == "C" or command == "H":
            
            print("File not loaded. Please, load a file first.")
            
        else:
            print("Invalid command")
            
        print("The available commands are:")
        print("L)oad Data")
        print("S)ort Data")
        print("C)urve Fit")
        print("H)istogram")
        print("E)xit")
        command = (input("Please type your command: "))
        command = command.upper()   
        
    
    
    if command == "L":
        
        file_name = input("Please enter the name of the file: ")
        
        attribute = input("Please enter the attribute to use as a filter: ")
        
        if attribute == "All":
            
            tup_category = ("All",-1)
            
            
            data = ld.add_average(ld.load_data(file_name, tup_category))
            
            print(data)
            
        else:
        
            value = input("Please enter the value of the attribute: ")
            
            tup_category = (attribute, value)
            
            data = ld.add_average(ld.load_data(file_name, tup_category))
            
            print(data)
        
            
        while command != "E":
            print("The available commands are:")
            print("L)oad Data")
            print("S)ort Data")
            print("C)urve Fit")
            print("H)istogram")
            print("E)xit")
            command = (input("Please type your command: "))
            command = command.upper()
        
            while command != "L" and command != "S" and command != "C" and command != "H" and command != "E":
                print("Invalid command")
                print("The available commands are:")
                print("L)oad Data")
                print("S)ort Data")
                print("C)urve Fit")
                print("H)istogram")
                print("E)xit")
                command = (input("Please type your command: "))
                command = command.upper()
                
                
            if command == "L":
                
                file_name = input("Please enter the name of the file: ")
                
                attribute = input("Please enter the attribute to use as a filter: ")
                
                if attribute == "All":
                    
                    tup_category = ("All",-1)
                    
                    
                    data = ld.add_average(ld.load_data(file_name, tup_category))
                    
                    print(data)
                    
                else:
                
                    value = input("Please enter the value of the attribute: ")
                    
                    tup_category = (attribute, value)
                    
                    data = ld.add_average(ld.load_data(file_name, tup_category))
                    
                    print(data)
                                
                
            if command == "S": 
    
    
    
                print("Please enter the attribute you want to use for sorting:")
                print("'Age' 'StudyTime' 'Failures' 'G_Avg'")
                attribute = input("")
                while attribute != "Age" and attribute != "StudyTime" and attribute != "Failures" and attribute != "G_avg":
                    print("Please enter the on of the valid attributes:")
                
                print("Please Enter Ascending <A> or Descneding <D>")
                order = input("")
            
                
            
                    
                sorted_data = st.sort(data, order , attribute)   
                
                yes_or_no = input("Data Sorted. Do you want to display the data?: ")
                
                if yes_or_no == "Y" or "y": 
                    
                    print(sorted_data) 
                
                
            
            elif command == "H":
                
                attribute = input("Please enter the attribute you want to use for plotting: ")
            
                    
                print(hs.histogram(data ,attribute))          
        
        
            elif command == "C":
            
                attribute = input("Please enter the attribute you want to use to find the best fit for G_Avg: ")
                
                order =  int(input("Please enter the order of the polynomial to be fitted: "))
                
                file_name = "student-mat.csv" 
                
                tup_category = ("All",-1)
                
                print(cr.curve_fit(data, attribute, order))
            
        
            elif command == "E": 
                break      
   
        

main()