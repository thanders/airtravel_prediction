import math
import itertools
import pprint

class PathCalculation:
    def __init__(self, unordered_itinerary):
        # Variables to store OWM connection data:
        self._unordered_itinerary = unordered_itinerary
        self._permutations_dict = {}

    def create_permutations(self):
        # permutations:
        perm = list(itertools.permutations(self._unordered_itinerary))
        print(perm)
        start_point = perm[0][0]
        perm_list = []
        itinerary_dist = []
        for i in perm:
            for j in i:
                perm_list.append(j)
        counter = 0
        perm_counter = 0
        print('Number of permutations:', len(perm))
        print('Number of permutations:', len(perm_list))
        for i in range(0, len(perm_list)):

            if i % 3 == 0:
                perm_counter += 1

                lat1 = float(self._unordered_itinerary[perm_list[i]][0])
                lat2 = float(self._unordered_itinerary[perm_list[i - 2]][0])
                long1 = float(self._unordered_itinerary[perm_list[i]][1])
                long2 = float(self._unordered_itinerary[perm_list[i - 2]][1])
            elif i == len(perm_list)-1:
                print("i equals;", i)
                lat1 = float(self._unordered_itinerary[perm_list[i]][0])
                lat2 = float(self._unordered_itinerary[perm_list[i-2]][0])
                long1 = float(self._unordered_itinerary[perm_list[i]][1])
                long2 = float(self._unordered_itinerary[perm_list[i-2]][1])
            else:
                print("i equals;", i)
                lat1 = float(self._unordered_itinerary[perm_list[i]][0])
                lat2 = float(self._unordered_itinerary[perm_list[i+1]][0])
                long1 = float(self._unordered_itinerary[perm_list[i]][1])
                long2 = float(self._unordered_itinerary[perm_list[i+1]][1])

            counter += 1

            distance = self.great_circle_distance(lat1, lat2, long1, long2)
            itinerary_dist.append(distance)

            print(itinerary_dist)

        # Citation: Stackoverflow: https://stackoverflow.com/questions/19777612/python-range-and-zip-object-type
        def grouper(iterable, n):
            args = [iter(iterable)] * n
            return zip(*args)

        groups = grouper(itinerary_dist, 3)

        print("THIS IS THE GROUPER:")
        groups = list(groups)
        sum_list = []
        for i in groups:
            group_sum = sum(i)
            sum_list.append(group_sum)

        print(sum_list)

        pl = list(itertools.permutations(self._unordered_itinerary))

        # START FROM
        '''
        start_only = []
        for i in pl:
            for j in pl: 
                if j == start_point:
                    start_only.append(i)
                
                
        print("start_only", start_only)
        '''
        import operator
        index, price = min(enumerate(sum_list), key=operator.itemgetter(1))

        shortest_path = pl[index]

        return shortest_path, price




    def great_circle_distance(self, lat1, lat2, long1, long2):

        # Prepare variables for calculation:
        radius_earth = 6371
        theta1 = long1 * (2 * math.pi) / 360
        theta2 = long2 * (2 * math.pi) / 360
        phil1 = (90 - lat1) * (2 * math.pi) / 360
        phil2 = (90 - lat2) * (2 * math.pi) / 360

        # Calculate the great circle distance:
        distance = math.acos(math.sin(phil1)
                             * math.sin(phil2) * math.cos(theta1 - theta2)
                             + math.cos(phil1) * math.cos(phil2)) * radius_earth

        return distance
'''
    @staticmethod
    def price_weighted_distance(distance):

        pw_distance = None

        return pw_distance

# Getters and setters start here:

    @property
    # Pythonic way of doing a "getter"
    def unordered_itinerary(self):
        return self._unordered_itinerary
'''


