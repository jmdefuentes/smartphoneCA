#!/usr/bin/python
#############################
#Authors: Lorena González-Manzano and José María de Fuentes
#University Carlos III of Madrid
#February 2018
##############################

import sys
import pandas as pd 
import csv
import os
# USAGE: MobileCAerrorAnalysis.py predictionsFolder outputFolder
folder = str(sys.argv[1])
outputfolder = str(sys.argv[2]) 
linesToConsiderRealAttack = [1,5,10,20]

for filename in os.listdir(folder):


	fullFileName = folder + '/' + filename
	print('Filename: %s' %filename) 
	falsePositive=0
	falseNegative=0
	lineCount=0
	inSequenceFN=0
	inSequenceFP=0
	longestSequenceFN=0
	longestSequenceFP=0
	sequencesFN=[]
	sequencesFP=[]
	predictions=[]
	actuals=[]
	firstErrorFound = 0
	lineFirstError = 0
	firstLineAttackerReal =0
	lineRealAttackDetected = [0,0,0,0]
	attackerDetectedRunLength =0
	if filename.find(".DS_Store") == -1:
		#file name format: 810_910_8000_5000_21_5000_KNN.pred
		realUser,attacker,timeRealUser,timeAttack,kvalue,width,method = filename.split('_')
		
		with open(fullFileName) as f:
			for line in f:
				predicted,real = line.split(',')
				#Building confusion matrix
				predictions.append(predicted)
				actuals.append(real)
				#Analysing the accuracy...
				if int(predicted) != int(real):
					#Then we are in a FP or FN case
					if firstErrorFound == 0 and lineCount!=0:
						#write down the line number of first error
						lineFirstError = lineCount + 1
						firstErrorFound = 1

					if predicted == realUser:
						falseNegative = falseNegative + 1
						inSequenceFN= inSequenceFN + 1
						if inSequenceFP!=0:
							#We were in a run of FPs, and now we are in a FN case, cancel the FP run
							if inSequenceFP>longestSequenceFP:
								longestSequenceFP=inSequenceFP
							sequencesFP.append(inSequenceFP)
							inSequenceFP=0
					else:
						falsePositive = falsePositive + 1
						inSequenceFP= inSequenceFP + 1
						if inSequenceFN!=0:
							#We were in a run of FNs, and now we are in a FP case, cancel the FN run
							if inSequenceFN>longestSequenceFN:
								longestSequenceFN=inSequenceFN
							sequencesFN.append(inSequenceFN)
							inSequenceFN=0
				else:
					# This prediction is right, we have to cancel any run of FP or FN
					if inSequenceFP!=0:
						if inSequenceFP>longestSequenceFP:
							longestSequenceFP=inSequenceFP
						sequencesFP.append(inSequenceFP)
						
					if inSequenceFN!=0:
						if inSequenceFN>longestSequenceFN:
							longestSequenceFN=inSequenceFN
						sequencesFN.append(inSequenceFN)
					inSequenceFP=0
					inSequenceFN=0
				if int(real) == int(attacker): 
					# the device has been robbed!
					if firstLineAttackerReal ==0:
						#mark the start of the rob
						firstLineAttackerReal = lineCount
					if int(predicted) == int(attacker): 
						attackerDetectedRunLength = attackerDetectedRunLength + 1
						try:
							pos = linesToConsiderRealAttack.index(attackerDetectedRunLength)
							if lineRealAttackDetected[pos] ==0:
								lineRealAttackDetected[pos] = lineCount
						except:
							#nothing to do
							attackerDetectedRunLength = attackerDetectedRunLength
					else:
						# the device is confused. It thinks that it is the real user holding it...
						attackerDetectedRunLength = 0

				lineCount = lineCount + 1
		try:
			for idx,val in 	enumerate(lineRealAttackDetected):	
				outputTimeToDetect = outputfolder + filename + '_TTD-'+ str(linesToConsiderRealAttack[idx]) + '.csv'
				if val==0: #the system is so terrible that it has not detected the attacker!
					TimeToDetect = lineCount - firstLineAttackerReal
				else:
					TimeToDetect = val - firstLineAttackerReal
				print('TTD(%d): %d, firstreal %d blocked at %d' %(linesToConsiderRealAttack[idx],TimeToDetect,firstLineAttackerReal,val)) 
				outf = open(outputTimeToDetect, 'w')
				outf.write(str(TimeToDetect)) 
				outf.close()
		except IOError as e:
			print ('I/O error %s: %s' %(str(e.errno), str(e.strerror)))