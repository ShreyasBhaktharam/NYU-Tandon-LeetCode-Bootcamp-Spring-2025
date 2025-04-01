class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1) 
        dp[1] = 1  
        share_count = 0  

        for day in range(2, n + 1):
            #people can start sharing
            if day - delay >= 1:
                share_count = (share_count + dp[day - delay]) % MOD 
            #people can stop sharing
            if day - forget >= 1:
                share_count = (share_count - dp[day - forget]) % MOD 

            dp[day] = share_count 

        return sum(dp[-forget:]) % MOD