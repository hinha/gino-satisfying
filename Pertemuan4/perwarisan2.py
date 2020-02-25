class Person( object ):     
  
	def __init__(self, name, idnumber):    
		self.name = name 
		self.idnumber = idnumber 
		
	def display(self): 
		print(self.name) 
		print(self.idnumber) 
  

class Employee( Person ):            
	def __init__(self, name, idnumber, salary, post): 
		self.salary = salary 
		self.post = post 

		Person.__init__(self, name, idnumber)  

	def display(self):
		print(self.name) 
		print(self.idnumber) 
		print(self.salary)
		print(self.post)
                  

a = Person('Rahul', 886012)     
a.display()

print('\n')
b = Employee("Andika", 66127, "4jt", 3)
b.display()