# def closestPrice(pizzas, toppings, x):
#     import bisect
#     closest = float('inf')
#     new_toppings = [0]
# # Generate combinations for 0, 1, and 2 toppings
#     for i in range(len(toppings)):
#         new_toppings.append(toppings[i])
#         for j in range(i+1, len(toppings)):
#             new_toppings.append(toppings[i] + toppings[j])
#     new_toppings.sort()
#     for pizza in pizzas:
#         idx = bisect.bisect_left(new_toppings, x - pizza)
#         for j in range(idx-1, idx+2):
#             if 0 <= j < len(new_toppings):
#                 diff = abs(pizza + new_toppings[j] - x)
#                 if diff == abs(closest - x):
#                     closest = min(closest, pizza + new_toppings[j]) # When two are equal, take the lowest one according to example 3
#                 elif diff < abs(closest - x):
#                     closest = pizza + new_toppings[j]
#     return closest
#
#
# print(closestPrice(pizzas = [800, 850, 900], toppings = [100, 150], x = 1000))
# print(closestPrice(pizzas = [850, 900], toppings = [200, 250], x = 1000))
# print(closestPrice(pizzas = [1100, 900], toppings = [200], x = 1000))
# print(closestPrice(pizzas = [800, 800, 800, 800], toppings = [100], x = 1000))


def find_piz_top(piz, top, target):
    Lp = len(piz)  # length of pizzas
    Lt = len(top)  # length of topings
    piz.sort()  # sort them so that we get cheapest pizza (to counter the fact that abs(1100 - 1000) == abs(900 - 1000))
    top.sort()  # same here
    dp = [[0] * (Lt + 1) for i in range(Lp + 1)]
    dp[0][1:] = piz  # assign the first row as given pizzas

    for i in range(1, Lp + 1):
        for j in range(1, Lt + 1):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], piz[i - 1] + top[j - 1], key=lambda x: abs(target - x))
            if dp[i][j] == target:  # if we found the exact match we can just return it.
                return target

    return dp[i][j]


print(find_piz_top([1100, 900], [200], 1000) == 900)
print(find_piz_top([850, 900], [200, 250], 1000) == 1050)
print(find_piz_top([1100, 900], [200], 1000) == 900)
print(find_piz_top([800, 800, 800, 800], [100], 1000) == 900)
