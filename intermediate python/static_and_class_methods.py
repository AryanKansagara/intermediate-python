class Person:
	Population = 501
	def __init__(self,name,age):
		self.name = name
		self.age = age
	@classmethod#-->you can call it on the class no need for object
	def getPopulation(cls):
		return cls.Population

	@staticmethod#-->this is just a normal function
	def isAdult(age):
		return age >=18

	def display(self):
		print(self.name,'is',self.age,'years old')

newPerson = Person("ARYAN",16)			
print(Person.getPopulation())			
Person.Population = 12 #-->this will chenge the population variable defined in the class
print(Person.getPopulation())	
print(Person.isAdult(5))#-->returns False