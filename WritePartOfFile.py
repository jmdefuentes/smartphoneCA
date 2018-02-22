#############################
#Authors: Lorena González-Manzano and José María de Fuentes
#University Carlos III of Madrid
#February 2018
##############################
import csv

import os
import csv
import sys

import re
import math, string, fileinput

def partOfFile(file,fromLine, toLine):
	linecounter2=0
	cont2=0
	result=""
	with open(file) as infile2:
		for line2 in infile2:
			if cont2 < toLine and cont2>=fromLine:
				linecounter2 = linecounter2 +1
				result = result +line2
			elif cont2 > toLine:
				break
			cont2 = cont2 +1

	return linecounter2,result
	
def partOfFileAudioLight(file,fromLine, toLine,line, linesToAdd):
	linecounter2=0
	cont2=0
	result=""
	elem2=0
	with open(file) as infile2:
		for line2 in infile2:
			if cont2 < toLine and cont2>=fromLine:
				linecounter2 = linecounter2 +1
				line2AuxL = []
				elem=""
				if cont2 ==100:
					for x in range(0, 23):
						if x==0:
							elem2 = line2.split(",")[0].strip() 
						else: 
							elem = line.split(",")[x].strip() 
							elem2 = line2.split(",")[x].strip() 
							elem2Aux = abs(float(elem)-float(elem2))
							if float(elem)>float(elem2) :
								elem2 = elem2Aux * -1
							elif float(elem)==float(elem2):
								elem2 = -999999 #It means that they are equal and it should not change
							else:
								elem2 = elem2Aux   
						line2AuxL.append(elem2)
						print elem2
					for i in range(1,linesToAdd):
						for j in range(0, 23): 
							if j==0:
								line2Aux= line2.split(",")[0].strip()+"," #This is to include the userId which does not change
							else:
								if line2AuxL[j] != -999999:
									#This considering float numbers
									line2Aux +=str((( float(line.split(",")[j].strip()) + ((float(line2AuxL[j])/linesToAdd)*(i)))))
									
								else:
									line2Aux +=line2.split(",")[j].strip() 
								if j !=22: # In the last case , is not needed
									line2Aux +=","
								elif x==22:
									line2Aux +="\n"
						result = result + line2Aux
					result = result + line2 #The first line of file should be added
				else:
					line3Aux = ""
					for t in range(0, 23):
						if t==0:
							line3Aux= line2.split(",")[0].strip() #This is to include the userId which does not change					
						else: #This is to remove field battery present
							line3Aux +=line2.split(",")[t].strip()
						if t !=22: # In the last case , is not needed
							line3Aux +=","
						elif t==22:
							line3Aux +="\n"							
					result = result + line3Aux 
			elif cont2 > toLine:
				break
			cont2 = cont2 +1

	return linecounter2,result
	
def partOfFileAudioLightSameUser(file,fromLine, toLine,line, linesToAdd):
	linecounter2=0
	cont2=0
	result=""
	elem2=0
	#The ID should be different even been the same user
	with open(file) as infile2:
		for line2 in infile2:
			if cont2 < toLine and cont2>=fromLine:
				linecounter2 = linecounter2 +1
				line2AuxL = []
				elem=""
				lineFirstWithoutId=""
				if cont2 ==100:
					for x in range(0, 23):
						if x==0:
							elem2 = line2.split(",")[0].strip() 
							lineFirstWithoutId = str(int(line2.split(",")[0].strip() )+100)
						else: 
							lineFirstWithoutId += line2.split(",")[x].strip() 
							elem = line.split(",")[x].strip() 
							elem2 = line2.split(",")[x].strip() 
							elem2Aux = abs(float(elem)-float(elem2))
							if float(elem)>float(elem2) :
								elem2 = elem2Aux * -1
							elif float(elem)==float(elem2):
								elem2 = -999999 #It means that they are equal and it should not change
							else:
								elem2 = elem2Aux   
						line2AuxL.append(elem2)
						print elem2
					for i in range(1,linesToAdd):
						for j in range(0, 23): 
							if j==0:
								line2Aux= str(int(line2.split(",")[0].strip())+100)+"," #This is to include the userId which does not change
							else:
								if line2AuxL[j] != -999999:
									#This considering float numbers
									line2Aux +=str((( float(line.split(",")[j].strip()) + ((float(line2AuxL[j])/linesToAdd)*(i)))))
									
								else:
									line2Aux +=line2.split(",")[j].strip() 
								if j !=22: # In the last case , is not needed
									line2Aux +=","
								elif x==22:
									line2Aux +="\n"
						result = result + line2Aux
					result = result + lineFirstWithoutId #The first line of file should be added
						#print result
				else:
					line3Aux = ""
					for t in range(0, 23):
						if t==0:
							line3Aux= str(int(line2.split(",")[0].strip())+100) #This is to include the userId which does not change					
						else: #This is to remove field battery present
							line3Aux +=line2.split(",")[t].strip()
						if t !=22: # In the last case , is not needed
							line3Aux +=","
						elif t==22:
							line3Aux +="\n"							
					result = result + line3Aux 
			elif cont2 > toLine:
				break
			cont2 = cont2 +1

	return linecounter2,result	
	
	
def partOfFileBattery(file,fromLine, toLine, line, linesToAdd):
	linecounter2=0
	cont2=0
	result=""
	elem2=0
	with open(file) as infile2:
		for line2 in infile2:
			if cont2 < toLine and cont2>=fromLine:
				linecounter2 = linecounter2 +1
				line2AuxL = []
				if cont2 ==100:
					for x in range(0, 11):
						if x==0:
							elem2 = line2.split(",")[0].strip() 
						elif x!=6: 
							elem = line.split(",")[x].strip() 
							elem2 = line2.split(",")[x].strip() 
							elem2Aux = abs(float(elem)-float(elem2))
							if elem>elem2:
								elem2 = elem2Aux 
							elif elem==elem2:
								elem2 = -999999 #It means that they are equal and it should not change
							else:
								elem2 = elem2Aux  * -1
						line2AuxL.append(elem2)
					for i in range(1,linesToAdd):
						for j in range(0, 11): 
							if j==0:
								line2Aux= line2.split(",")[0].strip()+"," #This is to include the userId which does not change
							elif j!=6:
								if line2AuxL[j] != -999999:
									#This in the form of integers
									line2Aux +=str(int(math.floor( float(line2.split(",")[j].strip()) + ((float(line2AuxL[j])/linesToAdd)*(linesToAdd-i)))))
								else:
									line2Aux +=line2.split(",")[j].strip() 
								if j !=10 and j!=6: # In the last case , is not needed
									line2Aux +=","
								elif x==10:
									line2Aux +="\n"
						result = result + line2Aux
					#The first line of file should be added	
					line3Aux = ""
					for t in range(0, 11):
						if t==0:
							line3Aux= line2.split(",")[0].strip() #This is to include the userId which does not change					
						elif t!=6: #This is to remove field battery present
							line3Aux +=line2.split(",")[t].strip()
						if t !=10 and t!=6: # In the last case , is not needed
							line3Aux +=","
						elif t==10:
							line3Aux +="\n"								
					result = result + line3Aux 
				else:
					line3Aux = ""
					for t in range(0, 11):
						if t==0:
							line3Aux= line2.split(",")[0].strip() #This is to include the userId which does not change					
						elif t!=6: #This is to remove field battery present
							line3Aux +=line2.split(",")[t].strip()
						if t !=10 and t!=6: # In the last case , is not needed
							line3Aux +=","
						elif t==10:
							line3Aux +="\n"							
					result = result + line3Aux 
			elif cont2 > toLine:
				break
			cont2 = cont2 +1

	return linecounter2,result
	
def partOfFileBatterySameUser(file,fromLine, toLine, line, linesToAdd):
	linecounter2=0
	cont2=0
	result=""
	elem2=0
	with open(file) as infile2:
		for line2 in infile2:
			if cont2 < toLine and cont2>=fromLine:
				linecounter2 = linecounter2 +1
				line2AuxL = []
				if cont2 ==100:
					for x in range(0, 11):
						if x==0:
							elem2 = str(int(line2.split(",")[0].strip())+100)
						elif x!=6: 
							elem = line.split(",")[x].strip() 
							elem2 = line2.split(",")[x].strip() 
							elem2Aux = abs(float(elem)-float(elem2))
							if elem>elem2:
								elem2 = elem2Aux 
							elif elem==elem2:
								elem2 = -999999 #It means that they are equal and it should not change
							else:
								elem2 = elem2Aux  * -1
						line2AuxL.append(elem2)
					for i in range(1,linesToAdd):
						for j in range(0, 11): 
							if j==0:
								line2Aux= str(int(line2.split(",")[0].strip())+100)+"," #This is to include the userId which does not change
							elif j!=6:
								if line2AuxL[j] != -999999:
									#This in the form of integers
									line2Aux +=str(int(math.floor( float(line2.split(",")[j].strip()) + ((float(line2AuxL[j])/linesToAdd)*(linesToAdd-i)))))

								else:
									line2Aux +=line2.split(",")[j].strip() 
								if j !=10 and j!=6: # In the last case , is not needed
									line2Aux +=","
								elif x==10:
									line2Aux +="\n"
						result = result + line2Aux

					#The first line of file should be added	
					line3Aux = ""
					for t in range(0, 11):
						if t==0:
							line3Aux= str(int(line2.split(",")[0].strip())+100) #This is to include the userId which does not change					
						elif t!=6: #This is to remove field battery present
							line3Aux +=line2.split(",")[t].strip()
						if t !=10 and t!=6: # In the last case , is not needed
							line3Aux +=","
						elif t==10:
							line3Aux +="\n"								
					result = result + line3Aux 
				else:
					line3Aux = ""
					for t in range(0, 11):
						if t==0:
							line3Aux= str(int(line2.split(",")[0].strip())+100) #This is to include the userId which does not change					
						elif t!=6: #This is to remove field battery present
							line3Aux +=line2.split(",")[t].strip()
						if t !=10 and t!=6: # In the last case , is not needed
							line3Aux +=","
						elif t==10:
							line3Aux +="\n"							
					result = result + line3Aux 
			elif cont2 > toLine:
				break
			cont2 = cont2 +1

	return linecounter2,result
		
	
def partOfFileAudioLightBattery(file,fromLine, toLine, line, linesToAdd):
	linecounter2=0
	cont2=0
	result=""
	elem2=0
	with open(file) as infile2:
		for line2 in infile2:
			if cont2 < toLine and cont2>=fromLine:
				linecounter2 = linecounter2 +1
				line2AuxL = []
				if cont2 ==100:
					for x in range(0, 31):
						if x==0:
							elem2 = line2.split(",")[0].strip()
						elif x!=28: 
							elem = line.split(",")[x].strip() 
							elem2 = line2.split(",")[x].strip() 
							elem2Aux = abs(float(elem)-float(elem2))
							if float(elem)>float(elem2):
								elem2 = elem2Aux  * -1
							elif elem==elem2:
								elem2 = -999999 #It means that they are equal and it should not change
							else:
								elem2 = elem2Aux 
						line2AuxL.append(elem2)
					for i in range(1,linesToAdd):
						for j in range(0, 31): 
							if j==0:
								line2Aux= line2.split(",")[0].strip()+"," #This is to include the userId which does not change
							elif j!=28:
								if line2AuxL[j] != -999999:
									#This considering float numbers
									line2Aux +=str((( float(line.split(",")[j].strip()) + ((float(line2AuxL[j])/linesToAdd)*(i)))))
								else:
									line2Aux +=line2.split(",")[j].strip() 
								if j !=30 and j!=28: # In the last case , is not needed
									line2Aux +=","
								elif x==30:
									line2Aux +="\n"
						result = result + line2Aux
					line3Aux = ""
					for t in range(0, 31):
						if t==0:
							line3Aux= line2.split(",")[0].strip() #This is to include the userId which does not change					
						elif t!=28: #This is to remove field battery present
							line3Aux +=line2.split(",")[t].strip()
						if t !=30 and t!=28: # In the last case , is not needed
							line3Aux +=","
						elif t==30:
							line3Aux +="\n"							
					result = result + line3Aux 
				else:
					line3Aux = ""
					for t in range(0, 31):
						if t==0:
							line3Aux= line2.split(",")[0].strip() #This is to include the userId which does not change					
						elif t!=28: #This is to remove field battery present
							line3Aux +=line2.split(",")[t].strip()
						if t !=30 and t!=28: # In the last case , is not needed
							line3Aux +=","
						elif t==30:
							line3Aux +="\n"							
					result = result + line3Aux 
			elif cont2 > toLine:
				break
			cont2 = cont2 +1

	return linecounter2,result	
	
def partOfFileAudioLightBatterySameUser(file,fromLine, toLine, line, linesToAdd):
	linecounter2=0
	cont2=0
	result=""
	elem2=0
	with open(file) as infile2:
		for line2 in infile2:
			if cont2 < toLine and cont2>=fromLine:
				linecounter2 = linecounter2 +1
				line2AuxL = []
				if cont2 ==100:
					for x in range(0, 31):
						if x==0:
							elem2 = str(int(line2.split(",")[0].strip())+100)
						elif x!=28: 
							elem = line.split(",")[x].strip() 
							elem2 = line2.split(",")[x].strip() 
							elem2Aux = abs(float(elem)-float(elem2))
							if float(elem)>float(elem2):
								elem2 = elem2Aux  * -1
							elif elem==elem2:
								elem2 = -999999 #It means that they are equal and it should not change
							else:
								elem2 = elem2Aux 
						line2AuxL.append(elem2)
					for i in range(1,linesToAdd):
						for j in range(0, 31): 
							if j==0:
								line2Aux= str(int(line2.split(",")[0].strip())+100)+"," #This is to include the userId which does not change
							elif j!=28:
								if line2AuxL[j] != -999999:
									#This considering float numbers
									line2Aux +=str((( float(line.split(",")[j].strip()) + ((float(line2AuxL[j])/linesToAdd)*(i)))))
								else:
									line2Aux +=line2.split(",")[j].strip() 
								if j !=30 and j!=28: # In the last case , is not needed
									line2Aux +=","
								elif x==30:
									line2Aux +="\n"
						result = result + line2Aux
					line3Aux = ""
					for t in range(0, 31):
						if t==0:
							line3Aux= str(int(line2.split(",")[0].strip())+100) #This is to include the userId which does not change					
						elif t!=28: #This is to remove field battery present
							line3Aux +=line2.split(",")[t].strip()
						if t !=30 and t!=28: # In the last case , is not needed
							line3Aux +=","
						elif t==30:
							line3Aux +="\n"							
					result = result + line3Aux 
				else:
					line3Aux = ""
					for t in range(0, 31):
						if t==0:
							line3Aux= str(int(line2.split(",")[0].strip())+100) #This is to include the userId which does not change					
						elif t!=28: #This is to remove field battery present
							line3Aux +=line2.split(",")[t].strip()
						if t !=30 and t!=28: # In the last case , is not needed
							line3Aux +=","
						elif t==30:
							line3Aux +="\n"							
					result = result + line3Aux 
			elif cont2 > toLine:
				break
			cont2 = cont2 +1

	return linecounter2,result		
	
	
	
	