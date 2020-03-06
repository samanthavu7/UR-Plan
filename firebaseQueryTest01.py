#Function that adds documents to Firebase collection
class Class(object):
    def __init__(self, courseName, classType, sectionNum, CRN, startTime, endTime, days,
                classLoc, seatsOpen, seatsActual, creditAmt, prof,isUpperDiv, quarterOffered, preReqClasses=[], preReqFor=[], fulfillsReq=[]):
        self.courseName = courseName
        self.classType = classType
        self.sectionNum = sectionNum
        self.CRN = CRN
        self.startTime = startTime
        self.endTime = endTime
        self.days = days
        self.classLoc = classLoc
        self.seatsOpen = seatsOpen
        self.seatsActual = seatsActual
        self.creditAmt = creditAmt
        self.prof = prof
        self.isUpperDiv = isUpperDiv
        self.quarterOffered = quarterOffered
        self.preReqClasses = preReqClasses
        self.preReqFor = preReqFor
        self.fulfillsReq = fulfillsReq

    @staticmethod
    def from_dict(source):
        
        c = Class(source[u'courseName'], source[u'classType'], source[u'sectionNum'], source[u'CRN'], source[u'startTime'],
                 source[u'endTime'], source[u'days'], source[u'classLoc'], source[u'seatsOpen'], source[u'seatsActual'], source[u'creditAmt'],
                 source[u'prof'], source[u'isUpperDiv'], source[u'quarterOffered'], source[u'preReqClasses'], source[u'preReqFor'], source[u'fulfillsReq'])
        return c
        

    def to_dict(self):
        
        dest = {
            u'courseName': self.courseName,
            u'classType': self.classType,
            u'sectionNum': self.sectionNum,
            u'CRN': self.CRN,
            u'startTime': self.startTime,
            u'endTime': self.endTime,
            u'days': self.days,
            u'classLoc': self.classLoc,
            u'seatsOpen': self.seatsOpen,
            u'seatsActual': self.seatsActual,
            u'creditAmt': self.creditAmt,
            u'prof': self.prof,
            u'isUpperDiv': self.isUpperDiv,
            u'quarterOffered': self.quarterOffered,
            u'preReqClasses': self.preReqClasses,
            u'preReqFor': self.preReqFor,
            u'fulfillsReq': self.fulfillsReq
        }
        return dest
        

    def __repr__(self):
        return(u'Class(courseName={}, classType={}, sectionNum={}, CRN={}, startTime={}, endTime={}, days={}, classLoc={}, seatsOpen={}, seatsActual={}, creditAmt={}, prof={}, isUpperDiv={}, quarterOffered={}, preReqClasses={}, preReqFor={}, fulfillsReq={})'
               .format(self.courseName, self.classType, self.sectionNum, self.CRN, self.startTime, self.endTime, self.days,
                      self.classLoc, self.seatsOpen, self.seatsActual, self.creditAmt, self.prof, self.isUpperDiv, 
                      self.quarterOffered, self.preReqClasses, self.preReqFor, self.fulfillsReq))

class Student(object):
    def __init__(self, firstName, lastName, major, year=0, prefClassesLimit=4, prefStartTime=8000, prefEndTime=2200, prefDays="MTWRF", coursesList=[]):
        #algorithm for class selection can first compare a student class's preferences against
        #default values. When a particular value is different from default, only then will it
        #be used as an element in a query to classes database.  
        self.firstName = firstName
        self.lastName = lastName
        self.major = major
        self.year = year
        self.prefClassesLimit = prefClassesLimit #default is 4 class limit
        self.prefStartTime = prefStartTime
        self.prefEndTime = prefEndTime
        self.prefDays = prefDays
        self.coursesList = coursesList

    @staticmethod
    def from_dict(source):
        
        s = Student(source[u'firstName'], source[u'lastName'], source[u'major'], source[u'year'], source[u'prefClassesLimit'], source[u'prefStartTime'], source[u'prefEndTime'],
                    source[u'prefDays'], source[u'coursesList'])
        return s
        

    def to_dict(self):
        
        dest = {
            u'firstName': self.firstName,
            u'lastName': self.lastName,
            u'major': self.major,
            u'year': self.year,
            u'prefClassesLimit': self.prefClassesLimit,
            u'prefStartTime': self.prefStartTime,
            u'prefEndTime': self.prefEndTime,
            u'prefDays': self.prefDays,
            u'coursesList': self.coursesList
        }
        return dest
        

    def __repr__(self):
        return(u'Student(firstName={}, lastName={}, major={}, year={}, prefClassesLimit={}, prefStartTime={}, prefEndTime={}, prefDays={}, coursesList={})'
               .format(self.firstName, self.lastName, self.major, 
                       self.year, self.prefClassesLimit, self.prefStartTime, self.prefEndTime, self.prefDays, self.coursesList))

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
