import pika
import json
from collections import namedtuple
from json import JSONEncoder
import json
from TextProcessor import TextProcessor
from DataPreprocessor import DataPreprocessor

import configparser
import sys


if __name__ == '__main__':
    data_preprocessor = DataPreprocessor()
    text_processor = TextProcessor()

    data = data_preprocessor.readFile('neberitrubku_output.csv')
    data = data_preprocessor.cleanData(data)

    text_processor.make_clusters(data)
    raw_input()
    
    



