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

    startList = []
    endList = []
    try:
        docs1 = queryStartTimes.stream()
        for doc in docs1:
            startList.append(Class.from_dict(doc.to_dict()))
    except google.cloud.exceptions.NotFound:
        print("Doc not found")

    try:
        docs2 = queryEndTimes.stream()
        for doc in docs2:
            endList.append(Class.from_dict(doc.to_dict()))
    except google.cloud.exceptions.NotFound:
        print("Doc not found")
    print("Length of lists: " + str(len(startList)) + " " + str(len(endList)))
    meetsBoth = []
    for doc3 in startList:
        for doc4 in endList:
            if(doc3.CRN == doc4.CRN):
                meetsBoth.append(doc4)
                print("Entered")
    #matchingClasses = []
    #for item in meetsBoth:
    #    matchingClasses.append(Class.from_dict(item.to_dict()))
    #return matchingClasses
    return meetsBoth

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


#Intersection of matchingClassesDays and matchingClassesTime
intersectList = [] #holds the intersection of the lists 
for class1 in queryDayList:
    for class2 in queryTimeList:
        if(class1.CRN == class2.CRN):
            intersectList.append(class2)
                    
coreList = initCSCoreClass() #has to have a fresh copy of coreClasses
nonCoreList = initCSNonCoreClasses() #has to have a fresh copy of nonCoreClasses
tupleList = []
passedOnce = True
for item in intersectList:
    passedOnce = True
    for classItem in coreList:
        if((item.courseName == classItem.className) and (passedOnce)):
            passedOnce = False
            tupleList.append((item, classItem.numDescendants()))

for item in intersectList:
    passedOnce = True
    for classItem in nonCoreList:
        if((item.courseName == classItem.className) and (passedOnce)):
            passedOnce = False
            tupleList.append((item, classItem.numDescendants()))

tupleList.sort(key=lambda x: x[1], reverse=True)
print("Tuples:")
for item5 in tupleList:
    print(item5)


print("NonTuples:")
for item in intersectList:
    print(item)

#At this point the result is stored as a list holding Class elements
#print("Non intersection Lines ++++++++")
#for classItem in queryTimeList:
#    print(classItem)

#print("---Days---")
#for classItem in queryDayList:
#    print(classItem)