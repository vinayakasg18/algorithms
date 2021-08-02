""" SeamCarving Class """


class SeamCarving:
    """ SeamCarving function """

    def carve_seam(self, disruption: [[int]]) -> [int]:

        # Input matrix
        print(disruption)
        d = disruption
        en_m = []
        en_m.append(d[0])

        m = len(d)
        result = []
        final = []

        # j i = 0  1  2  3
        # 0 [  [1, 2, 0, 3],
        # 1    [1, 2, 3, 0],
        # 2    [1, 2, 3, 0],
        # 3    [1, 2, 0, 3]  ]

        for i in range(1, len(d)):
            t = []
            for j in range(m):
                if j == 0:
                    d[i][j] += min(d[i - 1][j], d[i - 1][j + 1])
                    t.append(d[i][j])
                elif j == m - 1:
                    d[i][j] += min(d[i - 1][j], d[i - 1][j - 1])
                    t.append(d[i][j])
                else:
                    d[i][j] += min(d[i - 1][j - 1], d[i - 1][j], d[i - 1][j + 1])
                    t.append(d[i][j])
            en_m.append(t)

        # for i in range(0, len(d)):
        #     min_value = min(d[i])
        #     result.append(min_value)

        # for i, j in enumerate(d):
        #     if result[i] in j:
        #         final.append(j.index(result[i]))

        # finding the lowest energy points from the resultant energy matrix

        final = [0] * m
        final[m - 1] = min(en_m[m - 1])

        for i in range(m - 2, -1, -1):
            j = final[i + 1]
            if j == 0:
                final[i] = min(en_m[i][j:j + 2]) + j
            elif j == m - 1:
                final[i] = min(en_m[i][j - 1:j + 1]) + j - 1
            else:
                ind = min(en_m[i][j - 1:j + 2]) + j - 1
                final[i] = en_m[i].index(ind)

            # final[m - 1] = en_m[m - i].index(min(en_m[m - i]))
            # m -= 1

            # final[i] = min(en_m[m - 1][i], )
            # final[m - 1] = en_m[m - 1].index(min(en_m[m - 1]))
            # m -= 1

        return final


# print(SeamCarving().carve_seam([[1, 2, 0, 3],
#                           [1, 2, 3, 0],
#                           [1, 2, 3, 0],
#                           [1, 2, 0, 3]]))

# print(SeamCarving().carve_seam([[0, 1, 2], [0, 0, 1], [1, 1, 0]]))

print(SeamCarving().carve_seam([[1, 2, 0, 3], [1, 4, 4, 4], [1, 2, 3, 4], [3, 1, 1, 3]]))

# [[1, 2, 0, 3], [1, 2, 3, 0], [1, 2, 3, 0], [1, 2, 0, 3]]
# 2	[2, 3, 3, 2]
# 3	[[0, 1, 2], [0, 0, 1], [1, 1, 0]]

# [[1, 2, 0, 3], [2, 4, 4, 4], [3, 4, 7, 8], [6, 4, 5, 10]]
# [[1, 2, 0, 3], 
# [2, 4, 4, 4], 
# [3, 4, 7, 8], 
# [6, 4, 5, 10]]
# [0, 0, 0, 1]
