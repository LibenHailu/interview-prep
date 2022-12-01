class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions) + 1) 
        for i in range(len(questions) - 1, -1, -1):
            points, jump = questions[i][0], questions[i][1]
            dp[i] = max(points + dp[min(jump + i + 1, len(questions))], dp[i + 1])
        return dp[0];
        # dp = [0] * len(questions)
        # for i in range(len(questions) - 1, -1, - 1):
        #     if i + 1 +  questions[i][1] >= len(questions):
        #         dp[i] = questions[i][0]
        #     else:
        #         dp[i] = questions[i][0] + dp[i + 1 + questions[i][1]]
        # return max(dp)
#         for i,q in enumerate(questions):
#             if len(dp) >= 3:
#                 dp.append(q[0] + dp[i - 3])
#             else:
#                 dp.append(q[0])
        
#         return max(dp)