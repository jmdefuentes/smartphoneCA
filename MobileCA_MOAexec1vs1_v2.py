#############################
#Authors: Lorena González-Manzano and José María de Fuentes
#University Carlos III of Madrid
#February 2018
##############################
#THIS SCRIPT RUNS MOA AUTOMATICALLY USING ALL COMBINATIONS OF PARAMETERS
#USAGE: MobileCA_MOAexec.py <folder_with_ARFFs>
#Outputs will be placed within a folder of the input one
import os, subprocess, sys


commandKNN = 'java -cp /FOLDERNAME/moa.jar moa.DoTask "EvaluatePrequential -l (lazy.kNN '
inputdir = sys.argv[1]

for fichier in os.listdir(inputdir):
	for kvalues in [3, 10, 21]:
		for storedInstances in [1000, 5000, 10000]:
			sourceFile = inputdir + '/' + fichier

			outputPredKNN = inputdir + '/outputPred/' + fichier + '_' + str(kvalues) + '_' + str(storedInstances) + '_KNN.pred'

			commandeKNN = commandKNN + ' -k ' + str(kvalues) + ' -w ' + str(storedInstances)  + ') -s (ArffFileStream -f (' +sourceFile + ') -c 1) -i -1 -o (' + outputPredKNN + ')"'
			print(commandeKNN)
			os.system(commandeKNN)

