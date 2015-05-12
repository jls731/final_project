'''
Filename: Unittest_FinalProject.py
Created by: Joseph Song
Created on: May 11, 2015
Description: This is the unit test to test the package to make sure 
all the necessary programs/files exist.
'''
import unittest
import os.path

class Test(unittest.TestCase):


    def testfileexist(self):
        self.assertTrue(os.path.exists("./CalcEconStats.py"), 'The File does not exist')
        self.assertTrue(os.path.exists("./CalcForecastStats.py"), 'The File does not exist')
        self.assertTrue(os.path.exists("./CPI.csv"), 'The File does not exist')
        self.assertTrue(os.path.exists("./DXY.csv"), 'The File does not exist')
        self.assertTrue(os.path.exists("./FOMC.csv"), 'The File does not exist')
        self.assertTrue(os.path.exists("./GDP.csv"), 'The File does not exist')
        self.assertTrue(os.path.exists("./GetFOMCDate.py"), 'The File does not exist')
        self.assertTrue(os.path.exists("./GetStatByDate.py"), 'The File does not exist')
        self.assertTrue(os.path.exists("./__init__.py"), 'The File does not exist')
        self.assertTrue(os.path.exists("./LoadAllData.py"), 'The File does not exist')
        self.assertTrue(os.path.exists("./LoadEconData.py"), 'The File does not exist')
        self.assertTrue(os.path.exists("./LoadEconStatDates.py"), 'The File does not exist')
        self.assertTrue(os.path.exists("./LoadFinancialData.py"), 'The File does not exist')
        self.assertTrue(os.path.exists("./LoadRawData.py"), 'The File does not exist')
        self.assertTrue(os.path.exists("./Main_Run.py"), 'The File does not exist')
        self.assertTrue(os.path.exists("./Median_CPI_Level.xls"), 'The File does not exist')
        self.assertTrue(os.path.exists("./Median_RGDP_Level.xls"), 'The File does not exist')
        self.assertTrue(os.path.exists("./Median_UNEMP_Level.xls"), 'The File does not exist')
        self.assertTrue(os.path.exists("./PCE.csv"), 'The File does not exist')
        self.assertTrue(os.path.exists("./PlotFinancialData.py"), 'The File does not exist')
        self.assertTrue(os.path.exists("./SelectFOMCMtgDate.py"), 'The File does not exist')
        self.assertTrue(os.path.exists("./SP500.csv"), 'The File does not exist')
        self.assertTrue(os.path.exists("./TSY2YR.csv"), 'The File does not exist')
        self.assertTrue(os.path.exists("./TSY5YR.csv"), 'The File does not exist')
        self.assertTrue(os.path.exists("./TSY10YR.csv"), 'The File does not exist')
        self.assertTrue(os.path.exists("./TSY30YR.csv"), 'The File does not exist')
        self.assertTrue(os.path.exists("./Urate.csv"), 'The File does not exist')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()