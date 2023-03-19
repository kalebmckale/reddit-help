import os
import csv

print(os.getcwd())          
os.chdir("//mydesktop09/V5") 
print(os.getcwd())

data_filename = "data.csv"
if os.path.exists(data_file):
    try:
        with open(data_filename, encoding="utf-8-sig") as data_file:
            data = csv.reader(data_file, delimiter=",", quotechar="\"")
            for counter, row in enumerate(data):
                print(f"header row: data row #{counter}:{row}")
    except Exception as ex:
        print(f"error message: {ex}")
    else:
        print("file not found")