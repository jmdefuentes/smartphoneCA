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
dircsvBatteryNoMoriarty = dir + '\BatteryNoMoriarty.csv'
if not os.path.isfile(dircsvBatteryNoMoriarty):
	dircsvBatteryNoMoriarty = dir + '\Battery.csv'
dirarff = dir + '\Battery.arff'

with open(dircsvBatteryNoMoriarty) as infile:
    with open(dirarff,'wb') as outfile:
		outfile.write("@RELATION battery\n")
		outfile.write("@ATTRIBUTE UserId real\n")
		outfile.write("@ATTRIBUTE Battery_charge_type real\n")
		outfile.write("@ATTRIBUTE Battery_health real\n")
		outfile.write("@ATTRIBUTE Battery_level real\n")
		outfile.write("@ATTRIBUTE Battery_online real\n")
		outfile.write("@ATTRIBUTE Battery_plugged real\n")		
		#Battery present should be true or false but there is some error and it should be other field
		outfile.write("@ATTRIBUTE Battery_present real\n")
		outfile.write("@ATTRIBUTE Battery_scale real\n")
		outfile.write("@ATTRIBUTE Battery_status real\n")
		outfile.write("@ATTRIBUTE Battery_temperature real\n")
		outfile.write("@ATTRIBUTE Battery_voltage real\n")
		
		
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
				for x in range(3, 17):
					if (x != 4) and (x != 6) and (x != 7) and (x != 14) and (x != 16):
						if line.split(",")[x].strip()== 'NULL' or line.split(",")[x].strip()== 'null':
							nullVar=1

				if nullVar==0:
					charger=line.split(",")[8].strip()
					print charger
					chargerlevel = charger.rsplit(' ', 1)[0]
					if 'GHz' in chargerlevel:
						chargerlevel= str(int(float(chargerlevel) * 1000))
					idUser = 1
					idString= line.split(",")[0].strip()
					for ch in range(0, len(idString)):
						#The position is added to avoid the existence of equal id users
						idUser= idUser+ int(ord(idString[ch])) + ch
					outfile.write(str(idUser)+","+line.split(",")[3].strip()+","+line.split(",")[5].strip()+","+chargerlevel+","+line.split(",")[9].strip()+","+line.split(",")[10].strip()+","+line.split(",")[11].strip()+","+line.split(",")[12].strip()+","+line.split(",")[13].strip()+","+line.split(",")[15].strip()+","+line.split(",")[17].strip()+"\n")
				
			elif line.split(",")[0].strip() in listUsers:
				nullVar=0
				for x in range(3, 17):
					if (x != 4) and (x != 6) and (x != 7) and (x != 14) and (x != 16):
						if line.split(",")[x].strip()== 'NULL' or line.split(",")[x].strip()== 'null':
							nullVar=1

				if nullVar==0:
					charger=line.split(",")[8].strip()
					print charger
					chargerlevel = charger.rsplit(' ', 1)[0]
					if 'GHz' in chargerlevel:
						chargerlevel= str(int(float(chargerlevel) * 1000))
					idUser = 1
					idString= line.split(",")[0].strip()
					for ch in range(0, len(idString)):
						#The position is added to avoid the existence of equal id users
						idUser= idUser+ int(ord(idString[ch])) + ch
					
					outfile.write(str(idUser)+","+line.split(",")[3].strip()+","+line.split(",")[5].strip()+","+chargerlevel+","+line.split(",")[9].strip()+","+line.split(",")[10].strip()+","+line.split(",")[11].strip()+","+line.split(",")[12].strip()+","+line.split(",")[13].strip()+","+line.split(",")[15].strip()+","+line.split(",")[17].strip()+"\n")

				
