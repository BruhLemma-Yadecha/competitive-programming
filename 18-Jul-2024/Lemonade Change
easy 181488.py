# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        for bill in bills:
            if bill == 10:
                if fives < 1:
                    return False
                fives -= 1
                tens += 1
            elif bill == 20:
                if not ((fives > 0 and tens > 0) or (fives > 2)):
                    return False
                if fives > 0 and tens > 0:
                    fives -= 1
                    tens -= 1
                elif fives > 2: # deprioritise giving three fives as 10s are useless outside this use case
                    fives -= 3
            else:
                fives += 1
                
        return True