#############################
#Authors: Lorena González-Manzano and José María de Fuentes
#University Carlos III of Madrid
#February 2018
##############################

import csv
import os
import csv
import sys

#Dir to File to process - The downloaded one from Sherlock database
#The point is to clean the file from Moriarty data, if there is any
# TransmittedData is processed
dir = sys.argv[1]
dircsvT4 = dir + '\T4.csv'
dirOriginal = dir + '\T4'


csv.field_size_limit(sys.maxsize)

#This part can be removed in T4.csv already obtained
file = file(dircsvT4, 'wb')
#T4 battery filenames
fieldnames = ['Userid','UUID','Version','CpuHertz','CPU_0','CPU_1','CPU_2','CPU_3','Total_CPU','TotalMemory_freeSize','TotalMemory_max_size','TotalMemory_total_size','TotalMemory_used_size','Traffic_MobileRxBytes','Traffic_MobileRxPackets','Traffic_MobileTxBytes','Traffic_MobileTxPackets','Traffic_TotalRxBytes','Traffic_TotalRxPackets','Traffic_TotalTxBytes','Traffic_TotalTxPackets','Traffic_TotalWifiRxBytes','Traffic_TotalWifiRxPackets','Traffic_TotalWifiTxBytes','Traffic_TotalWifiTxPackets','Traffic_timestamp','Battery_charge_type','Battery_current_avg','Battery_health','Battery_icon_small','Battery_invalid_charger','Battery_level','Battery_online','Battery_plugged','Battery_present','Battery_scale','Battery_status','Battery_technology','Battery_temperature','Battery_timestamp','Battery_voltage','MemTotal','MemFree','Buffers','Cached','SwapCached','Active','Inactive','Active_anon','Inactive_anon','Active_file','Inactive_file','Unevictable','Mlocked','HighTotal','HighFree','LowTotal','LowFree','SwapTotal','SwapFree','Dirty','Writeback','AnonPages','Mapped','Shmem','Slab','SReclaimable','SUnreclaim','KernelStack','PageTables','CommitLimit','Committed_AS','VmallocTotal','VmallocUsed','VmallocChunk','msmgpio_cpu0','msmgpio_sum_cpu123','wcd9xxx_cpu0','wcd9xxx_sum_cpu123','pn547_cpu0','pn547_sum_cpu123','cypress_touchkey_cpu0','cypress_touchkey_sum_cpu123','synaptics_rmi4_i2c_cpu0','synaptics_rmi4_i2c_sum_cpu123','sec_headset_detect_cpu0','sec_headset_detect_sum_cpu123','flip_cover_cpu0','flip_cover_sum_cpu123','home_key_cpu0','home_key_sum_cpu123','volume_down_cpu0','volume_down_sum_cpu123','volume_up_cpu0','volume_up_sum_cpu123','companion_cpu0','companion_sum_cpu123','SLIMBUS_cpu0','SLIMBUS_sum_cpu123','function_call_interrupts_cpu0','function_call_interrupts_sum_cpu123','cpu123_intr_prs','tot_user','tot_nice','tot_system','tot_idle','tot_iowait','tot_irq','tot_softirq','ctxt','btime','processes','procs_running','procs_blocked','connectedWifi_SSID','connectedWifi_Level']
csv.writer(file).writerow(fieldnames)

csv.writer(file).writerows(csv.reader(open(dirOriginal), delimiter="\t"))

file.close()

#A file TransmittedData.csv is generated
dircsvTransmittedData = dir + '\TransmittedData.csv'
fileT4 = open(dircsvT4)
fileB = open(dircsvTransmittedData,"wb")
reader = csv.DictReader(fileT4)
writer = csv.writer(fileB)
fieldnames = ['UserId','UUID','version','Traffic_MobileRxBytes','Traffic_MobileRxPackets','Traffic_MobileTxBytes','Traffic_MobileTxPackets','Traffic_TotalRxBytes','Traffic_TotalRxPackets','Traffic_TotalTxBytes','Traffic_TotalTxPackets','Traffic_TotalWifiRxBytes','Traffic_TotalWifiRxPackets','Traffic_TotalWifiTxBytes','Traffic_TotalWifiTxPackets']
writer = csv.DictWriter(fileB, fieldnames=fieldnames)
writer.writeheader()



for row in reader:
	writer.writerow({'UserId': row['Userid'],'UUID': row['UUID'], 'version': row['Version'], 'Traffic_MobileRxBytes': row['Traffic_MobileRxBytes'], 'Traffic_MobileRxPackets': row['Traffic_MobileRxPackets'], 'Traffic_MobileTxBytes': row['Traffic_MobileTxBytes'], 'Traffic_MobileTxPackets': row['Traffic_MobileTxPackets'], 'Traffic_TotalRxBytes': row['Traffic_TotalRxBytes'], 'Traffic_TotalRxPackets': row['Traffic_TotalRxPackets'], 'Traffic_TotalTxBytes': row['Traffic_TotalTxBytes'], 'Traffic_TotalTxPackets': row['Traffic_TotalTxPackets'], 'Traffic_TotalWifiRxBytes': row['Traffic_TotalWifiRxBytes'], 'Traffic_TotalWifiRxPackets': row['Traffic_TotalWifiRxPackets'], 'Traffic_TotalWifiTxBytes': row['Traffic_TotalWifiTxBytes'], 'Traffic_TotalWifiTxPackets': row['Traffic_TotalWifiTxPackets']})	
	

				
fileT4.close()
fileB.close()

