# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = ""

# Update "" with your student number (e.g., 100100100)
__student_number__ = ""

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = ""

#==========================================#
# Place your histogram function after this line

import matplotlib.pyplot as plt


def histogram(data, attribute):
    # Create a dictionary to store the frequency counts for each level of the attribute
    
    
    """
    Makes a histogram based on the data given and the attribute
    
    Preconditions = G_avg must be in the list of data
    
    >>> histogram([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 
    
    'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67 }], Age)
    
    displays a histogram
    
    """
    freq_counts = {}

    # Loop through the data and count the number of students at each level of the attribute
    for student in data:
        level = student[attribute]

        # If the level is already in the dictionary, increment the count. Otherwise, add it to the dictionary with a count of 1.
        if level in freq_counts:
            freq_counts[level] += 1
        else:
            freq_counts[level] = 1
    
    # Sort the frequency counts by level
    sorted_counts = sorted(freq_counts.items())

    # Separate the levels and counts into separate lists
    levels = [level for level, count in sorted_counts]
    counts = [count for level, count in sorted_counts]

    # Create a bar plot of the frequency counts
    plt.bar(levels, counts)
    plt.xlabel(attribute)
    plt.ylabel('Frequency')
    plt.title('Histogram of ' + attribute)
    plt.show()

    return None



# Do NOT include a main script in your submission
