import numpy as np
import pandas as pd

def processData(courses, marks, students, tests):
    #dictionarys for holding total average data
    totalAverages = dict.fromkeys(students.id.to_numpy(),0 )
    totalAveragesTestWeights = dict.fromkeys(students.id.to_numpy(),0 )

    #dictionarys of lists for holding grades to be processed
    courseAverages = {k:np.zeros(len(courses.id)) for k in courses.id.to_numpy()}
    courseAveragesTestWeights = {k:np.zeros(len(courses.id)) for k in courses.id.to_numpy()}

    #create a new list to hold the calculated grade for each course
    studentGradesByCourse = [None]*len(courseAverages)

    #calculate total averages as well as track what students completed tests
    #i calculate weightings incase there is bonus material that goes above 100 (bonus marks)
    for index,row in marks.iterrows():
        totalAverages[row['student_id']] += row['mark']*tests.iloc[row['test_id']-1]['weight']
        totalAveragesTestWeights[row['student_id']] +=tests.iloc[row['test_id']-1]['weight']

        courseAverages[row['student_id']][tests.iloc[row['test_id']-1]['course_id']-1] +=row['mark']*tests.iloc[row['test_id']-1]['weight']
        courseAveragesTestWeights[row['student_id']][tests.iloc[row['test_id']-1]['course_id']-1] +=tests.iloc[row['test_id']-1]['weight']

    totalAverages = {k: totalAverages[k]/totalAveragesTestWeights[k] for k in totalAveragesTestWeights.keys() & totalAverages}

    #calculate student averages
    for i in range(len(courseAverages)):
        studentGradesByCourse[i] = [i / j for i, j in zip(courseAverages[i+1], courseAveragesTestWeights[i+1])]

    return totalAverages, totalAveragesTestWeights, courseAverages, courseAveragesTestWeights, studentGradesByCourse