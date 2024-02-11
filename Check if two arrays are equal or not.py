#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        
        #code here
        same = True
        in_a = {}
        in_b = {}
        for i in A:
            if i in in_a:
                in_a[i] += 1
            else:
                in_a[i] = 1
        for i in B:
            if i in in_b:
                in_b[i] += 1
            else:
                in_b[i] = 1
        
        if len(in_a) != len(in_b):
            return False
        
        for i, freq in in_a.items():
            if (i not in in_b) or (in_b[i] != freq):
                same = False
                break
        return same
