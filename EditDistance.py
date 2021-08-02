""" Class to find the min edit distance """

class EditDistance:
    def editDistance(self, word1, word2):
        
        """ Function to find the min edit distance """
        m = len(word1)
        n = len(word2)
        
        #      a b c
        #    0 1 2 3
        #  d 1 1 2 3
        #  e 2 2 2 3
        #  f 3 3 3 3

        if m == 0:
            return n

        if n == 0:
            return m

        # t = [[0 for i in range(n + 1)] for j in range(m + 1)]

        t = [0] * (n + 1)

        min_dist = 0
        
        for i in range(n + 1):
            t[i] = [0] * (m + 1)

        for i in range(1, n + 1):
            t[i][0] = i

        for i in range(m + 1):
            t[0][i] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[j - 1] == word2[i - 1]:
                    dist = 0
                else:
                    dist = 1
                t[i][j] = min(t[i - 1][j - 1] + dist, t[i - 1][j] + 1, t[i][j - 1] + 1)
                min_dist = t[i][j]
        return min_dist

print(EditDistance().editDistance('deffgf', 'deff'))
