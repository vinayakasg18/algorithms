""" SeamCarving Class """


class SeamCarving:
    def min_elem_index(self, f_list):
        """ Finding the index of the min element from the final[[]] list"""

        ind = f_list.index(min(f_list))
        return ind

    def carve_seam(self, disruption: [[int]]) -> [int]:
        """ SeamCarving Function """

        d = disruption
        m = len(d)
        en_m = [d[0]]

        # 0 [  [1, 2, 0, 3],
        # 1    [1, 2, 3, 0],
        # 2    [1, 2, 3, 0],
        # 3    [1, 2, 0, 3]  ]

        for i in range(1, m):
            t = []
            for j in range(m):
                if j == 0:
                    t.append(d[i][j] + min(en_m[i - 1][j], en_m[i - 1][j + 1]))
                elif j == m - 1:
                    t.append(d[i][j] + min(en_m[i - 1][j], en_m[i - 1][j - 1]))
                else:
                    t.append(d[i][j] + min(en_m[i - 1][j - 1], en_m[i - 1][j], en_m[i - 1][j + 1]))
            en_m.append(t)

        # for i in range(0, len(d)):
        #     min_value = min(d[i])
        #     result.append(min_value)

        # for i, j in enumerate(d):
        #     if result[i] in j:
        #         final.append(j.index(result[i]))

        # finding the lowest energy points from the resultant energy matrix
        final = [0] * m
        final[m - 1] = self.min_elem_index(en_m[m - 1])
        for i in range(m - 2, -1, -1):
            j = final[i + 1]
            if j == 0:
                final[i] = self.min_elem_index(en_m[i][j:j + 2]) + j
            elif j == m - 1:
                final[i] = self.min_elem_index(en_m[i][j - 1:j + 1]) + j - 1
            else:
                final[i] = self.min_elem_index(en_m[i][j - 1:j + 2]) + j - 1
        return final


print(SeamCarving().carve_seam([[3, 2, 2, 3, 1, 2], [2, 1, 3, 2, 3, 1], [3, 4, 3, 1, 3, 1], [3, 2, 1, 2, 4, 3], [1, 3, 3, 2, 4, 3]]))
