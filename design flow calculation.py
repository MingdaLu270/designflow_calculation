
# coding: utf-8



## This program downloads annual peak streamflow data from USGS surface Data Portal
## for a USBR_INPUT USGS gage station
## Stores as csv file (.csv) in assigned location in Jupyter Notebook
## Calculate the Design Flow for certain Return Periods of this station

## Import the required Modules/Packages for obtaining the data from portal
import urllib.parse
import urllib.request


## Import useful packages
import matplotlib.pyplot as plt
import pandas as pd
import os
import math
import csv
import numpy as np
os.getcwd()


## Define a function for obtaining the peak flow data from USGS Surface Data Portal
## Parameters - station number and flolder name
def GetPeakFlowData(station_number,FolderName):
    ## Building URLs
    var1={'site_no': station_number}
    part1='https://nwis.waterdata.usgs.gov/in/nwis/peak?'
    part2='&agency_cd=USGS&format=rdb'
    link=(part1+urllib.parse.urlencode(var1)+part2)
    print("The USGS Link is: \n",link)
    
    ## Opening the link & retrieving data
    response=urllib.request.urlopen(link)
    page_data=response.read()
    
    ## File name assigning & storing the raw data as .txt and .csv file
    with open(FolderName+'data_'+station_number+'_raw'+'.txt','wb')as f1:
        f1.write(page_data)
    f1.close
    with open(FolderName+'data_'+station_number+'_raw'+'.csv','wb')as f2:
        f2.write(page_data)
    f2.close





## Main Code
## USGS 03335500 can be applied for this part.
station_number=input("Enter HUC8 Number of the Required Station (USGS Station Number/site_no)\t")
print('\t')
## Assigning the location for storing the data
## First Method
FolderName="./Results/"
## Second Method
# FolderName="/home/mygeohub/lu270/HW/HW2/Results"
peakflow_list_wb=GetPeakFlowData(station_number,FolderName)




## Read useful data from .csv file, calculate the mean and standard deviation of stored dataset.
data=pd.read_csv('./Results/data_'+station_number+'_raw.csv',skiprows=74,header=None,delimiter='\t',na_filter=True,usecols=[2,4],names=['Datetime','Discharge'])
discharge_mean=np.mean(data['Discharge'])
discharge_sd=np.std(data['Discharge'])
print (f'mean= {discharge_mean} cfs')
print (f'standard deviation= {discharge_sd} cfs')




## Calculate Design Flow with return periods of 10, 25, 50, 100, and 500 years.
def EV1():
    x_bar=discharge_mean
    sx=discharge_sd
    x_10 = x_bar - math.sqrt(6) / math.pi * (0.5772 + math.log (math.log ( 10 / (10-1)))) * sx
    x_25 = x_bar - math.sqrt(6) / math.pi * (0.5772 + math.log (math.log ( 25 / (25-1)))) * sx
    x_50 = x_bar - math.sqrt(6) / math.pi * (0.5772 + math.log (math.log ( 50 / (50-1)))) * sx
    x_100 = x_bar - math.sqrt(6) / math.pi * (0.5772 + math.log (math.log ( 100 / (100-1)))) * sx
    x_500 = x_bar - math.sqrt(6) / math.pi * (0.5772 + math.log (math.log ( 500 / (500-1)))) * sx
    return pd.DataFrame(np.array([[10,x_10],[25,x_25],[50,x_50],[100,x_100],[500,x_500]]),columns=['ReturnPeriod_yrs','DesignFLow_cfs'])
df=EV1()
print ('Return Period and DesignFlow for USGS station '+station_number+':')
print (df)





## Create frequency plot.
plt.plot(df.ReturnPeriod_yrs,df.DesignFLow_cfs)
plt.xlabel('Return Period (yrs)')
plt.ylabel('Design Flow (cfs)')
plt.title('Design Flow for Different Return Period (USGS 03335500)')

