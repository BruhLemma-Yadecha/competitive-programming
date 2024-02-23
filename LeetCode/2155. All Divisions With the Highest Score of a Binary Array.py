class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        l = [0] * (len(nums) + 1)  # boundary zero
        r = [0] * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] == 0:
                l[i] = l[i - 1] + 1
            else:
                l[i] = l[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            r[i] = r[i + 1] + nums[i]

        scores = [0] * (len(nums) + 1)
        for i in range(len(nums) + 1):
            scores[i] = l[i] + r[i]

        highest = max(scores)
        res = [i for i, value in enumerate(scores) if value == highest]
        return res