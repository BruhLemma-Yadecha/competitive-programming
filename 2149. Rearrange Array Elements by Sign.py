class Solution(object):
    def rearrangeArray(self, nums):
        positives = [x for x in nums if x > 0]
        negatives = [x for x in nums if x < 0]
        result = [item for pair in zip(positives, negatives) for item in pair]
        if len(positives) > len(negatives):
            result.append(positives[-1])
        elif len(positives) < len(negatives):
            result.insert(0, negatives[0])
        return result
