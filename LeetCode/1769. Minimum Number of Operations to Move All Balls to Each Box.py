class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        left = [0 for x in range(len(boxes))]
        right = [0 for x in range(len(boxes))]
        left_boxes, right_boxes = 0, 0
        lcost, rcost = 0, 0
        for i in range(1, len(boxes)):
            if boxes[i - 1] == '1':
                left_boxes += 1
            lcost += left_boxes
            left[i] = lcost
        for i in range(len(boxes) - 2, -1, -1):
            if boxes[i + 1] == '1':
                right_boxes += 1
            rcost += right_boxes
            right[i] += rcost
        result = [left[x] + right[x] for x in range(len(boxes))]
        return result
        