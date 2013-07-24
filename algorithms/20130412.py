"""
guidetodatamining.com    DataMining-ch3.pdf
"""
from _20130409 import recommender


users2 = {"Amy": {"Taylor Swift": 4, "PSY": 3, "Whitney Houston": 4},
          "Ben": {"Taylor Swift": 5, "PSY": 2},
          "Clara": {"PSY": 3.5, "Whitney Houston": 4},
          "Daisy": {"Taylor Swift": 5, "Whitney Houston": 3}}


class recommender2(recommender):
    
    def __init__(self, data, k=1, metric='pearson', n=5):
        self.frequencies = {}
        self.deviations = {}
        recommender.__init__(self, data, k, metric, n)

    def computeDeviations(self):
        for ratings in self.data.values():
            for (item, rating) in ratings.items():
                self.frequencies.setdefault(item, {})
                self.deviations.setdefault(item, {})
                for (item2, rating2) in ratings.items():
                    if item != item2:
                        self.frequencies[item].setdefault(item2, 0)
                        self.deviations[item].setdefault(item2, 0.0)
                        self.frequencies[item][item2] += 1
                        self.deviations[item][item2] += rating - rating2
        for (item, ratings) in self.deviations.items():
            for item2 in ratings:
                ratings[item2] /= self.frequencies[item][item2]
    
    def slopeOneRecommendations(self, userRatings):
        recommendations = {}
        frequencies = {}
        for (userItem, userRating) in userRatings.items():
            for (diffItem, diffRatings) in self.deviations.items():
                if diffItem not in userRatings and \
                    userItem in self.deviations[diffItem]:
                    freq = self.frequencies[diffItem][userItem]
                    recommendations.setdefault(diffItem, 0.0)
                    frequencies.setdefault(diffItem, 0)
                    recommendations[diffItem] += (diffRatings[userItem] + \
                                                  userRating) * freq
                    frequencies[diffItem] += freq
        recommendations = [(k, v / frequencies[k]) \
                            for (k, v) in recommendations.items()]
        recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse = True)
        return recommendations

    def slopeOneRecommendationsByFsp(self, userRatings):
        recommendations = {}
        frequencies = {}
        for (diffItem, diffRatings) in self.deviations.items():
            if diffItem not in userRatings:
                recommendations[diffItem] = 0
                frequencies[diffItem] = 0
                for (userItem, userRating) in userRatings.items():
                    if userItem in diffRatings:
                        freq = self.frequencies[diffItem][userItem]
                        recommendations[diffItem] += (diffRatings[userItem] + \
                                                     userRating) * freq
                        frequencies[diffItem] += freq
        recommendations = [(k, v / frequencies[k]) for (k, v) in recommendations.items()]
        recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse = True)
        return recommendations

if __name__ == "__main__":
    r = recommender2(users2)
    r.computeDeviations()
    print r.deviations
    g = users2['Ben']
    print r.slopeOneRecommendations(g)
    print r.slopeOneRecommendationsByFsp(g)
    assert r.slopeOneRecommendations(g) == r.slopeOneRecommendationsByFsp(g)
