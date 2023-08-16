"""
CASHING BRUTE FORCE
put +/- beetwen nums , how many ways to get target?
"""
# f(i,sum) = beeing at position i having sum
class Solution:
    # brute-force with cashing
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        cash = {} #(idx,sum) -> no. of ways

        def dfs(i,total): #using all el in nums
            if i == len(nums): #end of path
                if total == target: return 1
                else: return 0
            if (i,total) in cash: return cash[(i,total)]

            set_to_minus = dfs(i+1,total-nums[i])
            set_to_plus = dfs(i+1,total+nums[i])

            cash[(i,total)] = set_to_minus + set_to_plus

            return set_to_minus + set_to_plus

        return dfs(0,0)