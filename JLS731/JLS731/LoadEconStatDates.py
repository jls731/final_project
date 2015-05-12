'''
Filename: LoadEconStatDates.py
Created by: Joseph Song
Last version on: 5/11/2015
Description: Create a dataframe with the release dates for each economic
statistic (Unemployment Rate, CPI, Core CPI, PCE, core PCE). We need these
dates since the release date of each reference month varies by statistic
and depending on the FOMC meeting date, the latest reference month for each
statistic might differ.
'''

from LoadRawData import loadcsvdata
import pandas as pd

def LoadEconStatDates():
    '''Load the release dates for each statistic and create DataFrame'''
    try:
        unemploymentDate = loadcsvdata('Urate.csv', ['Date', 'Urate_Release'])
        CPIDate = loadcsvdata('CPI.csv', ['Date', 'CPI_Release'])
        PCEDate = loadcsvdata('PCE.csv', ['Date', 'PCE_Release'])
        
        unemploymentDate.set_index('Urate_Release', inplace = True)
        CPIDate.set_index('CPI_Release', inplace = True)
        PCEDate.set_index('PCE_Release', inplace = True)
        
        return unemploymentDate, CPIDate, PCEDate
    
    except IOError:
        print 'CPI.csv, PCE.csv or Urate.csv file is either missing or misspelled'
        raise

    