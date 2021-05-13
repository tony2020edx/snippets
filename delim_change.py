import csv

reader = csv.reader(open("output11.csv", newline=None), delimiter=',')
writer = csv.writer(open("outputv12.csv", 'w'), delimiter=';')
writer.writerows(reader)
