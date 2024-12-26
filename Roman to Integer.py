class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        idx = 0
        symbol = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        special = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        while idx < len(s) :
            if idx < len(s)-1 and s[idx] + s[idx+1] in special :
                answer += symbol[special.index(s[idx] + s[idx + 1])]
                idx+=2
            else :
                answer += symbol[special.index(s[idx])]
                idx+=1
        return answer
            