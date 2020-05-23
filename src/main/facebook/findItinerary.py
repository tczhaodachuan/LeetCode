class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        itinerary_map = {}
        for [depart, arrive] in tickets:
            if depart in itinerary_map:
                itinerary_map[depart].append(arrive)
            else:
                itinerary_map[depart] = [arrive]

        for airport in itinerary_map.keys():
            itinerary_map[airport].sort()
        # find a way to use all tickets, thus it's a permutation problem
        result = []
        self.travel('JFK', itinerary_map, result)
        return result[::-1]

    def travel(self, airport, itinerary_map, result):
        # post order traversal, changes the graph to the tree
        next_dests = itinerary_map.get(airport, [])
        while len(next_dests) > 0:
            # pop up the ticket, so next time it won't be used again
            self.travel(next_dests.pop(0), itinerary_map, result)

        # the leaf airport is the destination
        result.append(airport)


if __name__ == '__main__':
    s = Solution()
    print s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    print s.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])
