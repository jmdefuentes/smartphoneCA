#############################
#Authors: Lorena González-Manzano and José María de Fuentes
#University Carlos III of Madrid
#February 2018
##############################

import csv
import sys
import os

#Dir to File to process - The downloaded one from Sherlock database
dir = sys.argv[1]
#Moriarty is processed to remove all lines related to it...that is we want "clean" data
dircsvMoriarty = dir + '\Moriarty.csv'
dircsvToProcess = sys.argv[2]
dircsvToProcessResult = sys.argv[3]

#this is used to identify the row of T3 and Battery which are closed to each other, for instance UUIDT3=500 and UUIDB=450
with open(dircsvMoriarty) as infile, open(dircsvToProcess) as infile2:
    with open(dircsvToProcessResult,'wb') as outfile:
	counterM=1
	counter=1
	endM=True
	end=True
	
	

	#This is used to identify the fact that a UUID is smaller than a UUIDM and then, we need to processed a new line of Moriarty file but not the other file (we remain in the same line)
	notMove=1
	
	endM=True
	end=True

	#to remove headers
	line= infile.next()
	line2= infile2.next()
	#to write headers in the outputfile
	outfile.write(line2)
	cont = 0
	while endM:
		cont= cont +1
		try:
			line= infile.next()	
			#print line
			#We are interested in those of Moriarty lines which are malicious because the benign ones we do not remove them--this can be change in case either
			#benign or malicious entries want to be removed
			if line.split(",")[5].strip() == 'malicious':
					end=True
					while end:
						try:
							if notMove==1:
								line2= infile2.next()
							elif notMove==0:
								notMove=1
							UUIDmoriarty=int(float(line.split(",")[1].strip()))
							
							UUID=int(float(line2.split(",")[1].strip()))
							#print counterAlreadyStored, (counterAlreadyStored not in listAlreadyStored)
							#If the UserId and the UUID  match, the line from the processed file is stored in the output file
							if ( (UUID-100) < UUIDmoriarty and (UUID+100)>= UUIDmoriarty and line.split(",")[0].strip()==line2.split(",")[0].strip()):
								#don't do anything because in this line Moriarty is found!! Malware found!
								print UUID, UUIDmoriarty, line.split(",")[0].strip(),line2.split(",")[0].strip()
							#Here UUIDMoriarty always is going to be smaller than UUIDAnyFile (because it has been previous processed). But if UUIDMoriarty is too much smaller, the following UUIDMoriarty has to be processed
								end=False
							elif UUIDmoriarty < UUIDmoriarty-100:
								#In the UUIDMoriarty is very far from the one processed, you can stop and change to another UUIDMoriarty
								end=False
								notMove=0
							else:
								#It means that this line does not contain Moriarty
								outfile.write(line2)
						except StopIteration:
							end=False
							endM=False
		except StopIteration:
				endM=False
	outfile.close()
	if cont==1:
		#This means that Moriarty is empty and then, no file should be created.
		os.remove(dircsvToProcessResult)
					
						
						
