# The actual problem is similar to this Leetcode problem:
# 1335. Minimum Difficulty of a Job Schedule
 

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        self.dp = [[-1]*(n+1) for _ in range(d+2)]
        return self.solution(jobDifficulty, d, idx=0)
    
    def solution(self, jobDifficulty, d, idx):
        if d == 1:
            # That means rest of the tasks have to be finished on that day
            return max(jobDifficulty[idx:])
        
        # Return if already calculated
        if self.dp[d][idx] != -1:
            return self.dp[d][idx]
        
        result = float('inf')
        max_diff = 0
        for i in range(idx, len(jobDifficulty)-d+1):
            # Find the maxDifficulty when cut at idx
            max_diff = max(jobDifficulty[i], max_diff)
            result = min(result, max_diff + self.solution(jobDifficulty, d-1, i+1))
            
        self.dp[d][idx] = result
        return result