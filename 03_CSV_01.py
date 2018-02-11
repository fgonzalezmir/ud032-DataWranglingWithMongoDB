"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
from pprint import pprint
import dateutil.parser

INPUT_FILE = r'C:\Users\Usuario\Desktop\autos.csv'
OUTPUT_GOOD = r'C:\Users\Usuario\Desktop\autos-valid.csv'
OUTPUT_BAD = r'C:\Users\Usuario\Desktop\FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        

        #COMPLETE THIS FUNCTION
        
        good=[]
        bad=[]

        for car in reader:
            if len(car)<58:
                bad.append(car)
                continue
            
            if not car["URI"].startswith('http://dbpedia.org/resource/'):

                continue
            
            if car["productionStartYear"] == "NULL" or car["productionStartYear"] == "":
                bad.append(car)
                continue
            
            dt = dateutil.parser.parse(car["productionStartYear"])
            if dt.year <1886 or dt.year>2014:
                bad.append(car)
                continue
            
            car["productionStartYear"]= dt.year
            good.append(car)
        
            



    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files
    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", lineterminator='\n', fieldnames= header)
        writer.writeheader()
        for row in good:
            writer.writerow(row)
            
    with open(output_bad, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", lineterminator='\n', fieldnames= header)
        writer.writeheader()
        for row in bad:
            writer.writerow(row)


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()