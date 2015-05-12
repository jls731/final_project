'''
Filename: LoadEconData.py
Created by: Joseph Song
Created on: May 11, 2015
Description: This loads the csv data for GDP and FOMC dates and fed funds rates
'''

from LoadRawData import *

def LoadEconData():
    '''Loads the FOMC and GDP data'''
    
    try:
        GDPdata = loadcsvdata('GDP.csv', ['Date'])
        FOMCdata = loadcsvdata('FOMC.csv', ['Date'])
        GDPdata.set_index('Date', inplace = True)
        FOMCdata.set_index('Date', inplace = True)

        return GDPdata, FOMCdata
    except IOError:
        print 'Either GDP or FOMC data is missing or misspelled'
        raise