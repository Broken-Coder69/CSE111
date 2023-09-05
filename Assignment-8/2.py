class Exam:
    def __init__(self,marks):
        self.marks = marks
        self.time = 60
        
    def examSyllabus(self):
        return "Maths , English"
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"
    
    
    
    
 
class ScienceExam(Exam):
    def __init__(self, marks, time, *args):
        super().__init__(marks)
        self.time = time
        self.args = args
        
        self.count = 2
        self.count += len(self.args)
        
        self.sub_list = list(args)
        
        
    def __str__(self):
        return (f"Marks: {self.marks} Time: {self.time} minutes Number of Parts: {self.count}")
        

    
    def examSyllabus(self):
        new_syllabus =  super().examSyllabus()
        
        for i in self.sub_list:
            new_syllabus += ", " + i
        
        return new_syllabus

    
    
    
    def examParts(self):
        parts = super().examParts()
        for i in range (len(self.sub_list)):
            parts += f"part {3 + i} - {self.sub_list[i]} \n"
    
    
        return parts
    
    
    
    
engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================') 
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())