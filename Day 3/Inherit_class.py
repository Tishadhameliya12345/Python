# Simple example of Inheritance of Class
# create a Parant class
class MyClass:
    def __init__(self,sname,rollno):
        self.sname=sname
        self.rollno=rollno
     
    #Method   
    def info(self):
        print(self.sname,self.rollno)
        
class Student(MyClass):
    #pass
    def __init__(self, sname, rollno,year):
    #   MyClass.__init__(self,sname, rollno) # inharit perent class __init__ method 
        super().__init__(sname,rollno) # use super keyword
        self.passyear=year # add properties
    
    #add method    
    def welcome(self):
        print("Welcome",self.sname,"to the class of",self.passyear)
        
a=Student("Tisha","1234","2023")
a.info()
#print(a.passyear) # add properties
a.welcome() # method call