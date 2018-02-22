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

dirWF= dir + '\Moriarty.csv'
dirRF=dir + '\Moriarty'
file = file(dirWF, 'wb')
#This 3 lines are required when the downloaded file does not contain headers
#moriarty filenames
fieldnames = ['Userid','UUID','extras','action','timestamp']
csv.writer(file).writerow(fieldnames)

csv.writer(file).writerows(csv.reader(open(dirRF), delimiter="\t"))

file.close()

