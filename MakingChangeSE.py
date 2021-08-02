class MakingChange:
    def minimumCoins(self, money, coins):

        # Return 1 if money(coin) is found in the array
        if money in coins:
            return 1

        if money < 1:
            return 0

        return self.min_change(coins, money, [0] * (money + 1))
    
    def min_change(self, coins, rem, re_array):
        if rem < 0:
            return -1

        if rem == 0:
            return 0

        if re_array[rem] != 0:
            return re_array[rem]

        max_value = 90000
        min_value = max_value
        for coin in coins:
            cr = self.min_change(coins, rem - coin, re_array)

            if (cr >= 0 and cr < min_value):
                min_value = 1 + cr

        re_array[rem] = -1 if (min_value == max_value) else min_value

        return re_array[rem]

# print(MakingChange().minimumCoins(11, [1, 2, 5]))
