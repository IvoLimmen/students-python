from domain import Course
from domain import Student

def help():
  print("Grading system")
  print("add-student [name] - Add student")
  print("select-student [name] - Select a student")
  print("add-grade [course] [grade] - Add a grade for a course for the current selected student")
  print("end - Stop the program")

student = None
students = []

while True:
  command = input("Input command:")
  if not command:
    print('Please enter a valid command')
    help()
  elif command == 'help':
    help()
  elif command == 'end' or command == 'quit':
    break
  elif command.startswith("add-student"):
    name = command[11:].strip()
    student = Student(name)
    students.append(student)
  elif command.startswith("select-student"):
    name = command[14:].strip()
    student = next((x for x in students if x.name == name), None)
    if student:
      print("Student {0} is selected".format(name))
    else:
      print("Student {0} was not found".format(name))
  elif command.startswith("add-grade"):
    args = command[9:].strip().split(" ")
    if student:
      student.add_grade(args[0], float(args[1]))
    else:
      print("No student selected")

for s in students:
  s.totals()