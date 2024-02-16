class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counter = {}
        for line in cpdomains:
            count, link = line.split()
            count = int(count)

            link = link.split('.')
            if len(link) == 2:
                # has only level b and c
                b = '.'.join(link)
                c = link[1]

                counter[c] = counter.get(c, 0) + count 
                counter[b] = counter.get(b, 0) + count
            else:
                # a b c
                c = link[2]
                b = '.'.join([link[1], link[2]])
                a = '.'.join(link)

                counter[a] = counter.get(a, 0) + count 
                counter[b] = counter.get(b, 0) + count
                counter[c] = counter.get(c, 0) + count
        result = []
        for key, value in counter.items():
            result.append(' '.join([str(value), key]))
        return result