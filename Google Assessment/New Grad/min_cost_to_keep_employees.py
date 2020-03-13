# # fixed fee employment agency
# # fixed fee severance
# # monthly salary - monthly
#  # following values hiring cost
#  # salary of the employee
#  # severance fee
#  # number of months n
#  # integer array contains min employees required by the company for each month for n number of months
#  # calc and print min cost to company which is required to keep min emp each month for n months
#  # integer array has min emp reqd per month
#  # base cost will be sal-(assume monthly including benefits)
#  # when it decreases add sev_fee per resource termed
#  # when it increases add hire_fee
# from typing import List
#
#
# def minCost( hire_fee: int, sal_emp: int, sev_fee: int, n: int, nums: List[int]) -> int:
#     output_int = 0
#     for idx in range(n):
#         if idx == 0: # first month only hiring happened
#             output_int += (nums[idx] * sal_emp) + (nums[idx] * hire_fee)
#         elif nums[idx] > nums[idx - 1]: # any following month, increase in emp count
#             output_int += (nums[idx] * sal_emp) + ((nums[idx] - nums[idx - 1]) * hire_fee)
#         elif nums[idx] < nums[idx - 1]: #any](https://leetcode.com/problems/average-salary-departments-vs-company) following month, decrease in emp count
#             output_int += (nums[idx] * sal_emp) + ((nums[idx - 1] - nums[idx]) * sev_fee)
#         else:#any month following , no chnage in headcount
#             output_int += nums[idx] * sal_emp
#
#     return output_int
#
#
# print(minCost(2, 100, 10, 12, [3, 4, 5, 3, 2, 4, 5, 2, 4, 5, 3, 2]))


def solver(hire_fee,salary,fire_fee,nums):
  # The basic idea of this solution is based on the following logic:
  #
  # Firing an employee and then hiring them back in the future costs:
  #  fire_fee + hire_fee
  # Keeping an employee for n months costs:
  #  salary * n
  # So if n, the number of months before the employee is needed again to
  # meet our minimum requirements, is less than:
  #  n_threshold = (fire_fee + hire_fee) / salary
  # Then it's cheaper not to fire them. If n is greater than this, then it's
  # cheapter to fire them than to keep paying their salary and then hire
  # them back again later.
  #
  # So, what we're going to do is every time the minimum requirement drops
  # below the employee level that we had the previous month, then we look
  # into the future `n_threshold` days and look for the maximum minimum
  # number of employees in this window. Based on that information, we can
  # determine whether or not to fire employees and if so how many.
  n_threshold = math.ceil(float(fire_fee + hire_fee) / float(salary))

  prev = 0 # Number of employees in the previous month
  total_cost = 0 # Running total of cost to company
  i = 0
  while i < len(nums):
    req = nums[i]
    if req > prev:
      # This month's minimum is higher than the number of employees we had last
      # month, so hire up to the minimum
      total_cost = total_cost + (req - prev) * hire_fee + req * salary
      prev = req
      i = i + 1
    elif req == prev:
      # No change
      total_cost = total_cost + req * salary
      i = i + 1
    else:
      # Minimum required went down. In this case, we may want to fire some
      # employees depending on how long it is until we need to hire them again.
      max_req_in_window = 0
      max_req_index = 0
      for j in range(i, min(i + int(n_threshold), len(nums))):
        if nums[j] > max_req_in_window:
          max_req_in_window = nums[j]
          max_req_index = j

      if max_req_in_window >= prev:
        # There's a minimum requirement of employees within n_threshold that's
        # greater than or equal to what we had last month, so it's going to be
        # cheaper to just keep all of our employees on until that month, and
        # then hire up to the minimum for that month. In this case we can just
        # skip ahead to that month because all the months from here to there
        # will maintain last month's employee count.
        total_cost = total_cost + prev * salary * (max_req_index - i)
      else:
        # The maximum minimum employee requirement in the window is less than
        # what we had last month, so it's cheaper to fire employees down to this
        # number.
        total_cost = total_cost + (prev - max_req_in_window) * fire_fee + \
            max_req_in_window * salary * (max_req_index - i)
        prev = max_req_in_window

      i = max_req_index

  return total_cost

