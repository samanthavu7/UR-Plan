#Function that adds documents to Firebase collection
class Class(object):
    def __init__(self, courseName, classType, sectionNum, CRN, startTime, endTime, days,
                classLoc, seatsOpen, seatsActual, creditAmt, prof,isUpperDiv, quarterOffered, preReqClasses=[], fulfillsReq=[]):
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
        self.fulfillsReq = fulfillsReq

    @staticmethod
    def from_dict(source):
        
        c = Class(source[u'courseName'], source[u'classType'], source[u'sectionNum'], source[u'CRN'], source[u'startTime'],
                 source[u'endTime'], source[u'days'], source[u'classLoc'], source[u'seatsOpen'], source[u'seatsActual'], source[u'creditAmt'],
                 source[u'prof'], source[u'isUpperDiv'], source[u'quarterOffered'], source[u'preReqClasses'], source[u'fulfillsReq'])
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
            u'fulfillsReq': self.fulfillsReq
        }
        return dest
        

    def __repr__(self):
        return(u'Class(courseName={}, classType={}, sectionNum={}, CRN={}, startTime={}, endTime={}, days={}, classLoc={}, seatsOpen={}, seatsActual={}, creditAmt={}, prof={}, isUpperDiv={}, quarterOffered={}, preReqClasses={}, fulfillsReq={})'
               .format(self.courseName, self.classType, self.sectionNum, self.CRN, self.startTime, self.endTime, self.days,
                      self.classLoc, self.seatsOpen, self.seatsActual, self.creditAmt, self.prof, self.isUpperDiv, 
                      self.quarterOffered, self.preReqClasses, self.fulfillsReq))

userOption = input("-----Press any key to enter new class. ('q' to quit)-----: ")
if(userOption != 'q'):
    className = input("Enter course name (Format as 'CS010' or 'BIOL005'): ")
    classCRN = input("Enter courseCRN: ")
    classCRN = int(classCRN)
    classTyping = input("Enter class type (Enter either LEC, DIS, or LAB): ")
    classSection = input("Enter class sectionNum: ")
    classSection = int(classSection)
    classStartTime = input("Enter class start time (24 hour format, 1:37 entered as 1337): ")
    classStartTime = int(classStartTime)
    classEndTime = input("Enter class end time (24 hour format, 1:37 entered as 1337): ")
    classEndTime = int(classEndTime)
    classDays = input("Enter class days (Classes that meet on Tues & Thurs enter as TR, Mon Wed and Fri as MWF): ")
    classLocation = input("Enter class location: ")
    classSeatsActual = input("Enter amount of seats in class: ")
    classSeatsActual = int(classSeatsActual)
    classCredit = input("Enter number of credits class is worth: ")
    classCredit = int(classCredit)
    classProf = input("Enter last name of professor: ")
    userOption2 = input("Is an upper division course? ('y' or 'n'): ")
    if(userOption2 == 'y'):
        classUpperDiv = True
    else:
        classUpperDiv = False
    classQuarters = input("Enter quarters offered (Fall and Winter enter as 'FW' or 'SU' for spring and summer for example): ")
    classPreReq = []
    userOption3 = input("Enter classPreReqs (CS010, CS100), if any (enter 'q' to quit):")
    while(userOption3 != "q"):
        classPreReq.append(userOption3)
        userOption3 = input("Enter classPreReqs (CS010, CS100), if any (enter 'q' to quit):")
    classFulfills = []
    userOption4 = input("Enter requirements this class fulfills, if any (enter 'q' to quit): ")
    while(userOption4 != "q"):
        classFulfills.append(userOption4)
        userOption4 = input("Enter requirements this class fulfills, if any (enter 'q' to quit): ")
    potentialClass = Class(courseName=className, classType=classTyping, sectionNum=classSection, CRN=classCRN, startTime=classStartTime, 
                           endTime=classEndTime, days=classDays, classLoc=classLocation, seatsOpen=classSeatsActual, seatsActual=classSeatsActual,
                           creditAmt=classCredit, prof=classProf, isUpperDiv=classUpperDiv, quarterOffered=classQuarters, preReqClasses=classPreReq,
                           fulfillsReq=classFulfills)
    db.collection(u'classes').document(str(classCRN)).set(potentialClass.to_dict())
    print("Added new class to collection in Firebase.")
    userOption = input("+++++Press any key to enter another class. (or 'q' to quit)+++++: ")



