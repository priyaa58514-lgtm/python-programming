class stud:
    def __init__ (self,a,b,c,m1,m2,m3):
        self.sno=a
        self.name=b
        self.age=c
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def calculate(self):
        self.tot=self.mark1+self.mark2+self.mark3
        self.avg=self.tot/3
        if self.mark1>=40 and self.mark2>=40 and self.mark3>=40:
            self.result="pass"
        else:
            self.result="fail"
              
    def display(self):
        print("student number:",self.sno)
        print("student name:",self.name)
        print("studnet age:",self.age)
        print("mark1",self.mark1)
        print("mark2:",self.mark2)
        print("mark3:",self.mark3)
        print("total:",self.tot)
        print("average:",self.avg)

x=int(input("enter the student number:"))
y=input("enter the student name:")
z=int(input("enter the student age:"))
m1=int(input("enter mark1:"))
m2=int(input("enter m2:"))
m3=int(input("enter m3:"))

obj=stud(x,y,z,m1,m2,m3)
obj.calculate()
obj.display()
