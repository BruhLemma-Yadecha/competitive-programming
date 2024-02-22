class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        steps = 0
        amount = capacity
        pos = -1 # start at the river
        for i in range(len(plants)):
            # go to the next plant
            if pos != i:
                steps += i - pos
                pos = i

            # water the current plant
            amount -= plants[i]

            # look forward
            if i + 1 < len(plants) and amount < plants[i + 1]:
                # walk back
                steps += pos + 1
                pos  = -1
                amount = capacity
            else:
                pos += 1
                steps += 1
        if pos >= len(plants):
            steps -= 1
        return steps
        