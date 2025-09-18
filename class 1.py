class stud:
    def __init__ (self,a,b,c):
        self.sno=a
        self.name=b
        self.age=c
    def disp(self):
        print(self.sno)
        print(self.name)
        print(self.age)

x=int(input("enter the student number:"))
y=input("enter the student name:")
z=int(input("enter the student age:"))      
ob=stud(x,y,z)
ob.disp()
