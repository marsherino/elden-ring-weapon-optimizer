import csv

CalcCorrectValues = {}
with open('thefile.csv', newline='') as CalcCorrectGraph_ID:
    for ID in csv.reader(CalcCorrectGraph_ID):
        CalcCorrectValues[ID['ID']] = {k:v for k,v in ID.items() if k != 'ID'}

        physical_calccorrect = CalcCorrectValues['ID'][1]
        magic_calccorrect = CalcCorrectValues['ID'][2]
        fire_calccorrect = CalcCorrectValues['ID'][3]
        lightning_calccorrect = CalcCorrectValues['ID'][4]
        holy_calccorrect = CalcCorrectValues['ID'][5]
