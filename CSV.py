__author__ = 'MatthewHan'
import csv

with open('us-500.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile)
    rownum = 0
    for row in reader:
        if rownum == 0:
            header = row
        else:
            colnum = 0
            for col in row:
                print '%-12s: %s' % (header[colnum], col)
                colnum+=1
        rownum+=1
