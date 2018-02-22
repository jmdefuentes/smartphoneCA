#############################
#Authors: Lorena González-Manzano and José María de Fuentes
#University Carlos III of Madrid
#February 2018
##############################
import csv

import os
import csv
import sys

from WritePartOfFile import partOfFileBattery

##############Parameters#########
#infile the largest file (file to write)----File arff from which read data
file1 = sys.argv[1]
#infile2 the smallest file----File arff from which read data
file2 = sys.argv[2]
#Output arff file that contains file1 and file2 
fileResult = sys.argv[3]

with open(fileResult,'wb') as outfile:		
	outfile.write("@RELATION battery\n")
	outfile.write("@ATTRIBUTE UserId real\n")
	outfile.write("@ATTRIBUTE Battery_charge_type real\n")
	outfile.write("@ATTRIBUTE Battery_health real\n")
	outfile.write("@ATTRIBUTE Battery_level real\n")
	outfile.write("@ATTRIBUTE Battery_online real\n")
	outfile.write("@ATTRIBUTE Battery_plugged real\n")		
	outfile.write("@ATTRIBUTE Battery_scale real\n")
	outfile.write("@ATTRIBUTE Battery_status real\n")
	outfile.write("@ATTRIBUTE Battery_temperature real\n")
	outfile.write("@ATTRIBUTE Battery_voltage real\n")
	
	outfile.write("@DATA\n")

	cont1=0
	cont2=0
	th= (sys.argv[4]) #argv[3] refers to the number of files of first user (file)
	th2= (sys.argv[5] )#argv[4] refers to the number of files of second user (file)
	contEndFile=1
	linesToAdd= int(sys.argv[6]) +1

	#1000 lines of file2 header are removed to avoid inconsistencies
	with open(file1) as infile1:			
		for line in infile1:
			if cont1 <= (int(th)+100) and cont1>100:
				lineAux=""
				for x in range(0, 11): 
					if x!=6: #This is to remove field battery present
						lineAux +=line.split(",")[x].strip()
					if x !=10 and x!=6: # In the last case , is not needed
						lineAux +=","
					elif x==10:
						lineAux +="\n"
				outfile.write(lineAux)
				cont1 = cont1 +1
			elif cont1<=100:
				cont1 = cont1 +1
			else:
				#These lines are used to not loose a line of infile1
				lineAux=""
				for x in range(0, 11): 
					if x!=6: #This is to remove field battery present
						lineAux +=line.split(",")[x].strip()
					if x !=10 and x!=6: # In the last case , is not needed
						lineAux +=","
					elif x==10:
						lineAux +="\n"
				outfile.write(lineAux)			
				[linecounter2,linesToWrite]= partOfFileBattery(file2,100,int(th2)+100,line,(linesToAdd))
				outfile.write(linesToWrite)
				contEndFile = contEndFile +1
			if contEndFile==2:
				break				
						
		

