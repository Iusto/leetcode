class Solution:
    def myAtoi(self, s: str) -> int:
        # 공백 제거
        s = s.lstrip()  # 앞부분 공백만 제거
        
        if not s:
            return 0
        
        sign = 1  # 기본적으로 양수
        result = 0
        
        # 부호 처리
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]  # 부호 문자 처리 후, 그 뒤의 부분으로 문자열 잘라냄
        
        # 숫자 부분 처리
        for i in s:
            if i.isdigit():
                result = result * 10 + int(i)
            else:
                break
        
        result *= sign
        
        # 결과값을 32비트 정수 범위에 맞추기
        int_min = -2**31
        int_max = 2**31 - 1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max
        
        return result
