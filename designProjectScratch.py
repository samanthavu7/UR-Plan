class ClassInfo(object):
    def __init__(self, className, quartersOffered, yearUsuallyTaken, ofaSeries,isUpperDiv, fulfillsReq, preReqtoTake=[], isPreReqFor=[]):
        self.className = className # Format: CS010 or PHYS040A
        self.quartersOffered = quartersOffered #(F)all, (W)inter, (S)pring, S(U)mmer
        self.yearUsuallyTaken = yearUsuallyTaken
        self.ofaSeries #CS010 is in a series with CS012 & CS014, PHYS040A w/ PHYS040B, etc.
        self.isUpperDiv = isUpperDiv
        self.fulfillsReq = fulfillsReq # CS_MAJOR, CS_CORE, CS_ELECT, ENGR_BREATH, HUM_A, LIFE_SCI, etc are all valid tags
        self.preReqtoTake = preReqtoTake # Theses classes are needed in order to take this class
        self.isPreReqFor = isPreReqFor # This class is needed to take the classes in this list
    def numDescendants(self):
        #gives number of class descendants
        return len(self.isPreReqFor)

def initCSCoreClass():
    #Creates a list of ClassInfo objects that match with core CS class info
    classList = []
    classList.append(ClassInfo("CS010", "FW", 1, True, False, ["CS_MAJOR", "CS_CORE"], [], ["CS011", "CS061", "CS012", "CS031", "CS014",
                                                      "CS120A", "CS100", "CS111", "CS120B", "CS150",
                                                      "CS141", "CS161", "CS152", "CS153"]))
    classList.append(ClassInfo("CS012", "FWS", 1, True, False, ["CS_MAJOR", "CS_CORE"], ["CS010"], ["CS014", "CS100", "CS150", "CS141",
                                                              "CS152", "CS153"]))
    classList.append(ClassInfo("CS014", "FWS", 1, True, False, ["CS_MAJOR", "CS_CORE"], ["CS012"], ["CS100", "CS150", "CS141", "CS152", 
                                                              "CS153"]))
    classList.append(ClassInfo("CS011", "WS", 2, False, False, ["CS_MAJOR", "CS_CORE"], ["MATH009A", "CS010"], ["CS111", "CS150", "CS141",
                                                                         "CS152", "CS153"]))
    classList.append(ClassInfo("CS061", "FWS", 2, False, False, ["CS_MAJOR", "CS_CORE"], ["CS010"], ["CS120A", "CS120B", "CS161", "CS152",
                                                              "CS153"]))
    classList.append(ClassInfo("CS031", "FWS", 3, False, False, ["CS_MAJOR", "CS_CORE"], ["CS010", "MATH009A"], []))
    classList.append(ClassInfo("CS120A", "FWS", 2, True, True, ["CS_MAJOR", "CS_CORE"], ["CS061"], ["CS120B", "CS161"]))
    classList.append(ClassInfo("CS100", "FWS", 2, False, True, ["CS_MAJOR", "CS_CORE"], ["CS014"], ["CS152", "CS153"]))
    classList.append(ClassInfo("CS111", "FWS", 3, False, True, ["CS_MAJOR", "CS_CORE"], ["CS010", "CS011", "MATH009C"], ["CS150", "CS141", 
                                                                                   "CS152", "CS153"]))
    classList.append(ClassInfo("CS120B", "FWS", 2, True, True, ["CS_MAJOR", "CS_CORE"], ["CS120A"], ["CS161"]))
    classList.append(ClassInfo("CS150", "WS", 3, False, True, ["CS_MAJOR", "CS_CORE"], ["CS014", "CS111", "MATH009C"], ["CS152"]))
    classList.append(ClassInfo("CS141", "WS", 4, False, True, ["CS_MAJOR", "CS_CORE"], ["CS111", "CS014"], []))
    classList.append(ClassInfo("CS161", "FWS", 4, False, True, ["CS_MAJOR", "CS_CORE"], ["CS120B"], []))
    classList.append(ClassInfo("CS152", "FWS", 4, False, True, ["CS_MAJOR", "CS_CORE"],["CS111", "CS150", "CS100"], []))
    classList.append(ClassInfo("CS153", "FWS", 4, False, True, ["CS_MAJOR", "CS_CORE"], ["CS111", "CS061", "CS100"], []))
    return classList

def initCSNonCoreClasses():
    #Will fill classes like MATH009A, ENGL001A, ENGR001 and/or ENGR180W
    classList2 = []
    classList.append(ClassInfo("MATH009A", "FWS", 1, True, False, ["CS_MAJOR"], ["MAE"], ["MATH009B", "CS011", "CS031", "MATH010A", 
                                                                                          "MATH009C", "STAT155", "CS111", "CS150", 
                                                                                          "CS141", "CS152", "CS153"]))
    classList.append(ClassInfo("MATH009B", "FWS", 1, True, False, ["CS_MAJOR"], ["MATH009A"], ["MATH010A", "MATH009C", "STAT155", 
                                                                                               "CS111", "CS150", "CS141", "CS152",
                                                                                              "CS153"]))
    return classList2

csCoreClassList = initCSCoreClass()

csNonCoreList = initCSNonCoreClasses()

for classObj in csCoreClassList:
    print(classObj.className + " has " + str(classObj.numDescendants()) + " descendants.")

print("Classes that you can take without prior req: ")
for classObj in csCoreClassList:
    if(not classObj.preReqtoTake):
        print(classObj.className + " can now be taken!")

studentList = ["CS010", "MATH009A", "MAE"]

#Before the program queues the database for classes, first determine what classes 
#student has already taken.

#Removes Classes student already took from csCoreClassList
for selClass in studentList:
    for classObj in csCoreClassList[:]:
        if(selClass == classObj.className):
            csCoreClassList.remove(classObj)

print("New list after class removal")
for classObj in csCoreClassList:
    print(classObj.className)

#removes instances of a class that a student has taken from each future classes preReq List.
#The reasoning is that when a class object has an empty preReq list, the student has the 
#prereq. classes needed to take the classes.
for selClass in studentList:
    for classObj in csCoreClassList[:]:
        if(selClass in classObj.preReqtoTake):
            classObj.preReqtoTake.remove(selClass)

print("Classes that you can take after classes removal: ")
for classObj in csCoreClassList:
    if(not classObj.preReqtoTake):
        print(classObj.className + " can now be taken!")
        print(classObj.className + " is a preReq for " + str(len(classObj.isPreReqFor)) + " classes.")