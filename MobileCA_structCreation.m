%#############################
%#Authors: Lorena González-Manzano and José María de Fuentes
%#University Carlos III of Madrid
%#February 2018
%##############################

clear
%demo with structures
myDir = [string('/FOLDERNAME/AudioLight/2users/predAnalysis/'), string('/FOLDERNAME/AudioLight/sameUser/predAnalysis/'), string('/FOLDERNAME/AudioLightBattery/2users/predAnalysis/'),string('/FOLDERNAME/AudioLightBattery/sameUser/predAnalysis/'),string('/FOLDERNAME/Battery/2users/predAnalysis/'),string('/FOLDERNAME/Battery/sameUser/predAnalysis/')] ; %gets directory

%%%FILE NAME STRUCTURE: 622_672_500_5000_3_1000_KNN.pred_FirstErr
%example structure
% experiment(1).user=622;
% experiment(1).attacker=672;
% experiment(1).timeTrain=500;
% experiment(1).timeRob=5000;
% experiment(1).k=3;
% experiment(1).stored=1000;
% experiment(1).method='KNN';
% experiment(1).sensors='B'; <-- this comes in the folder name
% Now the file contents should be stored:
% experiment(1).firstError=2002;
% experiment(1).FPRuns=[2 5 21];
% experiment(1).FNRuns=[1 1 4 13 2];
% experiment(1).timeToDetect1 = 40;
% experiment(1).timeToDetect5 = 40;
% experiment(1).timeToDetect10 = 40;
% experiment(1).timeToDetect20 = 40;

%1a. traverse the folder
totalExpCounter =1;
alreadyProcessed = {};
for i= 1:size(myDir,2)
    startFolder = fullfile(char(myDir(i)));
    if ~exist(startFolder, 'dir')
        fprintf('ERROR - STOP %s',char(myDir(i)));
    end
    myFiles = dir(startFolder); %gets all files
    for k = 1:length(myFiles)
        baseFileName = myFiles(k).name;
        fullFileName = fullfile(char(myDir(i)), baseFileName);

%1. split file name to get the fields
        nameParts=strsplit(baseFileName, '_');
        if length(nameParts)<8
           fprintf(1, 'Skipping %s\n', fullFileName);
        else
            %check if it has already been processed
            %sensor type
            if contains (fullFileName,'AudioLightBattery')
                sensor = 3;%audiolightbattery
            elseif contains (fullFileName,'AudioLight')
                sensor = 2; %audiolight
            else
                sensor = 1; %battery
            end
            invariantPartName = strcat(sensor,'_', strjoin(nameParts(1:7),'_'));
            %taken from:https://es.mathworks.com/matlabcentral/answers/48033-find-a-string-in-a-character-array
            % taken from https://es.mathworks.com/matlabcentral/answers/2015-find-index-of-cells-containing-my-string
            if isempty(alreadyProcessed)
                lidx = [];
            else
                lidx = find(strcmp(alreadyProcessed,invariantPartName));
            end
            
            if isempty(lidx)
                currentExp = totalExpCounter;
                fprintf('Now reading %s as experiment %d \n', fullFileName,currentExp);
                %this experiment has not been processed yet
                experiment(currentExp).user= str2double(nameParts(1));
                experiment(currentExp).attacker = str2double(nameParts(2));
                if experiment(currentExp).attacker - experiment(currentExp).user ==100 %% this is a design criteria to mark these cases
                experiment(currentExp).sameUser = 1;
                else
                 experiment(currentExp).sameUser = 0;   
                end
                experiment(currentExp).timeTrain= str2double(nameParts(3));
                experiment(currentExp).timeRob= str2double(nameParts(4));
                experiment(currentExp).k= str2double(nameParts(5));
                experiment(currentExp).storedInstances= str2double(nameParts(6));
                experiment(currentExp).method=nameParts(7);
                experiment(currentExp).sensors=sensor;
                alreadyProcessed{currentExp} = invariantPartName;
                totalExpCounter = totalExpCounter +1;
            else
                %this experiment has already been processed. lidx gives us the position of the experiment in the array
                %of experiments
                %fprintf('Experiment %s found as experiment %d \n', invariantPartName,lidx);
                currentExp = lidx;
            end    
                %2. get the file "FN", "FP" and "Ferr" contents to fill up the fields
                currentVal = csvread(fullFileName);
                if strcmp(nameParts(8),'FN.csv')
                    %fprintf(1, 'Adding FN data of file %s to experiment %d \n', fullFileName,currentExp);
                    experiment(currentExp).FNRuns = currentVal;
                    
                elseif strcmp(nameParts(8),'FP.csv')
                    %fprintf(1, 'Adding FP data of file %s to experiment %d \n', fullFileName,currentExp);
                    experiment(currentExp).FPRuns = currentVal;
                elseif strcmp(nameParts(8),'FirstErr.csv')
                    %fprintf(1, 'Adding FirstError data of file %s to experiment %d \n', fullFileName,currentExp);
                    experiment(currentExp).FirstError = currentVal;
                else
                    %is a TTD file
                    if contains(nameParts(8),'-1.csv')
                        %fprintf(1, 'Adding TTD(1) data of file %s to experiment %d \n', fullFileName,currentExp);
                        experiment(currentExp).timeToDetect1 = currentVal;
                    elseif contains(nameParts(8),'-5.csv')
                        %fprintf(1, 'Adding TTD(5) data of file %s to experiment %d \n', fullFileName,currentExp);
                        experiment(currentExp).timeToDetect5 = currentVal;
                    elseif contains(nameParts(8),'-10.csv')
                        %fprintf(1, 'Adding TTD(10) data of file %s to experiment %d \n', fullFileName,currentExp);
                        experiment(currentExp).timeToDetect10 = currentVal;
                    else
                        %it is TTD20
                        fprintf(1, 'Adding TTD(20) data of file %s to experiment %d \n', fullFileName,currentExp);
                        experiment(currentExp).timeToDetect20 = currentVal;
                    end
                end
            
        end

    end

end

