class Department:
    def __init__(self, name='ChE Department', sections=5):
        self.name = name
        self.sections = sections
        self.students = []

    def add_students(self, *student_counts):
        self.students.extend(student_counts)

    def average_students_per_section(self):
        if len(self.students) == 0:
            return 0
        return sum(self.students) / self.sections

    def merge_Department(self, *departments):
        merged_count = 0
        for dept in departments:
            merged_count += dept.sections
            self.students.extend(dept.students)
        self.sections += merged_count

        merged_departments = ''
        for dept in departments:
            merged_departments += dept.name + ', '
        merged_departments = merged_departments.rstrip(', ')
        merge_statement = "{} is merged to {}.".format(merged_departments, self.name)
        return merge_statement
    
    
    
    

# Example usage
print('1-----------------------------------')
d1 = Department()
print('The ChE Department has {} sections.'.format(d1.sections))
print('2-----------------------------------')
d2 = Department('MME Department')
print('The {} has {} sections.'.format(d2.name, d2.sections))
print('3-----------------------------------')
d3 = Department('NCE Department', 8)
print('The {} has {} sections.'.format(d3.name, d3.sections))
print('4-----------------------------------')
d1.add_students(12, 23, 12, 34, 21)
print('The {} has an average of {} students in each section.'.format(d1.name, d1.average_students_per_section()))
print('5-----------------------------------')
d2.add_students(40, 30, 21)
if d2.sections == 3:
    print('The {} has an average of {} students in each section.'.format(d2.name, d2.average_students_per_section()))
else:
    print('The {} doesn\'t have 3 sections.'.format(d2.name))
print('6-----------------------------------')
d3.add_students(12, 34, 41, 17, 30, 22, 32, 51)
print('The {} has an average of {} students in each section.'.format(d3.name, d3.average_students_per_section()))
print('7-----------------------------------')
mega = Department('Engineering Department', 10)
print('The {} has {} sections.'.format(mega.name, mega.sections))
print('8-----------------------------------')
mega.add_students(21, 30, 40, 36, 10, 32, 27, 51, 45, 15)
print('The {} has an average of {} students in each section.'.format(mega.name, mega.average_students_per_section()))
print('9-----------------------------------')
print(mega.merge_Department(d1, d2))
print('The {} has an average of {} students in each section.'.format(mega.name, mega.average_students_per_section()))
print('9-----------------------------------')
print(mega.merge_Department(d3))
print('The {} has an average of {} students in each section.'.format(mega.name, mega.average_students_per_section()))
