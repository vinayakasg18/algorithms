""" Class to find out the minimum number of coins required to match the input money """
class MakingChange:
    def minimumCoins(self, money, coins):
        """ Function to find the minmum change required """

        if money in coins:
            return 1

        re_array = [float('inf')] * (money + 1)
        re_array[0] = 0

        for coin in coins:
            for i in range(coin, len(re_array)):
                re_array[i] = min(re_array[i], re_array[i - coin] + 1)
        return re_array[money] if re_array[money] != float('inf') else -1

print(MakingChange().minimumCoins(3, [1, 2, 5]))