#Per Q of data the following scripts should be processed in the following order:

#To generate Audio, Light and AudioLight files:
1) tsv2csv2_Moriarty
2) CreateAndSeparationAudioLightFromT3
3) Light2arff
4) Audio2arff
5) AudioAndLight2arff

#To generate TransmittedData file
1) TransmittedData2cvs_beforeRemoveMoriarty_Q2
2) RemoveMoriarty_v4
3) TransmittedData2arff

#To generate Battery file
1) Battery2cvs_beforeRemoveMoriarty_Q2
2) RemoveMoriarty_v4
3) Battery2arff

#To mix-data AudioLightTransmittedDAta dna AudioLightBattery
1) AudioLightAndTransmittedData
3) AudioLightAndBattery

#To create files independently for each user (based on an ID)
1) SeparateFiles

#Once files are separated, by pairs, they can be joined. This is used to simulated robbery
1) JoinFilesFromSpecifiedUsers_reduced_AudioLightBattery
2) JoinFilesFromSpecifiedUsersAudioLight_reduced
3) JoinFilesFromSpecifiedUsers_reduced_battery