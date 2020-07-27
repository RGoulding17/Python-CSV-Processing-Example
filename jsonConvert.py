import numpy as np
import pandas as pd
import json

#classes for json conversion
class Course:
    def __init__(self, id, name, teacher, courseAverage):
        self.id = id
        self.name = name
        self.teacher = teacher
        self.courseAverage = courseAverage

    def toJSON(self):
        return dict(id = self.id, name = self.name, teacher=self.teacher, courseAverage=self.courseAverage)

class Student:
    def __init__(self, id, name, totalAverage, courses):
        self.id = id
        self.name = name
        self.totalAverage = totalAverage
        self.courses = courses

    def toJSON(self):
        return dict(id = self.id, name = self.name, totalAverage = self.totalAverage, courses = self.courses)

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'toJSON'):
            return obj.toJSON()
        else:
            return json.JSONEncoder.default(self, obj)

def convertToJSON(totalAverages, totalAveragesTestWeights, courseAverages, courseAveragesTestWeights, studentGradesByCourse, courses, students):
    #declaration of variables
    coursesList = []*len(courseAverages)
    studentList = []*len(totalAverages)
    subCourseList = []*len(courseAverages)

    #create list of courses
    for x in studentGradesByCourse:
        iterator = 0
        subCourseList.clear()
        for y in x:
            subCourseList.append(Course(int(courses['id'][iterator]), str(courses['name'][iterator]), str(courses['teacher'][iterator]), str(y)))
            iterator+=1
        coursesList.append(subCourseList)

    #create list of students
    iterator = 0
    for k,v in totalAverages.items():
        if v != 'nan':
            studentList.append(Student(str(students['id'][iterator]), str(students['name'][iterator]),str(v), coursesList[iterator]))
            iterator +=1

    #parse list to json file
    jsonstring = json.dumps(studentList, cls=ComplexEncoder, indent=4)
    return jsonstring