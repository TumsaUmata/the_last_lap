import math


def solver(hire_fee, salary, fire_fee, nums):
    n_threshold = math.ceil(float(fire_fee + hire_fee) / float(salary))

    prev = 0
    total_cost = 0
    i = 0
    while i < len(nums):
        req = nums[i]
        if req > prev:
            total_cost = total_cost + (req - prev) * hire_fee + req * salary
            prev = req
            i = i + 1
        elif req == prev:
            total_cost = total_cost + req * salary
            i = i + 1
        else:
            max_req_in_window = 0
            max_req_index = 0
            for j in range(i, min(i + int(n_threshold), len(nums))):
                if nums[j] > max_req_in_window:
                    max_req_in_window = nums[j]
                    max_req_index = j
            if max_req_in_window >= prev:
                total_cost = total_cost + prev * salary * (max_req_index - i)
            else:
                total_cost = total_cost + (prev - max_req_in_window) * fire_fee + \
                             max_req_in_window * salary * (max_req_index - i)
                prev = max_req_in_window

            i = max_req_index

    return total_cost
