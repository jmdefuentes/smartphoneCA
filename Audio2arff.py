#############################
#Authors: Lorena González-Manzano and José María de Fuentes
#University Carlos III of Madrid
#February 2018
##############################
import csv
import sys
#Dir of file Audio.csv to process
dir = sys.argv[1]
dircsv = dir + '\Audio.csv'
#Output a file Audio.arff
dirarff = dir + '\Audio.arff'

with open(dircsv) as infile:
    with open(dirarff,'wb') as outfile:
		outfile.write("@RELATION audio\n")
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
				#In this case the first is the UserId but converted to a number regarding position in listUsers, second  Light_accuracy and third Light_lux
				if line.split(",")[3].strip() != 'null' and line.split(",")[4].strip()!= 'null'and line.split(",")[5].strip()!= 'null'and line.split(",")[6].strip()!= 'null'and line.split(",")[7].strip()!= 'null'and line.split(",")[8].strip()!= 'null'and line.split(",")[9].strip()!= 'null'and line.split(",")[10].strip()!= 'null'and line.split(",")[11].strip()!= 'null'and line.split(",")[12].strip()!= 'null'and line.split(",")[13].strip()!= 'null'and line.split(",")[14].strip()!= 'null'and line.split(",")[15].strip()!= 'null'and line.split(",")[16].strip()!= 'null'and line.split(",")[17].strip()!= 'null'and line.split(",")[18].strip()!= 'null'and line.split(",")[19].strip()!= 'null'and line.split(",")[20].strip()!= 'null'and line.split(",")[21].strip()!= 'null'and line.split(",")[22].strip()!= 'null':
						idUser = 1
						idString= line.split(",")[0].strip()
						for ch in range(0, len(idString)):
							#The position is added to avoid the existence of equal id users
							idUser= idUser+ int(ord(idString[ch])) + ch
						outfile.write(str(idUser)+","+line.split(",")[3].strip()+","+line.split(",")[4].strip()+","+line.split(",")[5].strip()+","+line.split(",")[6].strip()+","+line.split(",")[7].strip()+","+line.split(",")[8].strip()+","+line.split(",")[9].strip()+","+line.split(",")[10].strip()+","+line.split(",")[11].strip()+","+line.split(",")[12].strip()+","+line.split(",")[13].strip()+","+line.split(",")[14].strip()+","+line.split(",")[15].strip()+","+line.split(",")[16].strip()+","+line.split(",")[17].strip()+","+line.split(",")[18].strip()+","+line.split(",")[19].strip()+","+line.split(",")[20].strip()+","+line.split(",")[21].strip()+","+line.split(",")[22].strip()+"\n")
			elif line.split(",")[3].strip() != 'null' and line.split(",")[4].strip()!= 'null'and line.split(",")[5].strip()!= 'null'and line.split(",")[6].strip()!= 'null'and line.split(",")[7].strip()!= 'null'and line.split(",")[8].strip()!= 'null'and line.split(",")[9].strip()!= 'null'and line.split(",")[10].strip()!= 'null'and line.split(",")[11].strip()!= 'null'and line.split(",")[12].strip()!= 'null'and line.split(",")[13].strip()!= 'null'and line.split(",")[14].strip()!= 'null'and line.split(",")[15].strip()!= 'null'and line.split(",")[16].strip()!= 'null'and line.split(",")[17].strip()!= 'null'and line.split(",")[18].strip()!= 'null'and line.split(",")[19].strip()!= 'null'and line.split(",")[20].strip()!= 'null'and line.split(",")[21].strip()!= 'null'and line.split(",")[22].strip()!= 'null':
				idUser = 1
				idString= line.split(",")[0].strip()
				for ch in range(0, len(idString)):
					#The position is added to avoid the existence of equal id users
					idUser= idUser+ int(ord(idString[ch])) + ch			
				outfile.write(str(idUser)+","+line.split(",")[3].strip()+","+line.split(",")[4].strip()+","+line.split(",")[5].strip()+","+line.split(",")[6].strip()+","+line.split(",")[7].strip()+","+line.split(",")[8].strip()+","+line.split(",")[9].strip()+","+line.split(",")[10].strip()+","+line.split(",")[11].strip()+","+line.split(",")[12].strip()+","+line.split(",")[13].strip()+","+line.split(",")[14].strip()+","+line.split(",")[15].strip()+","+line.split(",")[16].strip()+","+line.split(",")[17].strip()+","+line.split(",")[18].strip()+","+line.split(",")[19].strip()+","+line.split(",")[20].strip()+","+line.split(",")[21].strip()+","+line.split(",")[22].strip()+"\n")
