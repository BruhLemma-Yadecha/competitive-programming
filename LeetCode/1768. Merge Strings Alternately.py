class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        smaller_length = min(len(word1), len(word2))
        for i in range(0, smaller_length):
            result = result + word1[i] + word2[i]
        if len(word1) > smaller_length:
            result += word1[smaller_length:]
        elif len(word2) > smaller_length:
            result += word2[smaller_length:]
        return result