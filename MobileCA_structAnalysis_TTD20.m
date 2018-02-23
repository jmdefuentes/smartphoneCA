%#############################
%#Authors: Lorena González-Manzano and José María de Fuentes
%#University Carlos III of Madrid
%#February 2018
%##############################
% TO BE RUN AFTER THE STRUCTURE CREATION

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
% experiment(1).timeToDetect = 40;

TIME_READING_BATTERY = 5;
TIME_READING_AUDIOLIGHT = 10;

%wrapper for boxplot to handle columns with different widths
col=@(x)reshape(x,numel(x),1);
boxplot2=@(C,varargin)boxplot(cell2mat(cellfun(col,col(C),'uni',0)),cell2mat(arrayfun(@(I)I*ones(numel(C{I}),1),col(1:numel(C)),'uni',0)),varargin{:});


%% TTD ANALYSIS BY SENSOR TYPE
fieldToFilterBy    = 'sensors';
fieldToProcess     = 'timeToDetect20';

%get battery
batteryValue    = 1;


listOfFilterValues    = [experiment.(fieldToFilterBy)];
vi                    = (listOfFilterValues == batteryValue);
filteredStructure     = experiment(vi);
allTTD_battery = [];
for curr=1:length(filteredStructure)
    allTTD_battery = [allTTD_battery;filteredStructure(curr).timeToDetect20];
end

%get audioLight
audioLightValue    = 2;


listOfFilterValues    = [experiment.(fieldToFilterBy)];
vi                    = (listOfFilterValues == audioLightValue);
filteredStructure     = experiment(vi);
allTTD_audioLight = [];
for curr=1:length(filteredStructure)
    allTTD_audioLight = [allTTD_audioLight;filteredStructure(curr).timeToDetect20];
end

%get audioLightBattery
audioLightBatteryValue    = 3;


listOfFilterValues    = [experiment.(fieldToFilterBy)];
vi                    = (listOfFilterValues == audioLightBatteryValue);
filteredStructure     = experiment(vi);
allTTD_audioLightBattery = [];
for curr=1:length(filteredStructure)
    allTTD_audioLightBattery = [allTTD_audioLightBattery;filteredStructure(curr).timeToDetect20];
end
figure
h2= boxplot2({allTTD_battery*TIME_READING_BATTERY, allTTD_audioLight*TIME_READING_AUDIOLIGHT, allTTD_audioLightBattery*TIME_READING_AUDIOLIGHT},'Labels',{'B','AL','ALB'})
ylabel('Time (s)','FontSize',12)
set(findobj(get(h2(1), 'parent'), 'type', 'text'), 'fontsize', 50);
ylim([0,1000])
set(gca,'YTick',0:50:1000)
print('TTD20-sensor-notitle','-dpng');
savefig('TTD20-sensor-notitle.fig');

%% TTD ANALYSIS BY TRAINING TIME
fieldToFilterBy1    = 'sensors';
fieldToFilterBy2    = 'timeTrain';
fieldToProcess     = 'timeToDetect20';

%get battery
batteryValue    = 1;
trainValue1     = 500;
trainValue2     = 5000;
trainValue3     = 10000;

%get all experiments with battery
listOfFilterValues    = [experiment.(fieldToFilterBy1)];
vi                    = (listOfFilterValues == batteryValue);
experimentsBattery     = experiment(vi);
%now get experiments with battery and each train value
listOfFilterValues    = [experimentsBattery.(fieldToFilterBy2)];
vi                    = (listOfFilterValues == trainValue1);
experimentsBatteryTrain500=experimentsBattery(vi);
vi                    = (listOfFilterValues == trainValue2);
experimentsBatteryTrain5000=experimentsBattery(vi);
vi                    = (listOfFilterValues == trainValue3);
experimentsBatteryTrain10000=experimentsBattery(vi);


allTTD_BatteryTrain500 = [];
allTTD_BatteryTrain5000 = [];
allTTD_BatteryTrain10000 = [];
for curr=1:length(experimentsBatteryTrain500)
    allTTD_BatteryTrain500 = [allTTD_BatteryTrain500;experimentsBatteryTrain500(curr).timeToDetect20];
end
for curr=1:length(experimentsBatteryTrain5000)
    allTTD_BatteryTrain5000 = [allTTD_BatteryTrain5000;experimentsBatteryTrain5000(curr).timeToDetect20];
end
for curr=1:length(experimentsBatteryTrain10000)
    allTTD_BatteryTrain10000 = [allTTD_BatteryTrain10000;experimentsBatteryTrain10000(curr).timeToDetect20];
end

%get audioLight
audioLightValue    = 2;


%get all experiments with audioLight
listOfFilterValues    = [experiment.(fieldToFilterBy1)];
vi                    = (listOfFilterValues == audioLightValue);
experimentsAudioLight     = experiment(vi);
%now get experiments with audioLight and each train value
listOfFilterValues    = [experimentsAudioLight.(fieldToFilterBy2)];
vi                    = (listOfFilterValues == trainValue1);
experimentsALTrain500=experimentsAudioLight(vi);
vi                    = (listOfFilterValues == trainValue2);
experimentsALTrain5000=experimentsAudioLight(vi);
vi                    = (listOfFilterValues == trainValue3);
experimentsALTrain10000=experimentsAudioLight(vi);


allTTD_ALTrain500 = [];
allTTD_ALTrain5000 = [];
allTTD_ALTrain10000 = [];
for curr=1:length(experimentsALTrain500)
    allTTD_ALTrain500 = [allTTD_ALTrain500;experimentsALTrain500(curr).timeToDetect20];
end
for curr=1:length(experimentsALTrain5000)
    allTTD_ALTrain5000 = [allTTD_ALTrain5000;experimentsALTrain5000(curr).timeToDetect20];
end
for curr=1:length(experimentsALTrain10000)
    allTTD_ALTrain10000 = [allTTD_ALTrain10000;experimentsALTrain10000(curr).timeToDetect20];
end

%get audioLightBattery
audioLightBatteryValue    = 3;


%get all experiments with audioLightBattery
listOfFilterValues    = [experiment.(fieldToFilterBy1)];
vi                    = (listOfFilterValues == audioLightBatteryValue);
experimentsAudioLightBattery     = experiment(vi);
%now get experiments with audioLightBattery and each train value
listOfFilterValues    = [experimentsAudioLightBattery.(fieldToFilterBy2)];
vi                    = (listOfFilterValues == trainValue1);
experimentsALBTrain500=experimentsAudioLightBattery(vi);
vi                    = (listOfFilterValues == trainValue2);
experimentsALBTrain5000=experimentsAudioLightBattery(vi);
vi                    = (listOfFilterValues == trainValue3);
experimentsALBTrain10000=experimentsAudioLightBattery(vi);


allTTD_ALBTrain500 = [];
allTTD_ALBTrain5000 = [];
allTTD_ALBTrain10000 = [];
for curr=1:length(experimentsALBTrain500)
    allTTD_ALBTrain500 = [allTTD_ALBTrain500;experimentsALBTrain500(curr).timeToDetect20];
end
for curr=1:length(experimentsALBTrain5000)
    allTTD_ALBTrain5000 = [allTTD_ALBTrain5000;experimentsALBTrain5000(curr).timeToDetect20];
end
for curr=1:length(experimentsALBTrain10000)
    allTTD_ALBTrain10000 = [allTTD_ALBTrain10000;experimentsALBTrain10000(curr).timeToDetect20];
end
%PLOT IT!
figure


h2= boxplot2({allTTD_BatteryTrain500*TIME_READING_BATTERY,allTTD_BatteryTrain5000*TIME_READING_BATTERY,allTTD_BatteryTrain10000*TIME_READING_BATTERY, allTTD_ALTrain500*TIME_READING_AUDIOLIGHT, allTTD_ALTrain5000*TIME_READING_AUDIOLIGHT,allTTD_ALTrain10000*TIME_READING_AUDIOLIGHT,allTTD_ALBTrain500*TIME_READING_AUDIOLIGHT, allTTD_ALBTrain5000*TIME_READING_AUDIOLIGHT,allTTD_ALBTrain10000*TIME_READING_AUDIOLIGHT},'Labels',{'B 500','B 5k','B 10k','AL 500','AL 5k','AL 10k','ALB 500','ALB 5k','ALB 10k'})

%title('Analysis on time to detect (20) considering training time','FontSize',24)
ylabel('Time (s)','FontSize',12)
set(findobj(get(h2(1), 'parent'), 'type', 'text'), 'fontsize', 50);
ylim([0,1000])
set(gca,'YTick',0:50:1000)
print('TTD20-training-notitle','-dpng');
savefig('TTD20-training-notitle.fig');
%% TTD ANALYSIS BY VALUE OF K

fieldToFilterBy1    = 'sensors';
fieldToFilterBy2    = 'k';
fieldToProcess     = 'timeToDetect20';

%get battery
batteryValue    = 1;
kValue1     = 3;
kValue2     = 10;
kValue3     = 21;

%get all experiments with battery
listOfFilterValues    = [experiment.(fieldToFilterBy1)];
vi                    = (listOfFilterValues == batteryValue);
experimentsBattery     = experiment(vi);
%now get experiments with battery and each k value
listOfFilterValues    = [experimentsBattery.(fieldToFilterBy2)];
vi                    = (listOfFilterValues == kValue1);
experimentsBatteryk3=experimentsBattery(vi);
vi                    = (listOfFilterValues == kValue2);
experimentsBatteryk10=experimentsBattery(vi);
vi                    = (listOfFilterValues == kValue3);
experimentsBatteryk21=experimentsBattery(vi);


allTTD_Batteryk3 = [];
allTTD_Batteryk10 = [];
allTTD_Batteryk21 = [];
for curr=1:length(experimentsBatteryk3)
    allTTD_Batteryk3 = [allTTD_Batteryk3;experimentsBatteryk3(curr).timeToDetect20];
end
for curr=1:length(experimentsBatteryk10)
    allTTD_Batteryk10 = [allTTD_Batteryk10;experimentsBatteryk10(curr).timeToDetect20];
end
for curr=1:length(experimentsBatteryk21)
    allTTD_Batteryk21 = [allTTD_Batteryk21;experimentsBatteryk21(curr).timeToDetect20];
end

%get audioLight
audioLightValue    = 2;


%get all experiments with audioLight
listOfFilterValues    = [experiment.(fieldToFilterBy1)];
vi                    = (listOfFilterValues == audioLightValue);
experimentsAudioLight     = experiment(vi);
%now get experiments with audioLight and each k value
listOfFilterValues    = [experimentsAudioLight.(fieldToFilterBy2)];
vi                    = (listOfFilterValues == kValue1);
experimentsALk3=experimentsAudioLight(vi);
vi                    = (listOfFilterValues == kValue2);
experimentsALk10=experimentsAudioLight(vi);
vi                    = (listOfFilterValues == kValue3);
experimentsALk21=experimentsAudioLight(vi);


allTTD_ALk3 = [];
allTTD_ALk10 = [];
allTTD_ALk21 = [];
for curr=1:length(experimentsALk3)
    allTTD_ALk3 = [allTTD_ALk3;experimentsALk3(curr).timeToDetect20];
end
for curr=1:length(experimentsALk10)
    allTTD_ALk10 = [allTTD_ALk10;experimentsALk10(curr).timeToDetect20];
end
for curr=1:length(experimentsALk21)
    allTTD_ALk21 = [allTTD_ALk21;experimentsALk21(curr).timeToDetect20];
end

%get audioLightBattery
audioLightBatteryValue    = 3;


%get all experiments with audioLightBattery
listOfFilterValues    = [experiment.(fieldToFilterBy1)];
vi                    = (listOfFilterValues == audioLightBatteryValue);
experimentsAudioLightBattery     = experiment(vi);
%now get experiments with audioLightBattery and each k value
listOfFilterValues    = [experimentsAudioLightBattery.(fieldToFilterBy2)];
vi                    = (listOfFilterValues == kValue1);
experimentsALBk3=experimentsAudioLightBattery(vi);
vi                    = (listOfFilterValues == kValue2);
experimentsALBk10=experimentsAudioLightBattery(vi);
vi                    = (listOfFilterValues == kValue3);
experimentsALBk21=experimentsAudioLightBattery(vi);


allTTD_ALBk3 = [];
allTTD_ALBk10 = [];
allTTD_ALBk21 = [];
for curr=1:length(experimentsALBk3)
    allTTD_ALBk3 = [allTTD_ALBk3;experimentsALBk3(curr).timeToDetect20];
end
for curr=1:length(experimentsALBk10)
    allTTD_ALBk10 = [allTTD_ALBk10;experimentsALBk10(curr).timeToDetect20];
end
for curr=1:length(experimentsALBk21)
    allTTD_ALBk21 = [allTTD_ALBk21;experimentsALBk21(curr).timeToDetect20];
end
%PLOT IT!
figure
h2= boxplot2({allTTD_Batteryk3*TIME_READING_BATTERY,allTTD_Batteryk10*TIME_READING_BATTERY,allTTD_Batteryk21*TIME_READING_BATTERY, allTTD_ALk3*TIME_READING_AUDIOLIGHT, allTTD_ALk10*TIME_READING_AUDIOLIGHT,allTTD_ALk21*TIME_READING_AUDIOLIGHT,allTTD_ALBk3*TIME_READING_AUDIOLIGHT, allTTD_ALBk10*TIME_READING_AUDIOLIGHT,allTTD_ALBk21*TIME_READING_AUDIOLIGHT},'Labels',{'B k=3','B k=10','B k=21','AL k=3','AL k=10','AL k=21','ALB k=3','ALB k=10','ALB k=21'})

%title('Analysis on time to detect (20) considering value of K','FontSize',24)
ylabel('Time (s)','FontSize',12)
set(findobj(get(h2(1), 'parent'), 'type', 'text'), 'fontsize', 50);
ylim([0,1000])
set(gca,'YTick',0:50:1000)
print('TTD20-k-notitle','-dpng');
savefig('TTD20-k-notitle.fig');

%% TTD ANALYSIS BY STORED INSTANCES

fieldToFilterBy1    = 'sensors';
fieldToFilterBy2    = 'storedInstances';
fieldToProcess     = 'timeToDetect20';

%get battery
batteryValue    = 1;
storedValue1     = 1000;
storedValue2     = 5000;
storedValue3     = 10000;

%get all experiments with battery
listOfFilterValues    = [experiment.(fieldToFilterBy1)];
vi                    = (listOfFilterValues == batteryValue);
experimentsBattery     = experiment(vi);
%now get experiments with battery and each stored value
listOfFilterValues    = [experimentsBattery.(fieldToFilterBy2)];
vi                    = (listOfFilterValues == storedValue1);
experimentsBatterystored1000=experimentsBattery(vi);
vi                    = (listOfFilterValues == storedValue2);
experimentsBatterystored5000=experimentsBattery(vi);
vi                    = (listOfFilterValues == storedValue3);
experimentsBatterystored10000=experimentsBattery(vi);


allTTD_Batterystored1000 = [];
allTTD_Batterystored5000 = [];
allTTD_Batterystored10000 = [];
for curr=1:length(experimentsBatterystored1000)
    allTTD_Batterystored1000 = [allTTD_Batterystored1000;experimentsBatterystored1000(curr).timeToDetect20];
end
for curr=1:length(experimentsBatterystored5000)
    allTTD_Batterystored5000 = [allTTD_Batterystored5000;experimentsBatterystored5000(curr).timeToDetect20];
end
for curr=1:length(experimentsBatterystored10000)
    allTTD_Batterystored10000 = [allTTD_Batterystored10000;experimentsBatterystored10000(curr).timeToDetect20];
end

%get audioLight
audioLightValue    = 2;


%get all experiments with audioLight
listOfFilterValues    = [experiment.(fieldToFilterBy1)];
vi                    = (listOfFilterValues == audioLightValue);
experimentsAudioLight     = experiment(vi);
%now get experiments with audioLight and each stored value
listOfFilterValues    = [experimentsAudioLight.(fieldToFilterBy2)];
vi                    = (listOfFilterValues == storedValue1);
experimentsALstored1000=experimentsAudioLight(vi);
vi                    = (listOfFilterValues == storedValue2);
experimentsALstored5000=experimentsAudioLight(vi);
vi                    = (listOfFilterValues == storedValue3);
experimentsALstored10000=experimentsAudioLight(vi);


allTTD_ALstored1000 = [];
allTTD_ALstored5000 = [];
allTTD_ALstored10000 = [];
for curr=1:length(experimentsALstored1000)
    allTTD_ALstored1000 = [allTTD_ALstored1000;experimentsALstored1000(curr).timeToDetect20];
end
for curr=1:length(experimentsALstored5000)
    allTTD_ALstored5000 = [allTTD_ALstored5000;experimentsALstored5000(curr).timeToDetect20];
end
for curr=1:length(experimentsALstored10000)
    allTTD_ALstored10000 = [allTTD_ALstored10000;experimentsALstored10000(curr).timeToDetect20];
end

%get audioLightBattery
audioLightBatteryValue    = 3;


%get all experiments with audioLightBattery
listOfFilterValues    = [experiment.(fieldToFilterBy1)];
vi                    = (listOfFilterValues == audioLightBatteryValue);
experimentsAudioLightBattery     = experiment(vi);
%now get experiments with audioLightBattery and each stored value
listOfFilterValues    = [experimentsAudioLightBattery.(fieldToFilterBy2)];
vi                    = (listOfFilterValues == storedValue1);
experimentsALBstored1000=experimentsAudioLightBattery(vi);
vi                    = (listOfFilterValues == storedValue2);
experimentsALBstored5000=experimentsAudioLightBattery(vi);
vi                    = (listOfFilterValues == storedValue3);
experimentsALBstored10000=experimentsAudioLightBattery(vi);


allTTD_ALBstored1000 = [];
allTTD_ALBstored5000 = [];
allTTD_ALBstored10000 = [];
for curr=1:length(experimentsALBstored1000)
    allTTD_ALBstored1000 = [allTTD_ALBstored1000;experimentsALBstored1000(curr).timeToDetect20];
end
for curr=1:length(experimentsALBstored5000)
    allTTD_ALBstored5000 = [allTTD_ALBstored5000;experimentsALBstored5000(curr).timeToDetect20];
end
for curr=1:length(experimentsALBstored10000)
    allTTD_ALBstored10000 = [allTTD_ALBstored10000;experimentsALBstored10000(curr).timeToDetect20];
end
%PLOT IT!
figure
h2= boxplot2({allTTD_Batterystored1000*TIME_READING_BATTERY,allTTD_Batterystored5000*TIME_READING_BATTERY,allTTD_Batterystored10000*TIME_READING_BATTERY, allTTD_ALstored1000*TIME_READING_AUDIOLIGHT, allTTD_ALstored5000*TIME_READING_AUDIOLIGHT,allTTD_ALstored10000*TIME_READING_AUDIOLIGHT,allTTD_ALBstored1000*TIME_READING_AUDIOLIGHT, allTTD_ALBstored5000*TIME_READING_AUDIOLIGHT,allTTD_ALBstored10000*TIME_READING_AUDIOLIGHT},'Labels',{'B 1k','B 5k','B 10k','AL 1k','AL 5k','AL 10k','ALB 1k','ALB 5k','ALB 10k'})

%set(findobj(gca,'Type','text'),'FontSize',24)
%set(findobj(gca,'Type','text'),'VerticalAlignment','top')
%title('Analysis on time to detect (20) considering amount of stored instances','FontSize',24)
ylabel('Time (s)','FontSize',12)
set(findobj(get(h2(1), 'parent'), 'type', 'text'), 'fontsize', 50);
ylim([0,1000])
set(gca,'YTick',0:50:1000)
print('TTD20-stored-notitle','-dpng');
savefig('TTD20-stored-notitle.fig');



%% TTD ANALYSIS BY SAME/DIFFERENT USER


fieldToFilterBy1    = 'sensors';
fieldToFilterBy2    = 'sameUser';
fieldToProcess     = 'timeToDetect20';

%get battery
batteryValue    = 1;
sameUserValue1     = 1;
sameUserValue2     = 0;


%get all experiments with battery
listOfFilterValues    = [experiment.(fieldToFilterBy1)];
vi                    = (listOfFilterValues == batteryValue);
experimentsBattery     = experiment(vi);
%now get experiments with battery and each stored value
listOfFilterValues    = [experimentsBattery.(fieldToFilterBy2)];
vi                    = (listOfFilterValues == sameUserValue1);
experimentsBatterySameUser=experimentsBattery(vi);
vi                    = (listOfFilterValues == sameUserValue2);
experimentsBatterydifUsers=experimentsBattery(vi);



allTTD_BatterysameUser = [];
allTTD_BatterydifUsers = [];

for curr=1:length(experimentsBatterySameUser)
    allTTD_BatterysameUser = [allTTD_BatterysameUser;experimentsBatterySameUser(curr).timeToDetect20];
end
for curr=1:length(experimentsBatterydifUsers)
    allTTD_BatterydifUsers = [allTTD_BatterydifUsers;experimentsBatterydifUsers(curr).timeToDetect20];
end


%get audioLight
audioLightValue    = 2;


%get all experiments with audioLight
listOfFilterValues    = [experiment.(fieldToFilterBy1)];
vi                    = (listOfFilterValues == audioLightValue);
experimentsAudioLight     = experiment(vi);
%now get experiments with audioLight and each stored value
listOfFilterValues    = [experimentsAudioLight.(fieldToFilterBy2)];
vi                    = (listOfFilterValues == sameUserValue1);
experimentsALSameUser=experimentsAudioLight(vi);
vi                    = (listOfFilterValues == sameUserValue2);
experimentsALdifUsers=experimentsAudioLight(vi);



allTTD_ALsameUser = [];
allTTD_ALdifUsers = [];

for curr=1:length(experimentsALSameUser)
    allTTD_ALsameUser = [allTTD_ALsameUser;experimentsALSameUser(curr).timeToDetect20];
end
for curr=1:length(experimentsALdifUsers)
    allTTD_ALdifUsers = [allTTD_ALdifUsers;experimentsALdifUsers(curr).timeToDetect20];
end


%get audioLightBattery
audioLightBatteryValue    = 3;


%get all experiments with audioLightBattery
listOfFilterValues    = [experiment.(fieldToFilterBy1)];
vi                    = (listOfFilterValues == audioLightBatteryValue);
experimentsAudioLightBattery     = experiment(vi);
%now get experiments with audioLightBattery and each stored value
listOfFilterValues    = [experimentsAudioLightBattery.(fieldToFilterBy2)];
vi                    = (listOfFilterValues == sameUserValue1);
experimentsALBSameUser=experimentsAudioLightBattery(vi);
vi                    = (listOfFilterValues == sameUserValue2);
experimentsALBdifUsers=experimentsAudioLightBattery(vi);



allTTD_ALBsameUser = [];
allTTD_ALBdifUsers = [];

for curr=1:length(experimentsALBSameUser)
    allTTD_ALBsameUser = [allTTD_ALBsameUser;experimentsALBSameUser(curr).timeToDetect20];
end
for curr=1:length(experimentsALBdifUsers)
    allTTD_ALBdifUsers = [allTTD_ALBdifUsers;experimentsALBdifUsers(curr).timeToDetect20];
end

%PLOT IT!
figure
h2= boxplot2({allTTD_BatterysameUser*TIME_READING_BATTERY,allTTD_BatterydifUsers*TIME_READING_BATTERY, allTTD_ALsameUser*TIME_READING_AUDIOLIGHT, allTTD_ALdifUsers*TIME_READING_AUDIOLIGHT, allTTD_ALBsameUser*TIME_READING_AUDIOLIGHT, allTTD_ALBdifUsers*TIME_READING_AUDIOLIGHT},'Labels',{'B u-vs-u','B u-vs-A','AL u-vs-u','AL u-vs-A','ALB u-vs-u','ALB u-vs-A'})


%title('Analysis on time to detect (20) considering same or different user','FontSize',24)
ylabel('Time (s)','FontSize',12)
set(findobj(get(h2(1), 'parent'), 'type', 'text'), 'fontsize', 50);
ylim([0,1000])
set(gca,'YTick',0:50:1000)
print('TTD20-sameOrDifUser-notitle','-dpng');
savefig('TTD20-sameOrDifUser-notitle.fig');
