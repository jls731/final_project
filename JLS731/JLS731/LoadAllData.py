'''
Filename: LoadAllData.py
Created by: Joseph Song
Created on: May 11, 2015
Description: This uses the CalcEconStats, CalcForecastStats, LoadEconData, LoadFinancial
and LoadEconStatDates to load all the necessary data for use in the analysis.
'''
from CalcEconStats import *
from CalcForecastStats import *
from LoadRawData import *
from GetStatByDate import *
from LoadEconData import *
from LoadFinancialData import *

def LoadAllData():
    '''This program is to load all the necessary data'''
            
    try:
        print 'Loading Data...'
        
        'load data'
        econdata = CalcEconStats()
        forecastdata = CalcForecastStats()
        GDPdata, FOMCdata = LoadEconData()
        financialdata = LoadFinancialData()
        releasedateunemploy, releasedateCPI, releasedatePCE = LoadEconStatDates()

        print ' '
        print 'Data Loading complete!'
        
        return econdata, forecastdata, GDPdata, FOMCdata, financialdata, releasedateunemploy, releasedateCPI, releasedatePCE
    except urllib2.URLError:
        raise
    except IOError:
        raise
    except EOFError:
        raise
    except KeyboardInterrupt:
        raise

