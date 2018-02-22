#############################
#Authors: Lorena González-Manzano and José María de Fuentes
#University Carlos III of Madrid
#February 2018
##############################
import csv
import sys
import os

dir = sys.argv[1]
#Dir to File to process - The downloaded one from Sherlock database
#TransmittedData, Audio and Light are processed
dircsvT3 = dir + '\T3.csv'
dircsvTransmittedData = dir + '\TransmittedDataNoMoriarty.csv'
if not os.path.isfile(dircsvTransmittedData):
	dircsvTransmittedData = dir + '\TransmittedData.csv'
diffCountSrt = sys.argv[2]
diffCount= int(sys.argv[2])
dircsvALT = dir + '\AudioLightTransmittedData'+diffCountSrt + '.csv'

fileT3 = open(dircsvT3)
fileB = open(dircsvTransmittedData)
fileALB = open(dircsvALT,"wb")
readerT3 = csv.DictReader(fileT3)
readerB = csv.DictReader(fileB)
writer = csv.writer(fileALB)
#This is the header for the file to create
fieldnames = ['Userid','UUID','version','Audio_diffSecs','Audio_l1Norm','Audio_l2Norm','Audio_linfNorm','AudPSD_AcrossFreqBands0','AudPSD_AcrossFreqBands1','AudPSD_AcrossFreqBands2','AudPSD_AcrossFreqBands3','Audio_mfccs0','Audio_mfccs1','Audio_mfccs2','Audio_mfccs3','Audio_mfccs4','Audio_mfccs5','Audio_mfccs6','Audio_mfccs7','Audio_mfccs8','Audio_mfccs9','Audio_mfccs10','Audio_mfccs11','Audio_timestemp','Light_accuracy','Light_lux','Light_timestamp','Traffic_MobileRxBytes','Traffic_MobileRxPackets','Traffic_MobileTxBytes','Traffic_MobileTxPackets','Traffic_TotalRxBytes','Traffic_TotalRxPackets','Traffic_TotalTxBytes','Traffic_TotalTxPackets','Traffic_TotalWifiRxBytes','Traffic_TotalWifiRxPackets','Traffic_TotalWifiTxBytes','Traffic_TotalWifiTxPackets']
writer = csv.DictWriter(fileALB, fieldnames=fieldnames)
writer.writeheader()



endT3=True
endB=True

#This is used to ensore that if UUIDT3 is smaller than UUID, then we process a new line of T3 but ramain in the same line of the file TransmittedData 
notMove=1


#Note that TransmittedData and T3 file are just processed once...then, we move little by little in them
while endT3:
	try:
		rowT3= readerT3.next()	

		endB=True
		while endB:
			try:
				if notMove==1:
					row= readerB.next()
				elif notMove==0:
					notMove=1

				UUIDT3= int(float(rowT3['UUID']))	
				UUIDB= int(float(row['UUID']))
				#If the UUIDT3 and UUIDB are closed and the UserId is the same, then both rows are considered analogous
				#Otherwise TransmittedData file is iterated because those UUIDs far from UUIDT3 will not be stored in the new output file
				if(UUIDT3>(UUIDB-diffCount) and UUIDT3<=(UUIDB+diffCount)) and (rowT3['Userid']==row['UserId']):
					writer.writerow({'Userid': rowT3['Userid'],'UUID': rowT3['UUID'], 'version': rowT3['version'], 'Audio_diffSecs': rowT3['Audio_diffSecs'], 'Audio_l1Norm': rowT3['Audio_l1Norm'], 'Audio_l2Norm': rowT3['Audio_l2Norm'], 'Audio_linfNorm': rowT3['Audio_linfNorm'], 'AudPSD_AcrossFreqBands0': rowT3['AudPSD_AcrossFreqBands0'], 'AudPSD_AcrossFreqBands1': rowT3['AudPSD_AcrossFreqBands1'], 'AudPSD_AcrossFreqBands2': rowT3['AudPSD_AcrossFreqBands2'], 'AudPSD_AcrossFreqBands3': rowT3['AudPSD_AcrossFreqBands3'], 'Audio_mfccs0': rowT3['Audio_mfccs0'], 'Audio_mfccs1': rowT3['Audio_mfccs1'], 'Audio_mfccs2': rowT3['Audio_mfccs2'], 'Audio_mfccs3': rowT3['Audio_mfccs3'], 'Audio_mfccs4': rowT3['Audio_mfccs4'], 'Audio_mfccs5': rowT3['Audio_mfccs5'], 'Audio_mfccs6': rowT3['Audio_mfccs6'], 'Audio_mfccs7': rowT3['Audio_mfccs7'], 'Audio_mfccs8': rowT3['Audio_mfccs8'], 'Audio_mfccs9': rowT3['Audio_mfccs9'], 'Audio_mfccs10': rowT3['Audio_mfccs10'], 'Audio_mfccs11': rowT3['Audio_mfccs11'], 'Audio_timestemp': rowT3['Audio_timestemp'], 'Light_accuracy': rowT3['Light_accuracy'], 'Light_lux': rowT3['Light_lux'], 'Light_timestamp': rowT3['Light_timestamp'], 'Traffic_MobileRxBytes': row['Traffic_MobileRxBytes'], 'Traffic_MobileRxPackets': row['Traffic_MobileRxPackets'], 'Traffic_MobileTxBytes': row['Traffic_MobileTxBytes'], 'Traffic_MobileTxPackets': row['Traffic_MobileTxPackets'], 'Traffic_TotalRxBytes': row['Traffic_TotalRxBytes'], 'Traffic_TotalRxPackets': row['Traffic_TotalRxPackets'], 'Traffic_TotalTxBytes': row['Traffic_TotalTxBytes'], 'Traffic_TotalTxPackets': row['Traffic_TotalTxPackets'], 'Traffic_TotalWifiRxBytes': row['Traffic_TotalWifiRxBytes'], 'Traffic_TotalWifiRxPackets': row['Traffic_TotalWifiRxPackets'], 'Traffic_TotalWifiTxBytes': row['Traffic_TotalWifiTxBytes'], 'Traffic_TotalWifiTxPackets': row['Traffic_TotalWifiTxPackets']})
					endB=False
				#If UUIDT3 is very much smaller than UUIDB, we need to get the next UUIDT3 to be close to UUIDB
				elif  UUIDT3 < UUIDB-diffCount:
					endB=False
					notMove=0
			except StopIteration:
				endB=False
	except StopIteration:
		endT3=False
fileT3.close()
fileB.close()
fileALB.close()				

dirarffALT = dir + '\AudioLightTransmittedData'+diffCountSrt + '.arff'
with open(dircsvALT) as infile:
    with open(dirarffALT,'wb') as outfile:
		outfile.write("@RELATION TransmittedData\n")
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
		#Light_timestamp no se incluye
		outfile.write("@ATTRIBUTE Traffic_MobileRxBytes real\n")
		outfile.write("@ATTRIBUTE Traffic_MobileRxPackets real\n")
		outfile.write("@ATTRIBUTE Traffic_MobileTxBytes real\n")
		outfile.write("@ATTRIBUTE Traffic_MobileTxPackets real\n")
		outfile.write("@ATTRIBUTE Traffic_TotalRxBytes real\n")
		outfile.write("@ATTRIBUTE Traffic_TotalRxPackets real\n")
		outfile.write("@ATTRIBUTE Traffic_TotalTxBytes real\n")		
		outfile.write("@ATTRIBUTE Traffic_TotalTxPackets real\n")
		outfile.write("@ATTRIBUTE Traffic_TotalWifiRxBytes real\n")
		outfile.write("@ATTRIBUTE Traffic_TotalWifiRxPackets real\n")
		outfile.write("@ATTRIBUTE Traffic_TotalWifiTxBytes real\n")
		outfile.write("@ATTRIBUTE Traffic_TotalWifiTxPackets real\n")		
		
		
		outfile.write("@DATA\n")
		#This is used to not include headers
		first_line = infile.readline()
		listUsers=[]
		contLine=0
		for line in infile:
			contLine = contLine +1
			#For all users...
			if line.split(",")[0].strip() not in listUsers:
				listUsers.extend([line.split(",")[0].strip()])
				nullVar=0
				for x in range(3, 38):
					#23 and 26 corresponds to timestamp and they are not stored
					if (x != 23) and (x != 26):
						if line.split(",")[x].strip() == 'null':
							nullVar=1
						
				#It means that any field is null
				if nullVar==0:
					#time_stamps (located in pos 23 and 26) are not stored
					charger=line.split(",")[27].strip()
					print charger
					chargerlevel = charger.rsplit(' ', 1)[0]
					#chargerlevelPrefix = charger.rsplit(' ', 1)[1]
					if 'GHz' in chargerlevel:
						chargerlevel= str(int(float(chargerlevel) * 1000))					
					#data to store
					idUser = 1
					idString= line.split(",")[0].strip()
					for ch in range(0, len(idString)):
						#The position is added to avoid the existence of equal id users
						idUser= idUser+ int(ord(idString[ch])) + ch
					dataToStore = str(idUser)
					for x in range(3, 38):
						if (x != 23) and (x != 26):
							if x==27:
								dataToStore+=","+chargerlevel
							else:
								dataToStore+=","+line.split(",")[x].strip()
					dataToStore+= "\n"
					outfile.write(dataToStore)
			elif line.split(",")[0].strip() in listUsers:
				nullVar=0
				for x in range(3, 38):
					#23 and 26 corresponds to timestamp and they are not stored
					charger=line.split(",")[27].strip()
					print charger
					chargerlevel = charger.rsplit(' ', 1)[0]
					#chargerlevelPrefix = charger.rsplit(' ', 1)[1]
					if 'GHz' in chargerlevel:
						chargerlevel= str(int(float(chargerlevel) * 1000))					
					if (x != 23) and (x != 26):
						if line.split(",")[x].strip() == 'null':
							nullVar=1
				#It means that any field is null
				if nullVar==0:
					#time_stamps (located in pos 23 and 26) are not stored
					#data to store
					idUser = 1
					idString= line.split(",")[0].strip()
					for ch in range(0, len(idString)):
						#The position is added to avoid the existence of equal id users
						idUser= idUser+ int(ord(idString[ch])) + ch					
					dataToStore = str(idUser)
					for x in range(3, 38):
						if (x != 23) and (x != 26):
							if x==27:
								dataToStore+=","+chargerlevel
							else:
								dataToStore+=","+line.split(",")[x].strip()
					dataToStore+= "\n"
					outfile.write(dataToStore)
