# -*- coding: utf-8 -*-
'''
Find the time and value of max load for each of the regions
COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
and write the result out in a csv file, using pipe character | as the delimiter.

An example output can be seen in the "example.csv" file.
'''

import xlrd
import os
import csv
from zipfile import ZipFile

datafile = r"C:\Users\Usuario\Desktop\2013_ERCOT_Hourly_Load_Data.xls"
outfile = r"C:\Users\Usuario\Desktop\2013_Max_Loads.csv"


#def open_zip(datafile):
#    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
#        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    
    data= []
    data_sh = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

#    header = sheet.row_values(0, start_colx=1, end_colx=None)
    header = sheet.row_values(0)
    
    h=['Station','Year','Month','Day','Hour','Max Load']
    data.append(h)
    
    for col in range(sheet.ncols):
        if col==0 or col == sheet.ncols-1 :
            continue
        cv = sheet.col_values(col, start_rowx=1, end_rowx=None) 
        maxval = max(cv)
        maxpos = cv.index(maxval) + 1
        maxtime = sheet.cell_value(maxpos,0)
        realtime = realtime = xlrd.xldate_as_tuple(maxtime,0)
        reg = [header[col],realtime[0],realtime[1],realtime[2],realtime[3],round(maxval,1)]
        data.append(reg)
    
    return data

def save_file(data, filename):
    # YOUR CODE HERE
    
    csv.register_dialect('pipes', delimiter='|')
    
    with open(filename,'w') as f:
        writer = csv.writer(f,dialect='pipes', lineterminator='\n')
        for row in data:
            writer.writerow(row)
    

    
def test():
#    open_zip(datafile)
    data = parse_file(datafile)

    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']
#
#    with open(outfile) as of:
#        csvfile = csv.DictReader(of, delimiter="|")
#        for line in csvfile:
#            station = line['Station']
#            if station == 'FAR_WEST':
#                for field in fields:
#                    # Check if 'Max Load' is within .1 of answer
#                    if field == 'Max Load':
#                        max_answer = round(float(ans[station][field]), 1)
#                        max_line = round(float(line[field]), 1)
#                        assert max_answer == max_line
#
#                    # Otherwise check for equality
#                    else:
#                        assert ans[station][field] == line[field]
#
#            number_of_rows += 1
#            stations.append(station)
#
#        # Output should be 8 lines not including header
#        assert number_of_rows == 8
#
#        # Check Station Names
#        assert set(stations) == set(correct_stations)

        
if __name__ == "__main__":
    test()