# Create a reference to the students collection
cities_ref = db.collection(u'students')
# Create a query against the collection
query_ref = students_ref.where(u'major', u'==', u'Computer Engineering')
