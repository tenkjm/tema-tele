import csv
import string
import re


class DataPreprocessor:   
    def unicode_csv_reader(self,utf8_data, dialect=csv.excel, **kwargs):
        csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
        for row in csv_reader:
            yield [unicode(cell, 'utf-8') for cell in row]

    def readFile(self,filename):
        data=[]
        reader = self.unicode_csv_reader(open(filename))
        for categories,descriptions,phone_number,source,titles in reader:
            data.append(descriptions)
        return data
    def cleanData(self, data):
        return [re.sub('['+string.punctuation+']', '', row) for row in data]

