class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(img)
        m = len(img[0])
        result = copy.deepcopy(img)
        for i in range(n):
            for j in range(m):
                coords = []
                # check for existence
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if 0 <= k < n and 0 <= l < m:
                            coords.append(img[k][l])
                result[i][j] = sum(coords) // len(coords)
        return result