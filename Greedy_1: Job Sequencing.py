# -*- coding: utf-8 -*-
"""Greedy 1- Job Sequencing.ipynb

You are given a set of N jobs where each job comes with a deadline and profit. The profit can only be earned upon completing the job within its deadline. Find the number of jobs done and the maximum profit that can be obtained. Each job takes a single unit of time and only one job can be performed at a time.

Example 1:

Input: N = 4, Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}

Output: 2 60

Explanation: The 3rd job with a deadline 1 is performed during the first unit of time .The 1st job is performed during the second unit of time as its deadline is 4.
Profit = 40 + 20 = 60

Example 2:

Input: N = 5, Jobs = {(1,2,100),(2,1,19),(3,2,27),(4,1,25),(5,1,15)}

Output: 2 127

Explanation: The  first and third job both having a deadline 2 give the highest profit.
Profit = 100 + 27 = 127

Follow the given steps to solve the problem:  
Iterate on jobs in decreasing order of profit.For each job , do the following :
Sort all jobs in decreasing order of profit.

1.   Find a time slot i, such that slot is empty and i < deadline and i is greatest.
2.   Put the job in this slot and mark this slot filled.
If no such i exists, then ignore the job.
"""

import pandas as pd
import numpy as np

class Solution:

  def JobScheduling(self, jobs, deadline):
    jobs = np.array(list(jobs))
    n = len(jobs)
   # print(jobs)
    jobs_sorted = jobs[jobs[:, 2].argsort()[::-1]]
   # print(jobs_sorted)
    jobs_done = [0]*n
  #  print(jobs_done)
    profit = 0
    max_jobs = 0
    for i in range(n):
      current_deadline = jobs_sorted[i][1]
      current_profit = jobs_sorted[i][2]
     # print(deadline)
      if 0 in jobs_done[:deadline]:
        profit = profit + current_profit
       # print(profit)
        max_jobs = max_jobs + 1
        deadline = deadline -1
        if deadline == 0:
          break
   # print(profit)
  #  print(max_jobs)
    return max_jobs, profit

s = Solution()
max_jobs, profit = s.JobScheduling({(1,2,100),(2,1,19),(3,2,27),(4,1,25),(5,1,15)}, 2)
print(str(max_jobs), ",",str(profit))

