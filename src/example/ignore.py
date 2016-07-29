import csv

with open('sampleCSV.csv', 'rb') as inf:
    has_header = csv.Sniffer().has_header(inf.read(1024))
    inf.seek(0)  # rewind
    incsv = csv.reader(inf)
    if has_header:
        next(incsv)  # skip header row
    column = 1
    datatype = float
    data = (datatype(row[column]) for row in incsv)
    least_value = min(data)

print least_value