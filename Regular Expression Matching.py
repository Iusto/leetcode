class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j]는 s[:i]와 p[:j]가 일치하는지 여부
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # 빈 문자열과 빈 패턴은 일치
        dp[0][0] = True
        
        # 빈 문자열 s와 패턴 p에 대해 처리 (패턴이 '*'을 포함할 경우)
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # s와 p를 비교하면서 dp 테이블을 채운다
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        
        # 최종 결과 반환
        return dp[len(s)][len(p)]