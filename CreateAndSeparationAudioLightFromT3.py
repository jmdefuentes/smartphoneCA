#############################
#Authors: Lorena González-Manzano and José María de Fuentes
#University Carlos III of Madrid
#February 2018
##############################
import os
import csv
import sys

csv.field_size_limit(sys.maxsize)

#File to process - The downloaded one from Sherlock database
dir = sys.argv[1]
dirT3csv = dir + '\T3.csv'
dirT3 = dir + '\T3'
file = file(dirT3csv, 'wb')
#This 3 lines are required when the downloaded file does not contain headers

#T3 filenames
fieldnames = ['Userid','UUID','version','Audio_diffSecs','Audio_l1Norm','Audio_l2Norm','Audio_linfNorm','AudPSD_AcrossFreqBands0','AudPSD_AcrossFreqBands1','AudPSD_AcrossFreqBands2','AudPSD_AcrossFreqBands3','Audio_mfccs0','Audio_mfccs1','Audio_mfccs2','Audio_mfccs3','Audio_mfccs4','Audio_mfccs5','Audio_mfccs6','Audio_mfccs7','Audio_mfccs8','Audio_mfccs9','Audio_mfccs10','Audio_mfccs11','Audio_timestemp','Light_accuracy','Light_lux','Light_timestamp']
csv.writer(file).writerow(fieldnames)

csv.writer(file).writerows(csv.reader(open(dirT3), delimiter="\t"))

file.close()


import csv
fileT3 = open(dirT3csv)
dirAudiocsv = dir + '\Audio.csv'
dirLightcsv = dir + '\Light.csv'
fileA = open(dirAudiocsv,"wb")
fileL = open(dirLightcsv,"wb")
reader = csv.DictReader(fileT3)
writerA = csv.writer(fileA)
writerL = csv.writer(fileL)
fieldnamesA = ['Userid','UUID','version','Audio_diffSecs','Audio_l1Norm','Audio_l2Norm','Audio_linfNorm','AudPSD_AcrossFreqBands0','AudPSD_AcrossFreqBands1','AudPSD_AcrossFreqBands2','AudPSD_AcrossFreqBands3','Audio_mfccs0','Audio_mfccs1','Audio_mfccs2','Audio_mfccs3','Audio_mfccs4','Audio_mfccs5','Audio_mfccs6','Audio_mfccs7','Audio_mfccs8','Audio_mfccs9','Audio_mfccs10','Audio_mfccs11','Audio_timestemp']
writerA = csv.DictWriter(fileA, fieldnames=fieldnamesA)
writerA.writeheader()
fieldnamesL = ['Userid','UUID','version','Light_accuracy','Light_lux','Light_timestamp']
writerL = csv.DictWriter(fileL, fieldnames=fieldnamesL)
writerL.writeheader()
for row in reader:
	writerL.writerow({'Userid': row['Userid'],'UUID': row['UUID'], 'version': row['version'], 'Light_accuracy': row['Light_accuracy'], 'Light_lux': row['Light_lux'], 'Light_timestamp': row['Light_timestamp']})
	writerA.writerow({'Userid': row['Userid'],'UUID': row['UUID'],'UUID': row['UUID'], 'version': row['version'], 'Audio_diffSecs': row['Audio_diffSecs'], 'Audio_l1Norm': row['Audio_l1Norm'], 'Audio_l2Norm': row['Audio_l2Norm'],'Audio_linfNorm': row['Audio_linfNorm'],'AudPSD_AcrossFreqBands0': row['AudPSD_AcrossFreqBands0'],'AudPSD_AcrossFreqBands1': row['AudPSD_AcrossFreqBands1'],'AudPSD_AcrossFreqBands2': row['AudPSD_AcrossFreqBands2'],'AudPSD_AcrossFreqBands3': row['AudPSD_AcrossFreqBands3'],'Audio_mfccs0': row['Audio_mfccs0'],'Audio_mfccs1': row['Audio_mfccs1'],'Audio_mfccs2': row['Audio_mfccs2'],'Audio_mfccs3': row['Audio_mfccs3'],'Audio_mfccs4': row['Audio_mfccs4'],'Audio_mfccs5': row['Audio_mfccs5'],'Audio_mfccs6': row['Audio_mfccs6'],'Audio_mfccs7': row['Audio_mfccs7'],'Audio_mfccs8': row['Audio_mfccs8'],'Audio_mfccs9': row['Audio_mfccs9'],'Audio_mfccs10': row['Audio_mfccs10'],'Audio_mfccs11': row['Audio_mfccs11'],'Audio_timestemp': row['Audio_timestemp']})
				
fileT3.close()
fileA.close()				
fileL.close()				

