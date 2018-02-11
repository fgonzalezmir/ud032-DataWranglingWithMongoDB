#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd

datafile = r"C:\Users\Usuario\Desktop\2013_ERCOT_Hourly_Load_Data.xls"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    
    cv = sheet.col_values(1, start_rowx=1, end_rowx=None)    
    
    maxval = max(cv)
    minval = min(cv)
    
    maxpos = cv.index(maxval) + 1
    minpos = cv.index(minval) + 1

    maxtime = sheet.cell_value(maxpos,0)
    realtime = xlrd.xldate_as_tuple(maxtime,0)
    mintime = sheet.cell_value(minpos,0)
    realmintime=xlrd.xldate_as_tuple(mintime,0)
    
    print(realmintime)

    ### other useful methods:
#    print ("\nROWS, COLUMNS, and CELLS:")
#    print ("Number of rows in the sheet:",) 
#    print (sheet.nrows)
#    print ("Number of rows in the sheet:",) 
#    print (sheet.ncols)
#    
#    print ("HEADERS")
#    print (sheet.row_values(0))
#
#    print ("Type of data in cell (row 3, col 2):",) 
#    print (sheet.cell_type(3, 2))
#    print ("Value in cell (row 3, col 2):",) 
#    print (sheet.cell_value(3, 1))
#    print ("Get a slice of values in column 3, from rows 1-3:")
#    print (sheet.col_values(3, start_rowx=0, end_rowx=4))
    
    
    data = {
            'maxtime': realtime,
            'maxvalue': maxval,
            'mintime': realmintime,
            'minvalue': minval,
            'avgcoast': sum(cv)/float(len(cv))
    }
    return data

def test():
#    open_zip(datafile)
    data = parse_file(datafile)
    
    print (data)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)



test()