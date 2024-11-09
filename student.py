 # Display student details
  class StudentDetails:
    def__init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def display(self):
        print("STUDENT DETAILS")
        print("FULL NAME :",self.firstname,self.lastname)

#collecting student details from user input
firstname=input("Enter the student first name :")
lastname=input("Enter last name :")

#Creating a student object
student=StudentDetails(firstname,lastname)

#Displaying the stored student details
StudentDetails.display()