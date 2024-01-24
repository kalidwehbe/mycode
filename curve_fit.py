# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Kalid Wehbe"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101259994"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-058"

#==========================================#
# Place your curve_fit function after this line
import numpy as np

def curve_fit(data: list, attribute: str, order: int):
    
    
    """
    Displays the function of best fit for the curve
    
    Precondition attribute must be in the list
    
    >>> curve_fit( [{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 
    
    1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}], "Failures" , 0)
    
    
    y = 5.67x^0
    
    
    
    """
    
    
    values = {}
    for d in data:
        key = d[attribute]
        if key not in values:
            values[key] = []
        values[key].append(d['G_avg'])

    x, y = [], []
    for key, avg in values.items():
        x.append(key)
        y.append(np.mean(avg))
        

    if order > len(x) - 1:
        coeffs = np.polyfit(x, y, len(x) - 1)
    else:
        coeffs = np.polyfit(x, y, order)

    eqn = 'y = '
    for i in range(order, -1, -1):
        if i == order:
            eqn += str(round((coeffs[i]),2)) + 'x^' + str(i)
        elif i == 0:
            eqn += '+' + str(round((coeffs[i])))
        else:
            eqn += '+' + str(round((coeffs[i]))) + 'x^' + str(i)
    return eqn


# Do NOT include a main script in your submission
