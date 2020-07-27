import numpy as np
import pandas as pd

def readCSV(argv):
    #attempt to read csv files
    for arg in argv:
        try:
            if ("courses" in arg):
                courses = pd.read_csv(arg)
            elif("marks" in arg):
                marks = pd.read_csv(arg)
            elif("students" in arg):
                students = pd.read_csv(arg)
            elif("tests" in arg):
                tests = pd.read_csv(arg)
        except:
            print("An unexpected error occured") 
            return [], [], [], []
        
    return courses, marks, students, tests