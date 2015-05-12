'''
Filename: PlotFinancialData.py
Created by: Joseph Song
Last version on: 5/11/2015
Description: This is a class to load the financial data and set up the plots

'''
from datetime import datetime
from LoadRawData import loadcsvdata
from LoadFinancialData import *
import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib.dates import WeekdayLocator
from matplotlib.dates import MO

class PlotFinancialData:
    '''This class takes in the begin and end date for the financial data to plot'''

    def __init__(self, dataset, begindate, enddate):
        ''' Turn the begindate and enddate string into python datetime'''
        self.start = begindate
        self.end = enddate
        self.filenamedate = self.end.replace('/', '-')
        self.financialdata = dataset
        self.interval = (self.financialdata.index>self.start) & (self.financialdata.index<self.end)
        self.truncatedfinancialdata = self.financialdata.loc[self.interval]

    def MakeFinancialPlots(self):
        '''Create the plots for analysis'''
        plt.close()
        fig = plt.figure()
        fig.suptitle('Financial Data Between ' + self.start + ' and ' + self.end)
        
        'SP500 plot (top left)'
        ax1 = fig.add_subplot(3,2,1)
        ax1.set_title('S&P 500 Composite')
        ax1.plot(self.truncatedfinancialdata.index, self.truncatedfinancialdata['sp500'])
        ax1.axes.get_xaxis().set_visible(False)
        
        'Spot Dollar Index (top right)'
        ax2 = fig.add_subplot(3,2,2)
        ax2.set_title('Spot Dollar Index')
        ax2.plot(self.truncatedfinancialdata.index, self.truncatedfinancialdata['dxy'])
        ax2.axes.get_xaxis().set_visible(False)

        '2-year Treasury Yield (middle left)'
        ax3 = fig.add_subplot(3,2,3)
        ax3.set_title('2-Year Treasury Yields')
        ax3.plot(self.truncatedfinancialdata.index, self.truncatedfinancialdata['tsy2yr'])
        ax3.axes.get_xaxis().set_visible(False)

        '5-year Treasury Yield (middle right)'
        ax4 = fig.add_subplot(3,2,4)
        ax4.set_title('5-Year Treasury Yields')
        ax4.plot(self.truncatedfinancialdata.index, self.truncatedfinancialdata['tsy5yr'])
        ax4.axes.get_xaxis().set_visible(False)

        '10-year Treasury Yield (lower left) '
        ax5 = fig.add_subplot(3,2,5)
        ax5.set_title('10-Year Treasury Yields')
        ax5.plot(self.truncatedfinancialdata.index, self.truncatedfinancialdata['tsy10yr'])
        ax5.xaxis.set_major_formatter(dates.DateFormatter('%m/%d'))
        ax5.xaxis.set_major_locator(WeekdayLocator(byweekday=MO, interval=2))
        
        '30-year Treasury Yield (lower right)'
        ax6 = fig.add_subplot(3,2,6)
        ax6.set_title('30-Year Treasury Yields')
        ax6.plot(self.truncatedfinancialdata.index, self.truncatedfinancialdata['tsy30yr'])
        ax6.xaxis.set_major_formatter(dates.DateFormatter('%m/%d'))
        ax6.xaxis.set_major_locator(WeekdayLocator(byweekday=MO, interval=2))
        
        'Print out file to PDF'
        filename = 'Financial_Data_for_' + self.filenamedate + "_FOMC" + '.pdf'
        plt.savefig(filename)
        plt.show()




