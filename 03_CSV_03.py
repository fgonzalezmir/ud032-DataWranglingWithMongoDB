
import csv
import json
import pprint

CITIES = r'C:\Users\Usuario\Desktop\cities.csv'


def fix_area(area):

    # YOUR CODE HERE
    
    if area == "NULL":
        return None
    
    if area.startswith('{'):
        area= area.replace('{','').replace('}','')
        l = area.split('|')
        max_length=""

        for s in l:
            if len(s) > len(max_length):
                max_length=s
        return float(max_length)
        
    return float(area)



def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra metadata
        for i in range(3):
            next(reader)

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print("Printing three example results:")
    for n in range(5,8):
        pprint.pprint(data[n]["areaLand"])

    assert data[3]["areaLand"] == None        
    assert data[8]["areaLand"] == 55166700.0
    assert data[20]["areaLand"] == 14581600.0
    assert data[33]["areaLand"] == 20564500.0    


if __name__ == "__main__":
    test()