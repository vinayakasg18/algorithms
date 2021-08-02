class MakingChange:
    def minimumCoins(self, money, coins):
        
        if money in coins:
            return 1

        if money == 0:
            return 0

        re_array = []
        
        for k in range(0, money):
            re_array.append(money + 1)
        re_array[0] = 0

        # money = 3
        #       0  1  2  -> index
        # coins[1, 2, 5] -> i

        #  0  1  2  3 -> j
        # [0, 4, 4, 4] -> placeholder values
        min_val = 90000
        for i in range(1, len(re_array)):
            for j in range(0, len(coins)):
                if i >= coins[j]:
                    min_val = self.min_change(re_array, coins, i, j, min_val)
                    re_array[i] = min_val
        
        return min_val
        

    def min_change(self, res_array, coins, re_index, c_index, min_val):
        left_i = re_index - coins[c_index]
        left = res_array[left_i] + 1
        right = res_array[re_index]

        if left < right and left < min_val:
            min_val = left
        elif left > right and right < min_val:
            min_val = right
        
        return min_val


print(MakingChange().minimumCoins(11, [1, 2, 5]))
