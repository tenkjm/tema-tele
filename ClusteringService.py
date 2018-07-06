import pika
import json
from collections import namedtuple
from json import JSONEncoder
import json
from TextProcessor import TextProcessor
from DataPreprocessor import DataPreprocessor
import configparser
import sys

from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer


if __name__ == '__main__':
    data_preprocessor = DataPreprocessor()
    text_processor = TextProcessor()

    data = data_preprocessor.readFile('neberitrubku_output.csv')
    data = data_preprocessor.cleanData(data)

   
    sse = {}
    for k in range(1, 15):
        kmeans = text_processor.make_clusters(data, k)
        #data["clusters"] = kmeans.labels_
        #print(data["clusters"])
        sse[k] = kmeans.inertia_ # Inertia: Sum of distances of samples to their closest cluster center
    plt.figure()
    plt.plot(list(sse.keys()), list(sse.values()))
    plt.xlabel("Number of cluster")
    plt.ylabel("SSE")
    plt.show()

    ok_model=text_processor.make_clusters_and_show_results(data, 5)
    vect = TfidfVectorizer()  
    X = vect.fit_transform(data)

    for i in range (0, len(data)-1):
        print data[i] , " cluster = ", ok_model.predict(X[i])
    



