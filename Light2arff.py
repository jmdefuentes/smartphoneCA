#############################
#Authors: Lorena González-Manzano and José María de Fuentes
#University Carlos III of Madrid
#February 2018
##############################
import csv
import sys
#Dir of file Light.csv to process
dir = sys.argv[1]
dircsv = dir + '\Light.csv'
#Output a file Light.arff
dirarff = dir + '\Light.arff'

with open(dircsv) as infile:
    with open(dirarff,'wb') as outfile:
		outfile.write("@RELATION light\n")
		outfile.write("@ATTRIBUTE UserId real\n")
		outfile.write("@ATTRIBUTE Lightaccuracy real\n")
		outfile.write("@ATTRIBUTE Lightlux real\n")
		outfile.write("@DATA\n")
		#This is used to not include headers
		first_line = infile.readline()
		listUsers=[]
		contLine=0
		for line in infile:
			contLine=contLine+1
			#For all users...
			if line.split(",")[0].strip() not in listUsers:
				listUsers.extend([line.split(",")[0].strip()])
				idUser = 1
				idString= line.split(",")[0].strip()
				for ch in range(0, len(idString)):
					#The position is added to avoid the existence of equal id users
					idUser= idUser+ int(ord(idString[ch])) + ch					
				#In this case the first is the UserId but converted to a number regarding position in listUsers, second  Light_accuracy and third Light_lux
				if line.split(",")[3].strip() != 'null' and line.split(",")[4].strip()!= 'null':
					outfile.write(str(idUser)+","+line.split(",")[3].strip()+","+line.split(",")[4].strip()+"\n")
			elif (line.split(",")[0].strip() in listUsers):
				idUser = 1
				idString= line.split(",")[0].strip()
				for ch in range(0, len(idString)):
					#The position is added to avoid the existence of equal id users
					idUser= idUser+ int(ord(idString[ch])) + ch					
				if line.split(",")[3].strip() != 'null' and line.split(",")[4].strip()!= 'null':
					outfile.write(str(idUser)+","+line.split(",")[3].strip()+","+line.split(",")[4].strip()+"\n")

				