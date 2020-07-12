class Member:
    def __init__(self, r_d, label=None, doc_id=None):
        self._r_d = r_d
        self._label = label
        self._doc_id = doc_id
        
class Cluster:
    def __init__(self):
        self._centroid = None
        self._members = []
    def reset_members(self):
        self._members = []
    def add_member(self, member):
        self._members.append(member)
    
class Kmeans:
    def __init__(self, num_clusters):
        self._num_clusters = num_clusters
        self._clusters = [Cluster() for _ in range(self._num_clusters)]
        self._E = [] # list of centroids
        self._S = 0 # overall similarity

    def load_data(self, data_path):
        def sparse_to_dense(sparse_r_d, vocab_size):

        
        with open(data_path) as f:
            d_lines = f.read().splitlines()
        with open('./datasets/20news-bydate/words_idfs.txt') as f:
            vocab_size = len(f.read().splitlines())

        self._data = []
        self._label_count = defaultdict(int)
        for data_id, d in enumerate(d_lines):
            features = d.split('<fff>')
            label, doc_id 
    def random_init(self, seed_value):
        
    def compute_similarity(self, member, centroid):
        
    def select_cluster_for(self, member):
        best_fit_cluster = None
        max_similarity = -1
        for cluster in self.clusters:
            similarity = self.compute_similarity(member, cluster._centroid)
            if similarity > max_similarity:
                best_fit_cluster = cluster
                max_similarity = similarity
        
        best_fit_cluster.add_member(member)
        return max_similarity
        
    def stopping_condition(self, criterion, threshold):
        
    def run(self, seed_value, criterion, threshold):
        self.random_init(seed_value)

        # continually update clusters until converge
        self._iteration = 0
        while True:
            # reset clusters, retain only centroids
            for cluster in self._clusters:
                cluster.reset_members()
            self._new_S = 0
            for member in self.data:
                max_s = self.select_cluster_for(member)
                self._new_S += max_s
            for cluster in self._clusters:
                self.update_centroid_of(cluster)

            self._iteration += 1
            if self.stopping_condition(criterion, threshold):
                break
        
    def compute_purity(self):
        
    def compute_NMI(self):