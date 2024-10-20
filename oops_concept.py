# Defined the function
def greet():
  print("Hello how are you")
  print("My name is jarvis")
  print("may i know your name : ")
  name = input()

# Calling the function in order to ececute
greet()

class student():
  name = ""
  age = 12
  school_class = "year 7"
  color = "red"
  teacher_name = "Ms Smith" 

  # constructor class
  def __init__(self):
    print("making a new student")

  def change_details(self):
    print("please enter your age : ")
    self.age = int(input())
    print("please enter the name of the student")
    self.name = input()



# function to show the details
  def show_details(self):
    print("the details of the students are :")
    print(self.name)
    print(self.age)
    print(self.school_class)
    print(self.color)
    print(self.teacher_name)


abc = student()
abc.change_details()
abc.show_details()
