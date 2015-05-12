'''
Filename: SelectFOMCMtgDate.py
Created by: Joseph Song
Created on: May 11, 2015
Description: This runs through all the FOMC meeting date options and returns the
meeting date as a string to feed into the analysis
'''


def SelectFOMCMtgDate(date):
    '''This function determines which meeting date to analyze'''
    if date == 2000:
        userinput = raw_input('Please type one of the meeting dates: 3/21, 5/16, 6/28, 8/22, 10/3, 11/15, 12/19' + '\n')
        list2000 = ['3/21', '5/16', '6/28', '8/22', '10/3', '11/15', '12/19', 'quit']
        while userinput not in list2000:
            userinput = raw_input('Please type one of the meeting dates: 3/21, 5/16, 6/28, 8/22, 10/3, 11/15, 12/19' + '\n')
        mtgdate = str('2000/'+userinput)
        return mtgdate
        
    elif date == 2001:
        userinput = raw_input('Please type one of the meeting dates: 1/3, 1/31, 3/20, 4/18, 5/15, 6/27, 8/21, 9/17, 10/2, 11/6, 12/11' + '\n')
        list2001 = ['1/3', '1/31', '3/20', '4/18', '5/15', '6/27', '8/21', '9/17', '10/2', '11/6', '12/11', 'quit']
        while userinput not in list2001:
            userinput = raw_input('Please type one of the meeting dates: 1/3, 1/31, 3/20, 4/18, 5/15, 6/27, 8/21, 9/17, 10/2, 11/6, 12/11' + '\n')
        mtgdate = str('2001/'+userinput)

    elif date == 2002:
        userinput = raw_input('Please type one of the meeting dates: 1/30, 3/19, 5/7, 6/26, 8/13, 9/24, 11/6, 12/10' + '\n')
        list2002 = ['1/30', '3/19', '5/7', '6/26', '8/13', '9/24', '11/6', '12/10', 'quit']
        while userinput not in list2002:
            userinput = raw_input('Please type one of the meeting dates: 1/30, 3/19, 5/7, 6/26, 8/13, 9/24, 11/6, 12/10' + '\n')
        mtgdate = str('2002/'+userinput)
            
    elif date == 2003:
        userinput = raw_input('Please type one of the meeting dates: 1/29, 3/18, 5/6, 6/25, 8/12, 9/16, 10/28, 12/9' + '\n')
        list2003 = ['1/29', '3/18', '5/6', '6/25', '8/12', '9/16', '10/28', '12/9', 'quit']
        while userinput not in list2003:
            userinput = raw_input('Please type one of the meeting dates: 1/29, 3/18, 5/6, 6/25, 8/12, 9/16, 10/28, 12/9' + '\n')
        mtgdate = str('2003/'+userinput)

    elif date == 2004:
        userinput = raw_input('Please type one of the meeting dates: 1/28, 3/16, 5/4, 6/30, 8/10, 9/21, 11/10, 12/14' + '\n')
        list2004 = [ '1/28', '3/16', '5/4', '6/30', '8/10', '9/21', '11/10', '12/14', 'quit']
        while userinput not in list2004:
            userinput = raw_input('Please type one of the meeting dates: 1/28, 3/16, 5/4, 6/30, 8/10, 9/21, 11/10, 12/14' + '\n')
        mtgdate = str('2004/'+userinput)
        
    elif date == 2005:
        userinput = raw_input('Please type one of the meeting dates: 2/2, 3/22, 5/3, 6/30, 8/9, 9/20, 11/1, 12/13' + '\n')
        list2005 = [ '2/2', '3/22', '5/3', '6/30', '8/9', '9/20', '11/1', '12/13', 'quit']
        while userinput not in list2005:
            userinput = raw_input('Please type one of the meeting dates: 2/2, 3/22, 5/3, 6/30, 8/9, 9/20, 11/1, 12/13' + '\n')
        mtgdate = str('2005/'+userinput)
        
    elif date == 2006:
        userinput = raw_input('Please type one of the meeting dates: 1/31, 3/28, 5/10, 6/29, 8/8, 9/20, 10/25, 12/12' + '\n')
        list2006 = [ '1/31', '3/28', '5/10', '6/29', '8/8', '9/20', '10/25', '12/12', 'quit']
        while userinput not in list2006:
            userinput = raw_input('Please type one of the meeting dates: 1/31, 3/28, 5/10, 6/29, 8/8, 9/20, 10/25, 12/12' + '\n')
        mtgdate = str('2006/'+userinput)
        
    elif date == 2007:
        userinput = raw_input('Please type one of the meeting dates: 1/31, 3/21, 5/9, 6/28, 8/7, 9/18, 10/31, 12/11' + '\n')
        list2007 = [ '1/31', '3/21', '5/9', '6/28', '8/7', '9/18', '10/31', '12/11', 'quit']
        while userinput not in list2007:
            userinput = raw_input('Please type one of the meeting dates: 1/31, 3/21, 5/9, 6/28, 8/7, 9/18, 10/31, 12/11' + '\n')
        mtgdate = str('2007/'+userinput)

    elif date == 2008:
        userinput = raw_input('Please type one of the meeting dates: 1/22, 1/30, 3/18, 4/30, 6/25, 8/5, 9/16, 10/8, 10/29, 12/16' + '\n')
        list2008 = [ '1/22', '1/30', '3/18', '4/30', '6/25', '8/5', '9/16', '10/8', '10/29', '12/16', 'quit']
        while userinput not in list2008:
            userinput = raw_input('Please type one of the meeting dates: 1/22, 1/30, 3/18, 4/30, 6/25, 8/5, 9/16, 10/8, 10/29, 12/16' + '\n')
        mtgdate = str('2008/'+userinput)

    elif date == 2009:
        userinput = raw_input('Please type one of the meeting dates: 1/28, 3/18, 4/29, 6/24, 8/12, 9/23, 11/4, 12/16' + '\n')
        list2009 = [ '1/28', '3/18', '4/29', '6/24', '8/12', '9/23', '11/4', '12/16', 'quit']
        while userinput not in list2009:
            userinput = raw_input('Please type one of the meeting dates: 1/28, 3/18, 4/29, 6/24, 8/12, 9/23, 11/4, 12/16' + '\n')
        mtgdate = str('2009/'+userinput)

    elif date == 2010:
        userinput = raw_input('Please type one of the meeting dates: 1/27, 3/16, 4/28, 5/9, 6/23, 8/10, 9/21, 11/3, 12/14' + '\n')
        list2010 = [ '1/27', '3/16', '4/28', '5/9', '6/23', '8/10', '9/21', '11/3', '12/14', 'quit']
        while userinput not in list2010:
            userinput = raw_input('Please type one of the meeting dates: 1/27, 3/16, 4/28, 5/9, 6/23, 8/10, 9/21, 11/3, 12/14' + '\n')
        mtgdate = str('2010/'+userinput)

    elif date == 2011:
        userinput = raw_input('Please type one of the meeting dates: 1/26, 3/15, 4/27, 6/22, 8/9, 9/21, 11/2, 12/13' + '\n')
        list2011 = [ '1/26', '3/15', '4/27', '6/22', '8/9', '9/21', '11/2', '12/13', 'quit']
        while userinput not in list2011:
            userinput = raw_input('Please type one of the meeting dates: 1/26, 3/15, 4/27, 6/22, 8/9, 9/21, 11/2, 12/13' + '\n')
        mtgdate = str('2011/'+userinput)

    elif date == 2012:
        userinput = raw_input('Please type one of the meeting dates: 1/25, 3/13, 4/25, 6/20, 8/1, 9/13, 10/24, 12/12' + '\n')
        list2012 = ['1/25', '3/13', '4/25', '6/20', '8/1', '9/13', '10/24', '12/12', 'quit']
        while userinput not in list2012:
            userinput = raw_input('Please type one of the meeting dates: 1/25, 3/13, 4/25, 6/20, 8/1, 9/13, 10/24, 12/12' + '\n')
        mtgdate = str('2012/'+userinput)

    elif date == 2013:
        userinput = raw_input('Please type one of the meeting dates: 1/30, 3/20, 5/1, 6/19, 7/31, 9/18, 10/30, 12/18' + '\n')
        list2013 = ['1/30', '3/20', '5/1', '6/19', '7/31', '9/18', '10/30', '12/18', 'quit']
        while userinput not in list2013:
            userinput = raw_input('Please type one of the meeting dates: 1/30, 3/20, 5/1, 6/19, 7/31, 9/18, 10/30, 12/18' + '\n')
        mtgdate = str('2013/'+userinput)

    elif date == 2014:
        userinput = raw_input('Please type one of the meeting dates: 1/29, 3/19, 4/30, 6/18, 7/30, 9/17, 10/29, 12/17' + '\n')
        list2014 = ['1/29', '3/19', '4/30', '6/18', '7/30', '9/17', '10/29', '12/17', 'quit']
        while userinput not in list2014:
            userinput = raw_input('Please type one of the meeting dates: 1/29, 3/19, 4/30, 6/18, 7/30, 9/17, 10/29, 12/17' + '\n')
        mtgdate = str('2014/'+userinput)

    elif date == 2015:
        userinput = raw_input('Please type one of the meeting dates: 1/28, 3/18, 4/29' + '\n')
        list2015 = ['1/28', '3/18', '4/29', 'quit']
        while userinput not in list2015:
            userinput = raw_input('Please type one of the meeting dates: 1/28, 3/18, 4/29' + '\n')
        mtgdate = str('2015/'+userinput)   
    return mtgdate
