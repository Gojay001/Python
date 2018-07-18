#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class University(object):
	"""docstring for University"""
	pass

class ComputerScienceCollege(University):
	"""docstring for ComputerScienceCollege"""
	def  __init__(self):
		pass
		
	class CS:
		"""docstring for CS"""
		__location = "apartment 2"
		__course = ['big data', 'database', 'programing']
		__population = 0
		def __init__(self, population):
			self.__population = population
		
		def teach(self):
			print("CS teaching") 
			
		def exam(self):
			print("CS examing")

		def get_location(self):
			return self.__location

		def set_lcoation(self, location):
			self.__location = location

		def get_course(self):
			return self.__course

		def set_course(self, course):
			self.__course = course

		def get_population(self):
			return self.__population

		def set_population(self, population):
			self.__population = population

	class IS:
		"""docstring for IS"""
		__location = "apartment 2"
		__course = ['network security', 'cryptography', 'programing']
		__population = 0
		def __init__(self, population):
			self.__population = population
		
		def teach(self):
			print("IS teaching")
			
		def exam(self):
			print("IS examing")

		def get_location(self):
			return self.__location

		def set_lcoation(self, location):
			self.__location = location

		def get_course(self):
			return self.__course

		def set_course(self, course):
			self.__course = course

		def get_population(self):
			return self.__population

		def set_population(self, population):
			self.__population = population

if __name__ == '__main__':
	#ComputerScienceCollege.IS(120).teach()
	college = ComputerScienceCollege()
	profession = college.IS(120)
	profession.teach()