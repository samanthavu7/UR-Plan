#Function that adds documents to Firebase collection

#To make this work, make sure to have already run testFireBaseInit.py,
#or copy/paste all contents of that file after this file's 'from' statements
#Also, make sure URPlanClasses.py and designProjectScratch.py are in the 
#same project directory where you'll run this.

from URPlanClasses import Student
from URPlanClasses import Class

from designProjectScratch import ClassInfo
from designProjectScratch import initCSCoreClass
from designProjectScratch import initCSNonCoreClasses

#doc_refStudent = db.collection(u'students').document(u'864651254')
#doc_refClass = db.collection(u'classes').document(u'53095') #Currently example query set to CS014 class. 


#try:
#    docStudent = doc_refStudent.get()
#    studentQuery = Student.from_dict(docStudent.to_dict())
#    print(studentQuery)
#except google.cloud.exceptions.NotFound:
#    print("Student Document Not Found")

#try:
#    docClass = doc_refClass.get()
#    classQuery = Class.from_dict(docClass.to_dict())
#    print(classQuery)
#except google.cloud.exceptions.NotFound:
#    print("Document Not Found")

def updateClassesToTake(studentList, classListing):
    for selClass in studentList:
        for classObj in classListing[:]:
            if(selClass == classObj.className):
                classListing.remove(classObj)

    for selClass in studentList:
        for classObj in classListing[:]:
            if(selClass in classObj.preReqtoTake):
                classObj.preReqtoTake.remove(selClass)
    return classListing

doc_refStudent = db.collection(u'students').document(u'864651254')

try:
    docStudent = doc_refStudent.get()
    studentQuery = Student.from_dict(docStudent.to_dict())
    print(studentQuery)
except google.cloud.exceptions.NotFound:
    print("Student Document Not Found")

studentList = studentQuery.coursesList[:]

coreClasses = initCSCoreClass()
nonCoreClasses = initCSNonCoreClasses()

classesToQuery = []

coreClasses = updateClassesToTake(studentList, coreClasses)
nonCoreClasses = updateClassesToTake(studentList, nonCoreClasses)



print("Core classes that you can take after classes removal: ")
for classObj in coreClasses:
    if(not classObj.preReqtoTake):
        print(classObj.className + " can now be taken!")
        classesToQuery.append(classObj.className)
    else:
        print(classObj.className + " has " + str(classObj.numDescendants()) + " descendants.")

print("Classes in nonCore that can be taken")

for classObj2 in nonCoreClasses:
    if(not classObj2.preReqtoTake):
        print(classObj2.className + " can now be taken!")
        classesToQuery.append(classObj2.className)


#Querying is done here.

classes_Ref = db.collection(u'classes')
queryQueue = []
for classItem in classesToQuery:
    queryQueue.append(classes_Ref.where(u'courseName', u'==', classItem).where(u'classType', u'==', u'LEC'))

listOfClasses = []
for queryItem in queryQueue:
    try:
        docs = queryItem.stream()
        for doc in docs:
            listOfClasses.append(Class.from_dict(doc.to_dict()))
    except google.cloud.exceptions.NotFound:
        print("Doc not found")

print("Results (in Class object form)")
for item in listOfClasses:
    print(item)