# the straight forward though would be get a random number between 0 ~ total weights
# Then use the random weight to determine the index of the items, this method is called "roulette" method
# which requires to use random generator.
# After the random number is selected, to find out the index is to minus the weight respectively until a negative result
# is shown, this required we sorted items by weight
import random


class WeightSampler(object):
    def __init__(self):
        self.total_weight = 0
        self.sample_dict = {}
        self.tuples = []

    def insert(self, name, weight):
        if self.sample_dict.has_key(name):
            pre_weight = self.sample_dict[name]
            self.total_weight -= pre_weight
            self.sample_dict[name] = weight
        else:

            self.sample_dict[name] = weight
        self.total_weight += weight
        self.tuples = sorted(self.sample_dict.items(), key=lambda (key,value):value,reverse=True)

    def get(self):
        rnd = random.random() * self.total_weight
        for (name, weight) in self.tuples:
            rnd -= weight
            if rnd < 0:
                return (name, weight)


if __name__ == '__main__':
    weightSampler = WeightSampler()
    weightSampler.insert('Apple', 100)
    weightSampler.insert('Goole', 200)
    weightSampler.insert('Amazon', 150)
    # weightSampler.insert('Apple', 300)

    name_dict = dict()
    for i in range(2000):
        (name, weight) = weightSampler.get()
        if name_dict.has_key(name):
            name_dict[name] += 1
        else:
            name_dict[name] = 1

    print name_dict
