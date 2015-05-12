'''
Filename: Main_Run.py
Created by: Joseph Song
Last version on: 5/11/2015
Description: This is the main program that takes in the user input
and connects to the other functions/classes. The user input is 
the FOMC meeting date of interest. Once that is passed through,
economic statistics and financial charts are produced. It keeps asking for
user input until the user decides to quit.
'''

from LoadAllData import *
from GetFOMCDate import *
from PlotFinancialData import *
from SelectFOMCMtgDate import *

if __name__ == '__main__':
    '''This is the main file to run the program'''

    'Boolean trigger to bounce out of the loop if user quits'
    trigger = False

    try:
        'This Loads all the Data neccessary for the analysis'
        econdata, forecastdata, GDPdata, FOMCdata, financialdata, releasedateunemploy, releasedateCPI, releasedatePCE = LoadAllData()
        
        'Takes in user input'
        userinput = " "
        while(trigger == False):
            try:
                userinput = raw_input("Enter the Year of the FOMC Meeting (2000-2015) or type quit:" + '\n')
                if userinput.lower()== "quit":
                    trigger = True
                else:
                    year = int(userinput)
                    if (year > 1999) & (year < 2016):
                        
                        'This function guides the user to a correct FOMC meeting date'
                        FOMCdate = SelectFOMCMtgDate(year)
                    
                        'Calculate the economic statistics to display'
                        unemploymentrate, CPI, coreCPI, PCE, corePCE, unemployreferencedate, CPIreferencedate, PCEreferencedate = GetEconStatByDate(econdata, releasedateunemploy, releasedateCPI, releasedatePCE, FOMCdate)
                        GDP, year, quarter = GetGDPDataByDate(GDPdata, FOMCdate)
                        date, FFunds, ChngFFunds = GetFOMCDataByDate(FOMCdata, FOMCdate)
                        CPIforecast, Unemploymentrateforecast, GDPforecast = GetForecastDataByDate(forecastdata, FOMCdate)
                        FOMCdate, prevFOMCdate = GetFOMCDate(FOMCdate, FOMCdata)

                        'Display results'
                        print 'These are the economic statisics and forecasts available at the time of the ' + FOMCdate + ' FOMC meeting'
                        print 'The unemployment rate on ' + str(unemployreferencedate[0].date()) + ' was ' + unemploymentrate[0] + ' percent'
                        print 'The CPI and core CPI inflation rate on ' + str(CPIreferencedate[0].date()) + ' was ' + str(CPI[0]) + ' percent and ' + str(coreCPI[0]) + ' percent, respectively'
                        print 'The PCE and core PCE inflation rate on ' + str(PCEreferencedate[0].date()) + ' was ' + str(PCE[0]) + ' percent and ' + str(corePCE[0]) + ' percent, respectively'
                        print 'GDP annualized percent change for ' + str(int(year)) + 'Q'+ str(int(quarter)) + ' was ' +  str(GDP) + ' percent' 
                        print 'The 4 quarter ahead forecast for unemployment rate, CPI, and GDP are ' + str(Unemploymentrateforecast) + ' percent, ' + str(CPIforecast) + ' percent, and ' + str(GDPforecast) + ' percent, respectively' 
                        print 'At the selected FOMC meeting, the Committee decided to set the federal funds rate at ' + str(FFunds) + ' a change of ' + str(ChngFFunds) + ' from the prior meeting'
                
                        financialplots  = PlotFinancialData(financialdata, prevFOMCdate, FOMCdate)
                        financialplots.MakeFinancialPlots()       
                
            except:
                print("Incorrect input, please try a 4 digit year between 2000-2015 or quit")
    except urllib2.URLError, e:
        print 'Internet connection is down or St.Louis Fed FRED Server is down'
        print e.reason
        print 'Recheck connection...GoodBye'
    except IOError:
        print 'One of the files (see above) needed to run the program is missing or misspelled...GoodBye'
    except EOFError:
        print 'End of File Error--Goodbye'
    except KeyboardInterrupt:
        print 'Keyboard interrupt received: GoodBye'
    print 'Good Bye'
