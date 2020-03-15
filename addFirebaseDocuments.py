#Function that adds documents to Firebase collection
from URPlanClasses import Class

userOption = input("-----Press any key to enter new class. ('q' to quit)-----: ")
while(userOption != 'q'):
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
    willMeetMondays = False
    willMeetTuesdays = False
    willMeetWednesdays = False
    willMeetThursdays = False
    willMeetFridays = False
    classDays = input("Enter class days (Classes that meet on Tues & Thurs enter as TR, Mon Wed and Fri as MWF): ")
    if('M' in classDays):
        willMeetMondays = True
    if('T' in classDays):
        willMeetTuesdays = True
    if('W' in classDays):
        willMeetWednesdays = True
    if('R' in classDays):
        willMeetThursdays = True
    if('F' in classDays):
        willMeetFridays = True
    classLocation = input("Enter class location: ")
    classSeatsActual = input("Enter amount of seats in class: ")
    classSeatsActual = int(classSeatsActual)
    classCredit = input("Enter number of credits class is worth: ")
    classCredit = int(classCredit)
    classProf = input("Enter last name of professor: ")
    linkedClasses = []
    userOptions6 = input("Enter linked section CRNs. ('q' to quit): ")
    while(userOptions6 != "q"):
        linkedClasses.append(userOptions6)
        print(linkedClasses)
        userOptions6 = input("Enter add. linked section CRNs. ('q' to quit): ")

    potentialClass = Class(courseName=className, classType=classTyping, sectionNum=classSection,
                          CRN=classCRN, startTime=classStartTime, endTime=classEndTime, meetsOnMonday=willMeetMondays,
                         meetsOnTuesday=willMeetTuesdays, meetsOnWednesday=willMeetWednesdays, meetsOnThursday=willMeetThursdays,
                        meetsOnFriday=willMeetFridays, classLoc=classLocation, seatsOpen=classSeatsActual,
                       seatsActual=classSeatsActual, creditAmt=classCredit, prof=classProf, linkedSections=linkedClasses)
    print("Pass")
    db.collection(u'classes').document(str(classCRN)).set(potentialClass.to_dict())
    print("Added new class to collection in Firebase.")
    userOption = input("+++++Press any key to enter another class. (or 'q' to quit)+++++: ")



