"""
This is a module that defines the class structure.
Current version 0.3 - Changed days class variable to five Boolean variables
representing the days of the week. As well, removed static information from 
Class class, will store instead in another file
"""
class Class(object):
    def __init__(self, courseName, classType, sectionNum, CRN, startTime, endTime, meetsOnMonday, meetsOnTuesday, 
                 meetsOnWednesday, meetsOnThursday, meetsOnFriday, classLoc, seatsOpen, seatsActual, creditAmt,
                prof, linkedSections=[]):
        self.courseName = courseName
        self.classType = classType
        self.sectionNum = sectionNum
        self.CRN = CRN
        self.startTime = startTime
        self.endTime = endTime
        self.meetsOnMonday = meetsOnMonday
        self.meetsOnTuesday = meetsOnTuesday
        self.meetsOnWednesday = meetsOnWednesday
        self.meetsOnThursday = meetsOnThursday
        self.meetsOnFriday = meetsOnFriday
        self.classLoc = classLoc
        self.seatsOpen = seatsOpen
        self.seatsActual = seatsActual
        self.creditAmt = creditAmt
        self.prof = prof
        self.linkedSections = linkedSections

    @staticmethod
    def from_dict(source):
        
        c = Class(source[u'courseName'], source[u'classType'], source[u'sectionNum'], source[u'CRN'], 
                  source[u'startTime'], source[u'endTime'], source[u'meetsOnMonday'], 
                  source[u'meetsOnTuesday'], source[u'meetsOnWednesday'], source[u'meetsOnThursday'], 
                  source[u'meetsOnFriday'], source[u'classLoc'], source[u'seatsOpen'], 
                  source[u'seatsActual'], source[u'creditAmt'], source[u'prof'], source[u'linkedSections'])
        return c
        

    def to_dict(self):
        
        dest = {
            u'courseName': self.courseName,
            u'classType': self.classType,
            u'sectionNum': self.sectionNum,
            u'CRN': self.CRN,
            u'startTime': self.startTime,
            u'endTime': self.endTime,
            u'meetsOnMonday': self.meetsOnMonday,
            u'meetsOnTuesday': self.meetsOnTuesday,
            u'meetsOnWednesday': self.meetsOnWednesday,
            u'meetsOnThursday': self.meetsOnThursday,
            u'meetsOnFriday': self.meetsOnFriday,
            u'classLoc': self.classLoc,
            u'seatsOpen': self.seatsOpen,
            u'seatsActual': self.seatsActual,
            u'creditAmt': self.creditAmt,
            u'prof': self.prof,
            u'linkedSections': self.linkedSections
        }
        return dest
        

    def __repr__(self):
        return(u'Class(courseName={}, classType={}, sectionNum={}, CRN={}, startTime={}, endTime={}, meetsOnMonday={}, meetsOnTuesday={}, meetsOnWednesday={}, meetsOnThursday={}, meetsOnFriday={}, classLoc={}, seatsOpen={}, seatsActual={}, creditAmt={}, prof={}, linkedSections={})'
               .format(self.courseName, self.classType, self.sectionNum, self.CRN, self.startTime, self.endTime,
                       self.meetsOnMonday, self.meetsOnTuesday, self.meetsOnWednesday, self.meetsOnThursday,
                      self.meetsOnFriday,self.classLoc, self.seatsOpen, self.seatsActual, self.creditAmt,
                     self.prof, self.linkedSections))

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
