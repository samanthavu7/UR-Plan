class Student(object):
    def __init__(self, firstName, lastName, major, year=0, prefList=[], coursesList=[]):
        self.firstName = firstName
        self.lastName = lastName
        self.major = major
        self.year = year
        self.prefList = prefList
        self.coursesList = coursesList

@staticmethod
def from_dict(source):
        # [START_EXCLUDE]
        city = City(source[u'name'], source[u'state'], source[u'country'])

        if u'capital' in source:
            city.capital = source[u'capital']

        if u'population' in source:
            city.population = source[u'population']

        if u'regions' in source:
            city.regions = source[u'regions']

        return city
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {
            u'name': self.name,
            u'state': self.state,
            u'country': self.country
        }

        if self.capital:
            dest[u'capital'] = self.capital

        if self.population:
            dest[u'population'] = self.population

        if self.regions:
            dest[u'regions'] = self.regions

        return dest
        # [END_EXCLUDE]

    def __repr__(self):
        return(
            u'Students(firstName={}, lastName={}, major={}, year={}, prefList={}, coursesList={})'
            .format(self.firstName, self.lastName, self.major, self.year, self.prefList, self.coursesList))

students_ref = db.collection(u'students')
students_ref.document(u'862191102').set(
    Student(u'Xin Yan', u'Chok', u'Computer Engineering', 3,
[u'No Morning', u'No Friday'], [u'CS100', u'CS141', u'CS171’, u'CS179I’]).to_dict())
students_ref.document(u'861291195').set(
    Student(u'Samantha', u'Vu', u'Computer Science', 4, [u'No Monday', u'No Friday'], [u'CS130', u'CS182', u'CS014’, u'SOC128S’]).to_dict())
students_ref.document(u'').set(
    Student(u'Luis', u'Vargas', u'Computer Science', 4, [u'No Evening', u'No Monday'], [u'CS010', u'CS012', u'CS014’, u'CS100’, u'CS153’]).to_dict())
students_ref.document(u'861234567').set(
    Student(u'Mary', u'Jane', u'Chemistry', 1, [u'No Afternoon'], [u'', u'', u'’, u'’]).to_dict())
students_ref.document(u'864651254').set(
    Student(u'Tim', u'Tam', u'Medicine', 1, [u'No Wednesday', u'No Evening'], [u'', u'', u'’, u'’]).to_dict())
students_ref.document(u'867513493').set(
    Student(u'John', u'Paul', u'Civil Engineering', 2, [u'No Afternoon', u'No Evening'], [u'', u'', u'’, u'’]).to_dict())
students_ref.document(u'861643751').set(
    Student(u'Tommy', u'Hilfiger', u'Architecture', 2, [u'', u''], [u'', u'', u'’, u'’]).to_dict())
students_ref.document(u'861545787').set(
    Student(u'Joe', u'Jonas', u'Music', 3, [u'', u''], [u'', u'', u'’, u'’]).to_dict())
students_ref.document(u'861876785').set(
    Student(u'Lily', u'Aldridge', u'Dentistry', 1, [u'No Morning', u''], [u'', u'', u'’, u'’]).to_dict())
students_ref.document(u'861234567').set(
    Student(u'Jerry', u'Lee', u'Business', 3, [u'No Morning', u'No Afternoon'], [u'', u'', u'’, u'’]).to_dict())
