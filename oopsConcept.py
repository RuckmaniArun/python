import csv

csvfile="students_list.csv"
class Student:
    def __init__(self, name, age, classname):
        self.name=name
        if age < 0:
            raise Exception("Age cannot be negative")
        else:
            self.age=age
        self.classname=classname
        self.marks={}
        
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Class: {self.classname}, Marks: {self.marks}"
        
    def get_name(self):
        return self.name
    
    def set_Marks(self, subject, mark):
        if mark < 0:
            raise Exception("Mark can't be negative")
        if subject.strip() == "":
            print("Subject name can't be empty")
        self.marks[subject]=mark
        print("Mark is set")
        
    def get_Marks(self):
        print("Mark is..",self.marks)
        
class GradingSystem:
    def __init__(self):
        self.stud=[]
    
    def add_Student(self, student):
        self.stud.append(student)
        
        
    def update_file(self):
        filename='students_list.csv'
        with open(filename,"w",newline="") as fp:
            writer=csv.writer(fp)
            writer.writerow(["Name","Age","Class","Marks"])
            for s in gs.stud:
                writer.writerow([s.name,s.age,s.classname,s.marks])
            
    def total_marks(self):
        result=0;
        for s in self.stud:
            result=sum(s.marks.values())
            print(f"Total marks of student {s.name} is: {result}")
           
            
        
        
        

try:       
    ruckmani=Student('ruckmani',21,'12th')
    name=ruckmani.get_name()
    print("Name obtained..",name)
    ruckmani.set_Marks('Science',90)
    ruckmani.set_Marks('Maths',90)
    ruckmani.set_Marks('English',90)
    ruckmani.set_Marks('Tamil',90)
    ruckmani.get_Marks()

    radha=Student('radha',21,'12th')
    name=radha.get_name()
    print("Name obtained..",name)
    radha.set_Marks('Science',95)
    radha.set_Marks('Maths',80)
    radha.set_Marks('English',80)
    radha.set_Marks('Tamil',60)
    radha.get_Marks() 
    
except Exception as e:
    print("Error:", e)
    
gs=GradingSystem()
gs.add_Student(ruckmani)
gs.add_Student(radha)

#for s in gs.stud:
#    print(s)

gs.update_file()
gs.total_marks()
