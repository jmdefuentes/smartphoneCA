#############################
#Authors: Lorena González-Manzano and José María de Fuentes
#University Carlos III of Madrid
#February 2018
##############################
import os
import csv
import sys

csv.field_size_limit(sys.maxsize)
#Dir to File to process 
dir = sys.argv[1]
#An arff file is generated after processing a csv
dircsvTransmittedDataNoMoriarty = dir + '\TransmittedDataNoMoriarty.csv'
if not os.path.isfile(dircsvTransmittedDataNoMoriarty):
	dircsvTransmittedDataNoMoriarty = dir + '\TransmittedData.csv'
dirarff = dir + '\TransmittedData.arff'

with open(dircsvTransmittedDataNoMoriarty) as infile:
    with open(dirarff,'wb') as outfile:
		outfile.write("@RELATION TransmittedData\n")
		outfile.write("@ATTRIBUTE UserId real\n")
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
			contLine = contLine + 1	
			#For all users...
			if line.split(",")[0].strip() not in listUsers:
				listUsers.extend([line.split(",")[0].strip()])		
				nullVar=0	
				for x in range(3, 14):
					if line.split(",")[x].strip()== 'NULL' or line.split(",")[x].strip()== 'null':
						nullVar=1

				if nullVar==0:
					charger=line.split(",")[3].strip()
					chargerlevel = charger.rsplit(' ', 1)[0]
					if 'GHz' in chargerlevel:
						chargerlevel= str(int(float(chargerlevel) * 1000))
					idUser = 1
					idString= line.split(",")[0].strip()
					for ch in range(0, len(idString)):
						#The position is added to avoid the existence of equal id users
						idUser= idUser+ int(ord(idString[ch])) + ch
					outfile.write(str(idUser)+","+chargerlevel+','+line.split(",")[4].strip()+","+line.split(",")[5].strip()+","+line.split(",")[6].strip()+","+line.split(",")[7].strip()+","+line.split(",")[8].strip()+","+line.split(",")[9].strip()+","+line.split(",")[10].strip()+","+line.split(",")[11].strip()+","+line.split(",")[12].strip()+","+line.split(",")[13].strip()+","+line.split(",")[14].strip()+"\n")
				
			elif line.split(",")[0].strip() in listUsers:
				nullVar=0
				for x in range(3, 14):
					if line.split(",")[x].strip()== 'NULL' or line.split(",")[x].strip()== 'null':
						nullVar=1					

				if nullVar==0:
					charger=line.split(",")[3].strip()
					chargerlevel = charger.rsplit(' ', 1)[0]
					if ('GHz' in chargerlevel):
						chargerlevel= str(int(float(chargerlevel) * 1000))
					idUser = 1
					idString= line.split(",")[0].strip()
					for ch in range(0, len(idString)):
						#The position is added to avoid the existence of equal id users
						idUser= idUser+ int(ord(idString[ch])) + ch
					outfile.write(str(idUser)+","+chargerlevel+','+line.split(",")[4].strip()+","+line.split(",")[5].strip()+","+line.split(",")[6].strip()+","+line.split(",")[7].strip()+","+line.split(",")[8].strip()+","+line.split(",")[9].strip()+","+line.split(",")[10].strip()+","+line.split(",")[11].strip()+","+line.split(",")[12].strip()+","+line.split(",")[13].strip()+","+line.split(",")[14].strip()+"\n")

		
				
