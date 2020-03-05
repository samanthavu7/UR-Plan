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

doc_ref = db.collection(u'classes').document(u'53095') #Currently example query set to CS014 class.

try:
    doc = doc_ref.get()
    classQuery = Class.from_dict(doc.to_dict())
    print(classQuery)
except google.cloud.exceptions.NotFound:
    print("Document Not Found")
