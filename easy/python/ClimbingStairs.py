'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution(object):
    lookup={}
    def climbingStairs(self,n):
        if n<=1:
            return 1
        if n not in Solution.lookup:
            Solution.lookup[n] = self.climbingStairs(n-1) + self.climbingStairs(n-2)
        return Solution.lookup[n]

s = Solution()
assert 1 == s.climbingStairs(1)
assert 453973694165307953197296969697410619233826 == s.climbingStairs(200)
