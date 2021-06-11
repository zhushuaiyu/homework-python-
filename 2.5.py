import numpy as np


class TopicsRecommend:
    def __init__(self, uuid):
        self.uuid = uuid
        self.mysql_t = ...
        self.usr_topics = []
        self.all_topics = []

        def get_similarity_matrix(self):
            self.all_topics = [...]
            self.usr_topics = [...]
            C = np.zeros((len(self.all_topics), len(self.all_topics)), dtype=float)
            for usr_tps in self.usr_topics:
                for comb in itertools.combinations(self.usr_tps['topics'], 2):  # 倒排
                    tp1, tp2 = comb[0], comb[1]
                    if tp1 in self.all_topics and tp2 in self.all_topics:
                        C[self.all_topics.index(tp1)][self.all_topics.index(tp2)] += 1
            C += np.transpose(C)
            return C

        def recommend_topics(self):
            simi_matrix = self.get_similarity_matrix()
            if len(simi_matrix) > 0:
                tp_scores = np.zeros(len(self.all_topics), dtype=float)
                for tp in self.usr_topics:
                    if tp in self.all_topics:
                        temp_tps = list(simi_matrix[self.all_topics.index(tp)])
                        tp_scores = [tp_scores[i] + temp_tps[i] for i in range(0, len(self.all_topics))]
                score_sum = list(enumerate(tp_scores))
                score_sum.sort(key=lambda x: x[1], reverse=True)
                return [self.all_topics[x[0]] for k, x in enumerate(score_sum) if k < 10]
            else:
                return self.all_topics[:10]


res = TopicsRecommend('xxx').recommend_topics()
print(res)
