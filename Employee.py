# Title: Employee Class
# Author: Dalila Spencer
# Date: 2025-11-6

# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.


class Employee:
    def __init__(self, name, id_num, dep, job):
        self.name = name
        self.id_num = id_num
        self.dep = dep
        self.job = job

    def get_info(self):
       return self.name + '\t' + self.id_num + '\t' + self.dep + '\t' + self.job

employee1 = Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
employee2 = Employee('Mark Jones', '39119', 'IT', 'Programmer')
employee3 = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

for num in [employee1, employee2, employee3]:
    print(num.get_info())

