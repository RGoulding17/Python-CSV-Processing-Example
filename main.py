#Run Command: python -W ignore main.py courses.csv students.csv tests.csv marks.csv output.json
#Author: Ryan Goulding
#Date: 07/27/2020

import sys
import dataProcessing
import csvReader
import jsonConvert

def writeToFile(json, filename):
    f = open(filename, "a")
    f.truncate(0)
    f.write(json)
    f.close()

def main(argv):
    #send command line arguments to csvReader and store response in 4 seperate dataframes
    courses, marks, students, tests = csvReader.readCSV(argv)

    #send dataframes for processing
    totalAverages, totalAveragesTestWeights, courseAverages, courseAveragesTestWeights, studentGradesByCourse = dataProcessing.processData(courses, marks, students, tests)

    #send processed dataframes to be converted into json
    json = jsonConvert.convertToJSON(totalAverages, totalAveragesTestWeights, courseAverages, courseAveragesTestWeights, studentGradesByCourse, courses, students)

    #save the jsonified data into specified output file
    filename = argv[-1]
    writeToFile(json, filename)
    print("done")

if __name__ == "__main__":
   main(sys.argv[1:])