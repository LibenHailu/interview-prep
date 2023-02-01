class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ageScorePair = sorted(zip(ages,scores))
        dp = [0] * len(ageScorePair)
        dp[-1] = ageScorePair[-1][1]
        for i in range(len(ageScorePair) -1, -1, - 1):
            for j in range(i+1,len(ageScorePair)):
                if ageScorePair[i][1] <= ageScorePair[j][1]:
                    dp[i] = max(dp[i], ageScorePair[i][1] + dp[j])
                else:
                    dp[i] = max(dp[i],ageScorePair[i][1])
        return max(dp)