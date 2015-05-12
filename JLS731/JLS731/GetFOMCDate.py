'''
Filename: GetFOMCDate.py
Created by: Joseph Song
Last version on: 5/11/2015
Description: Takes the string input of one FOMC meeting date and retrieves the previous
FOMC meeting date.
'''
from datetime import datetime

def GetFOMCDate(FOMCdate, dataset):    
    '''This is to get the previous FOMC date so we can plot the financial charts'''
    getdate = lambda s: datetime.strptime(s, "%Y/%m/%d")
    basedate = getdate(FOMCdate)
    
    rowreleasedateFOMC = dataset.index.searchsorted(basedate)
    FOMCdataset = dataset.reset_index()
    prevdate = FOMCdataset['Date'][rowreleasedateFOMC-1]
    prevdate = str(prevdate.date())
    prevdate = prevdate.replace('-','/')
    return FOMCdate, prevdate

