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


class PickIndexWithWeight(object):

	def __init__(self, w):
		"""
		:type w: List[int]
		"""
		self.total = sum(w)
		self.w = w
		self.weights = sorted(w)
		self.min = self.weights[0]
		self.max = self.weights[-1]

	def pickIndex(self):
		"""
		:rtype: int
		"""
		import random
		num = random.uniform(0.0, 1.0) * self.total
		cum = 0
		for i, m in enumerate(self.weights):
			cum += m
			if cum > num:
				return self.w.index(self.weights[i])


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

    pick = PickIndexWithWeight([10, 7, 8, 10])
    results = {}
    for i in range(1000):
	    index = pick.pickIndex()
	    results[index] = results.get(index, 1) + 1

    total = pick.total
    for key, value in results.iteritems():
	    print key, value / 1000.0 * 100
