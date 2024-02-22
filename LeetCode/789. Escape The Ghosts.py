class Solution(object):
    def distance2D(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: float
        """
        return abs(b[1] - a[1]) + abs(b[0] - a[0])

    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        # calculate the distance to the target for every ghost and the player
        player = [0, 0]
        player_distance = self.distance2D(player, target)

        for ghost in ghosts:
            if self.distance2D(ghost, target) <= player_distance:
                return False
        return True
        