class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(-1, -len(digits) - 1, -1):
            if digits[i] + carry >= 10:
                digits[i] += carry - 10
                carry = 1
            else:
                digits[i] += carry
                carry = 0
        if carry == 1:
            return [1] + digits
        return digits