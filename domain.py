class Course:

  def __init__(self, name):
    self.name = name
    self.grades = []

  def add_grade(self, grade):
    self.grades.append(grade)

  def total(self):
    l = len(self.grades)
    t = sum(self.grades)
    avg = t / l
    print('{0} - {1} exams - {2} avg'.format(self.name, l, avg));    

class Student:

  def __init__(self, name):
    self.name = name
    self.courses = []

  def add_grade(self, course, grade):    
    c = next((x for x in self.courses if x.name == course), None)
    
    if not c:
      c = Course(course)
      self.courses.append(c)

    c.add_grade(grade)

  def totals(self):
    print('Grades for {0}'.format(self.name))
    for c in self.courses:
      c.total()
