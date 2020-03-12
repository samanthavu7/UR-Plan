#Function that adds documents to Firebase collection
from URPlanClasses import Student
from URPlanClasses import Class


doc_refStudent = db.collection(u'students').document(u'864651254')
doc_refClass = db.collection(u'classes').document(u'53095') #Currently example query set to CS014 class. 

try:
    docStudent = doc_refStudent.get()
    studentQuery = Student.from_dict(docStudent.to_dict())
    print(studentQuery)
except google.cloud.exceptions.NotFound:
    print("Student Document Not Found")

try:
    docClass = doc_refClass.get()
    classQuery = Class.from_dict(docClass.to_dict())
    print(classQuery)
except google.cloud.exceptions.NotFound:
    print("Document Not Found")

#if(not studentQuery.coursesList):
    #List empty - Likely a new student - Recommend default starting classes
#else:
    #Have a copy of a - or some - 'master list(s)' that compares against a student's coursesList.
    #Remove classes that are in student's coursesList from master list copies. 
    #Create a graph in Python using the remaining  

    #TA suggests that it will be a DFS issue.
