## This program downloads annual peak streamflow data from USGS Surface Data Portal 
## for a USER_INPUT USGS gage station 
## Stores as text file (.txt) in assigned location in Jupyter Notebook
## This code is written in Python 3 format
## Revision No: 05
## Last Revised : 2020-01-15

## Import the required Modules/Packages for obtaining the data from portal
import urllib.parse
import urllib.request

## Define a function for obtaining the peak flow data from USGS Surface Data Portal
## Parameters - station number and folder name
def GetPeakFlowData(station_number,FolderName):
    ## Building URLs
    var1 = {'site_no': station_number}
    part1 = 'https://nwis.waterdata.usgs.gov/nwis/peak?'
    part2 = '&agency_cd=USGS&format=rdb'
    link = (part1 + urllib.parse.urlencode(var1) + part2)
    print("The USGS Link is: \n",link)
    
    ## Opening the link & retrieving data
    response = urllib.request.urlopen(link)
    page_data = response.read()
    
    ## File name assigning & storing the raw data as text file
    with open(FolderName+'Data_' + station_number + '_raw'  + '.txt', 'wb') as f1:
        f1.write(page_data)
    #f1.close
    print("\nDownload complete for USGS Station Number: ", station_number)

## Main Code
station_number=input("Enter USGS Number of the Required Station(USGS Station Number/site_no) \t")
print('\t')
## Assigning the location for storing the data
## Absolute path
FolderName="./Results/"
peakflow_list_wb=GetPeakFlowData(station_number,FolderName)

