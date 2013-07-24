# -*- encoding: utf-8 -*-
import pprint

data  = [['i100', 'both', 'sedentary', 'moderate', 'yes'],
         ['i100', 'both', 'sedentary', 'moderate', 'no'],
         ['i500', 'health', 'sedentary', 'moderate', 'yes'],
         ['i500', 'appearance', 'active', 'moderate', 'yes'],
         ['i500', 'appearance', 'moderate', 'aggressive', 'yes'],
         ['i100', 'appearance', 'moderate', 'aggressive', 'no'],
         ['i500', 'health', 'moderate', 'aggressive', 'no'],
         ['i100', 'both', 'active', 'moderate', 'yes'],
         ['i500', 'both', 'moderate', 'aggressive', 'yes'],
         ['i500', 'appearance', 'active', 'aggressive', 'yes'],
         ['i500', 'both', 'active', 'aggressive', 'no'],
         ['i500', 'health', 'active', 'moderate', 'no'],
         ['i500', 'health', 'sedentary', 'aggressive', 'yes'],
         ['i100', 'appearance', 'active', 'moderate', 'no'],
         ['i100', 'health', 'sedentary', 'moderate', 'no']]

dataSample = {'i500': [{'health': 0.44444444444444442, 
                        'appearance': 0.33333333333333331,
                        'both': 0.22222222222222221}, 
                       {'active': 0.44444444444444442, 
                        'sedentary': 0.22222222222222221, 
                        'moderate': 0.33333333333333331}, 
                       {'aggressive': 0.66666666666666663, 
                        'moderate': 0.33333333333333331},
                       {'yes': 0.66666666666666663, 
                        'no': 0.33333333333333331}], 

              'i100': [{'both': 0.5, 
                        'health': 0.16666666666666666, 
                        'appearance': 0.33333333333333331},
                       {'active': 0.33333333333333331, 
                        'sedentary': 0.5, 
                        'moderate': 0.16666666666666666}, 
                       {'moderate': 0.83333333333333337, 
                        'aggressive': 0.16666666666666666}, 
                       {'yes': 0.33333333333333331, 
                        'no': 0.66666666666666663}]}

class Bayes(object):
    
    def __init__(self, data):
        # here I am assuming the first column of the data is the class.
        self.data = data
        self.prior = {}
        self.conditional = {}

    def train(self):
        """train the Bayes Classifier
        basically a lot of counting"""
        total = 0
        classes = {}
        counts = {}
        # determine size of a training vector
        size = len(self.data[0])
        # iterate through training instances
        for instance in self.data:
            total += 1
            category = instance[0]
            classes.setdefault(category, float(0))
            counts.setdefault(category, {})
            classes[category] += 1
            # now process each column in instance
            col = 0
            for columnValue in instance[1:]:
                col += 1
                tmp = {}
                if col in counts[category]:
                    tmp = counts[category][col]
                if columnValue in tmp:
                        tmp[columnValue] += 1
                else:
                    tmp[columnValue] = float(1)
                counts[category][col] = tmp
        for (category, count) in classes.items():
            self.prior[category] = count / total
        for (category, columns) in counts.items():
            tmp = {}
            for (col, valueCounts) in columns.items():
                tmp2 = {}
                for (value, count) in valueCounts.items():
                    tmp2[value] = count / classes[category]
                tmp[col] = tmp2
            tmp3 = []
            for i in range(1, size):
                tmp3.append(tmp[i])
            self.conditional[category] = tmp3

    def classify(self, instance):
        categories = {}
        for (category, vector) in self.conditional.items():
            prob = 1
            for i in range(len(vector)):
                colProbability = .0000001
                if instance[i] in vector[i]:
                    colProbability = vector[i][instance[i]]
                prob = prob * colProbability
            prob = prob * self.prior[category]
            categories[category] = prob
        cat = list(categories.items())
        # pprint.pprint(cat)
        # pprint.pprint(self.prior)
        # pprint.pprint (self.conditional)
        cat.sort(key=lambda catTuple: catTuple[1], reverse = True)
        return(cat[0])

if __name__ == '__main__':
    b = Bayes(data)
    b.train()
    print b.classify(['health', 'moderate', 'moderate', 'yes'])
    print b.classify(['appearance', 'moderate', 'moderate', 'no'])
