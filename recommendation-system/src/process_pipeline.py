import json

import pandas as pd
import numpy as np


class ProcessPipeline:
    def __init__(self, clustered_data_path:str = '../data/courses_clustered.parquet'):
        np.random.seed(42)
        self.data = pd.read_parquet(clustered_data_path)
        
    def get_recommendations_to_filter(self, json_string: str):
        courses = json.loads(json_string)

        rec_pool = []
        for course in courses:
            cluster_id = data.iloc[course['id']].clust_label

            rec_pool.append(data[data['clust_label'] == cluster_id].index)

        return np.random.choice(rec_pool, size=(30))


    def get_similar_cluster(self, cluster_label: int) -> pd.DataFrame:
        return self.data[data['clust_label'] == cluster_label]