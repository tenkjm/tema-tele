import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import TSNE

class TextProcessor:

    def __init__(self):
        self.tsne_init = 'pca'  # could also be 'random'
        self.tsne_perplexity = 20.0
        self.tsne_early_exaggeration = 4.0
        self.tsne_learning_rate = 1000
        self.random_state = 1

    def make_clusters(self,train, num_cluster):
        # train = ["is this good?", "this is bad", "some other text here", "i am hero", "blue jeans", "red carpet", "red dog",
        #     "blue sweater", "red hat", "kitty blue"]

        vect = TfidfVectorizer()  
        X = vect.fit_transform(train)
        clf = KMeans(n_clusters=num_cluster)
        model = clf.fit(X)
        #centroids = clf.cluster_centers_

        
        #model = TSNE(n_components=2, random_state=self.random_state, init=self.tsne_init, perplexity=self.tsne_perplexity,
         #       early_exaggeration=self.tsne_early_exaggeration, learning_rate=self.tsne_learning_rate)

        #transformed_centroids = model.fit_transform(centroids)
        #print transformed_centroids
        # plt.scatter(transformed_centroids[:, 0], transformed_centroids[:, 1], marker='x')
        # plt.show()
        # raw_input()
        return model

