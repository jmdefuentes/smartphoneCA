#############################
#Authors: Lorena González-Manzano and José María de Fuentes
#University Carlos III of Madrid
#February 2018
##############################
import csv
import sys
import os
#Dir to File to process - The downloaded one from Sherlock database
#TransmittedData, Audio and Battery are processed
dir = sys.argv[1]
#Threshold used to link files AudioLight and Battery-- Distance between which values are considered of the same set, that is generated in a similar amount of time
diffCount = int(sys.argv[2])
diffCountStr = sys.argv[2]
dircsvT3 = dir + '\T3.csv'
dircsvBattery = dir + '\BatteryNoMoriarty.csv'
if not os.path.isfile(dircsvBattery):
	dircsvBattery = dir + '\Battery.csv'
dircsvALB = dir + '\AudioLightBattery'+diffCountStr + '.csv'



fileT3 = open(dircsvT3)
fileB = open(dircsvBattery)
fileALB = open(dircsvALB,"wb")
readerT3 = csv.DictReader(fileT3)
readerB = csv.DictReader(fileB)
writer = csv.writer(fileALB)


#This is the header for the file to create
fieldnames = ['Userid','UUID','version','Audio_diffSecs','Audio_l1Norm','Audio_l2Norm','Audio_linfNorm','AudPSD_AcrossFreqBands0','AudPSD_AcrossFreqBands1','AudPSD_AcrossFreqBands2','AudPSD_AcrossFreqBands3','Audio_mfccs0','Audio_mfccs1','Audio_mfccs2','Audio_mfccs3','Audio_mfccs4','Audio_mfccs5','Audio_mfccs6','Audio_mfccs7','Audio_mfccs8','Audio_mfccs9','Audio_mfccs10','Audio_mfccs11','Audio_timestemp','Light_accuracy','Light_lux','Light_timestamp','Battery_charge_type','Battery_current_avg','Battery_health','Battery_icon_small','Battery_invalid_charger','Battery_level','Battery_online','Battery_plugged','Battery_present','Battery_scale','Battery_status','Battery_technology','Battery_temperature','Battery_timestamp','Battery_voltage']
writer = csv.DictWriter(fileALB, fieldnames=fieldnames)
writer.writeheader()

#This is used to ensore that if UUIDT3 is smaller than UUID, then we process a new line of T3 but ramain in the same line of the file broadcast 
notMove=1

endT3=True
endB=True

#Note that Battery and T3 file are just processed once...then, we move little by little in them
while endT3:
	try:
		rowT3= readerT3.next()	
		endB=True
		print rowT3
		while endB:
			try:
				if notMove==1:
					row= readerB.next()
				elif notMove==0:
					notMove=1
				print row
				UUIDT3= int(float(rowT3['UUID']))	
				UUIDB= int(float(row['UUID']))
				#If the UUIDT3 and UUIDB are closed and the UserId is the same, then both rows are considered analogous
				#Otherwise Battery file is iterated because those UUIDs far from UUIDT3 will not be stored in the new output file

				if(UUIDT3>(UUIDB-diffCount) and UUIDT3<=(UUIDB+diffCount) and rowT3['Userid']==row['UserId']):
					writer.writerow({'Userid': rowT3['Userid'],'UUID': rowT3['UUID'], 'version': rowT3['version'], 'Audio_diffSecs': rowT3['Audio_diffSecs'], 'Audio_l1Norm': rowT3['Audio_l1Norm'], 'Audio_l2Norm': rowT3['Audio_l2Norm'], 'Audio_linfNorm': rowT3['Audio_linfNorm'], 'AudPSD_AcrossFreqBands0': rowT3['AudPSD_AcrossFreqBands0'], 'AudPSD_AcrossFreqBands1': rowT3['AudPSD_AcrossFreqBands1'], 'AudPSD_AcrossFreqBands2': rowT3['AudPSD_AcrossFreqBands2'], 'AudPSD_AcrossFreqBands3': rowT3['AudPSD_AcrossFreqBands3'], 'Audio_mfccs0': rowT3['Audio_mfccs0'], 'Audio_mfccs1': rowT3['Audio_mfccs1'], 'Audio_mfccs2': rowT3['Audio_mfccs2'], 'Audio_mfccs3': rowT3['Audio_mfccs3'], 'Audio_mfccs4': rowT3['Audio_mfccs4'], 'Audio_mfccs5': rowT3['Audio_mfccs5'], 'Audio_mfccs6': rowT3['Audio_mfccs6'], 'Audio_mfccs7': rowT3['Audio_mfccs7'], 'Audio_mfccs8': rowT3['Audio_mfccs8'], 'Audio_mfccs9': rowT3['Audio_mfccs9'], 'Audio_mfccs10': rowT3['Audio_mfccs10'], 'Audio_mfccs11': rowT3['Audio_mfccs11'], 'Audio_timestemp': rowT3['Audio_timestemp'], 'Light_accuracy': rowT3['Light_accuracy'], 'Light_lux': rowT3['Light_lux'], 'Light_timestamp': rowT3['Light_timestamp'],'Battery_charge_type': row['Battery_charge_type'], 'Battery_current_avg': row['Battery_current_avg'], 'Battery_health': row['Battery_health'], 'Battery_icon_small': row['Battery_icon_small'], 'Battery_invalid_charger': row['Battery_invalid_charger'], 'Battery_level': row['Battery_level'], 'Battery_online': row['Battery_online'], 'Battery_plugged': row['Battery_plugged'], 'Battery_present': row['Battery_present'], 'Battery_scale': row['Battery_scale'], 'Battery_status': row['Battery_status'], 'Battery_technology': row['Battery_technology'], 'Battery_temperature': row['Battery_temperature'], 'Battery_timestamp': row['Battery_timestamp'], 'Battery_voltage': row['Battery_voltage']})
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

dirarffALB = dir + '\AudioLightBattery'+diffCountStr + '.arff'
with open(dircsvALB) as infile:
    with open(dirarffALB,'wb') as outfile:
		outfile.write("@RELATION audiolightbattery\n")
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
		#Light starts
		outfile.write("@ATTRIBUTE Lightaccuracy real\n")
		outfile.write("@ATTRIBUTE Lightlux real\n")
		#Battery starts				
		outfile.write("@ATTRIBUTE Battery_charge_type real\n")
		outfile.write("@ATTRIBUTE Battery_health real\n")
		outfile.write("@ATTRIBUTE Battery_level real\n")
		outfile.write("@ATTRIBUTE Battery_online real\n")
		outfile.write("@ATTRIBUTE Battery_plugged real\n")		
		#Battery present should be true or false but there is some error and it should be other field
		outfile.write("@ATTRIBUTE Battery_present {true,false}\n")
		outfile.write("@ATTRIBUTE Battery_scale real\n")
		outfile.write("@ATTRIBUTE Battery_voltage real\n")
		
		outfile.write("@DATA\n")
		#This is used to not include headers
		first_line = infile.readline()
		listUsers=[]
		contLine=0
		for line in infile:
			contLine = contLine+1
			#For all users...
			if line.split(",")[0].strip() not in listUsers:
				listUsers.extend([line.split(",")[0].strip()])
				nullVar=0
				for x in range(3, 40):
					#23 and 26 corresponds to timestamp and they are not stored
					if (x != 23) and (x != 26) and (x != 28) and (x != 30) and (x != 31) and (x != 38) and (x != 39)  and (x != 40):
						if line.split(",")[x].strip() == 'null' or line.split(",")[x].strip() == 'NULL':
							nullVar=1
						
				#It means that any field is null and action belong to word
				if nullVar==0:
					#time_stamps (located in pos 23 and 26) are not stored
					#This is to remove GHz or MHz
					charger=line.split(",")[32].strip()
					print charger
					chargerlevel = charger.rsplit(' ', 1)[0]
					if 'GHz' in chargerlevel:
						chargerlevel= str(int(float(chargerlevel) * 1000))					
					#data to store
					idUser = 1
					idString= line.split(",")[0].strip()
					for ch in range(0, len(idString)):
						#The position is added to avoid the existence of equal id users
						idUser= idUser+ int(ord(idString[ch])) + ch							
					dataToStore = str(idUser)
					for x in range(3, 40):
						if x == 32:
							dataToStore +=","+ chargerlevel
						elif (x != 23) and (x != 26) and (x != 28) and (x != 30) and (x != 31) and (x != 38) and (x != 39)  and (x != 40):
							dataToStore+=","+line.split(",")[x].strip()
					dataToStore+= "\n"
					outfile.write(dataToStore)
			elif line.split(",")[0].strip() in listUsers:
				nullVar=0
				for x in range(3, 40):
					#23 and 26 corresponds to timestamp and they are not stored
					if (x != 23) and (x != 26) and (x != 28) and (x != 30) and (x != 31) and (x != 38) and (x != 39)  and (x != 40):
						if line.split(",")[x].strip() == 'null' or line.split(",")[x].strip() == 'NULL':
							nullVar=1
				#It means that any field is null and action belong to word
				if nullVar==0:
					#time_stamps (located in pos 23 and 26) are not stored
					#This is to remove GHz or MHz
					charger=line.split(",")[32].strip()
					print charger
					chargerlevel = charger.rsplit(' ', 1)[0]
					if 'GHz' in chargerlevel:
						chargerlevel= str(int(float(chargerlevel) * 1000))						
					#data to store
					idUser = 1
					idString= line.split(",")[0].strip()
					for ch in range(0, len(idString)):
						#The position is added to avoid the existence of equal id users
						idUser= idUser+ int(ord(idString[ch])) + ch							
					dataToStore = str(idUser)
					for x in range(3, 40):
						if x == 32:
							dataToStore +=","+chargerlevel
						elif (x != 23) and (x != 26) and (x != 28) and (x != 30) and (x != 31) and (x != 38) and (x != 39)  and (x != 40):
							dataToStore+=","+line.split(",")[x].strip()
					dataToStore+= "\n"
					outfile.write(dataToStore)			


