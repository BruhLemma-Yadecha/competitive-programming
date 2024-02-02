class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n + 1):
            s = ""
            if i % 3 == 0:
                s = s + "Fizz"
            if i % 5 == 0:
                s = s + "Buzz"
            if s == "":
                result.append(str(i))
            else:
                result.append(s)
        return result
        