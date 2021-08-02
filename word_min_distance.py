word1 = 'abcvg'
word2 = 'def'

m = len(word1)
n = len(word2)
min_dist = 0

myArray = [[0 for i in range(m + 1)] for j in range(n + 1)]

for k in range(1, n + 1):
    myArray[k][0] = k

for l in range(1, m + 1):
    myArray[0][l] = l

for i in range(1, n + 1):
    for j in range(1, m + 1):

        if word1[j - 1] == word2[i - 1]:
            dist = 0
        else:
            dist = 1
        myArray[i][j] = min(myArray[i - 1][j - 1] + dist, myArray[i][j - 1] + 1, myArray[i - 1][j] + 1)
        min_dist = myArray[i][j]

print(min_dist)