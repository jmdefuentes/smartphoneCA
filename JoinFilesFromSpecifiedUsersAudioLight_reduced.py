#############################
#Authors: Lorena González-Manzano and José María de Fuentes
#University Carlos III of Madrid
#February 2018
##############################
import csv

import os
import csv
import sys

from WritePartOfFile import partOfFileAudioLight

##############Parameters#########
#infile the largest file (file to write)----File arff from which read data
file1 = sys.argv[1]
#infile2 the smallest file----File arff from which read data
file2 = sys.argv[2]
#Output arff file that contains file1 and file2 
fileResult = sys.argv[3]

with open(fileResult,'wb') as outfile:	
	outfile.write("@RELATION audiolight\n")
	outfile.write("@ATTRIBUTE UserId real\n")
	outfile.write("@ATTRIBUTE Audio_diffSecs real\n")
	outfile.write("@ATTRIBUTE Audio_l1Norm real\n")
	outfile.write("@ATTRIBUTE Audio_l2Norm real\n")
	outfile.write("@ATTRIBUTE Audio_linfNorm real\n")
	outfile.write("@ATTRIBUTE AudPSD_AcrossFreqBands0 real\n")
	outfile.write("@ATTRIBUTE AudPSD_AcrossFreqBands1 real\n")
	outfile.write("@ATTRIBUTE AudPSD_AcrossFreqBands2 real\n")
	outfile.write("@ATTRIBUTE AudPSD_AcrossFreqBands3 real\n")
	outfile.write("@ATTRIBUTE Audio_mfccs0 real\n")		
	outfile.write("@ATTRIBUTE Audio_mfccs1 real\n")
	outfile.write("@ATTRIBUTE Audio_mfccs2 real\n")
	outfile.write("@ATTRIBUTE Audio_mfccs3 real\n")
	outfile.write("@ATTRIBUTE Audio_mfccs4 real\n")
	outfile.write("@ATTRIBUTE Audio_mfccs5 real\n")
	outfile.write("@ATTRIBUTE Audio_mfccs6 real\n")
	outfile.write("@ATTRIBUTE Audio_mfccs7 real\n")
	outfile.write("@ATTRIBUTE Audio_mfccs8 real\n")
	outfile.write("@ATTRIBUTE Audio_mfccs9 real\n")
	outfile.write("@ATTRIBUTE Audio_mfccs10 real\n")		
	outfile.write("@ATTRIBUTE Audio_mfccs11 real\n")
	outfile.write("@ATTRIBUTE Lightaccuracy real\n")
	outfile.write("@ATTRIBUTE Lightlux real\n")
	outfile.write("@DATA\n")	
	cont1=0
	cont2=0
	th= (sys.argv[4]) #argv[3] refers to the number of files of first user (file)
	th2= (sys.argv[5] )#argv[4] refers to the number of files of second user (file)
	contEndFile=1
	linesToAdd= int(sys.argv[6]) +1

	with open(file1) as infile1:			
		for line in infile1:
			if cont1 <= (int(th)+100) and cont1>100:
				outfile.write(line)
				cont1 = cont1 +1
			elif cont1<=100:
				cont1 = cont1 +1
			else:
				#These lines are used to not loose a line of infile1
				outfile.write(line)			
				[linecounter2,linesToWrite]= partOfFileAudioLight(file2,100,int(th2)+100,line, linesToAdd)
				outfile.write(linesToWrite)
				contEndFile = contEndFile +1
			if contEndFile==2:
				break
	
		
		
	


