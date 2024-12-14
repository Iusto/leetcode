class Solution:
    def reverse(self, x: int) -> int:
        if x > 0 : # 양수일 때
            value = int(str(x)[::-1])
        elif x == 0 : # 0일 때
            value = 0
        else : # 음수일 때
            value = -1 * int(str(x)[:0:-1])
        if value not in range(-2 ** 31, 2 ** 31) : #overflow
            value = 0
        return value