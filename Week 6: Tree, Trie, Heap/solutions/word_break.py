class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # Fast lookup
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case

        for i in range(1, len(s) + 1):
            for word in word_set:
                if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    break  # No need to check further if s[0:i] is already breakable

        return dp[len(s)]