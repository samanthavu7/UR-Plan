#Program that queries based primarily on 
from URPlanClasses import Student
from URPlanClasses import Class

from designProjectScratch import ClassInfo
from designProjectScratch import initCSCoreClass
from designProjectScratch import initCSNonCoreClasses

#Hard coding this for now as this Student object has the most varied 
#time preferences compared to the rest (good for testing)

def getClassesBasedOnTime(preferStartTime, preferEndTime):
    classesRef = db.collection(u'classes').where(u'classType', u'==', u'LEC') #currently only gives Lectures, remove .where here to get LAB/DIS as well

    queryStartTimes = classesRef.where(u'startTime', u'>=', preferStartTime)
    queryEndTimes = classesRef.where(u'endTime', u'<=', preferEndTime)


    try:
        docs1 = queryStartTimes.stream()
    except google.cloud.exceptions.NotFound:
        print("Doc not found")

    try:
        docs2 = queryEndTimes.stream()
    except google.cloud.exceptions.NotFound:
        print("Doc not found")

    meetsBoth = [value for value in docs1 if value in docs2]
    matchingClasses = []
    for item in meetsBoth:
        matchingClasses.append(Class.from_dict(item.to_dict()))
    return matchingClasses

def getClassesBasedOnDays(useMondays, useTuesdays, useWednesdays, useThursdays, useFridays):
    classRef2 = db.collection(u'classes').where(u'classType', u'==', u'LEC')
    if(not useMondays):
        classRef2 = classRef2.where(u'meetsOnMonday', u'==', False)
    if(not useTuesdays):
        classRef2 = classRef2.where(u'meetsOnTuesday', u'==', False)
    if(not useWednesdays):
        classRef2 = classRef2.where(u'meetsOnWednesday', u'==', False)
    if(not useThursdays):
        classRef2 = classRef2.where(u'meetsOnThursday', u'==', False)
    if(not useFridays):
        classRef2 = classRef2.where(u'meetsOnFriday', u'==', False)
    try:
        matchTimeClasses = classRef2.stream()
    except google.cloud.exceptions.NotFound:
        print("Can not find a document that matches")

    returnList = []
    for item in matchTimeClasses:
        returnList.append(Class.from_dict(item.to_dict()))
    return returnList


studentRef = db.collection(u'students').document(u'862191102')

try:
    docStudent = studentRef.get()
    studentQuery = Student.from_dict(docStudent.to_dict())
    print(studentQuery)
except google.cloud.exceptions.NotFound:
    print("Student Document Not Found")

queryTimeList = getClassesBasedOnTime(studentQuery.prefStartTime, studentQuery.prefEndTime)
queryDayList = getClassesBasedOnDays(studentQuery.classesOnMonday, studentQuery.classesOnTuesday, 
                                     studentQuery.classesOnWednesday, studentQuery.classesOnThursday, 
                                     studentQuery.classesOnFriday)

#At this point the result is stored as a list holding Class elements
for classItem in queryTimeList:
    print(classItem)

print("---Days---")
for classItem in queryDayList:
    print(classItem)