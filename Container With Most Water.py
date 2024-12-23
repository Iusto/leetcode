class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0
        
        while left < right:
            # 현재 용량 계산
            currentArea = min(height[left], height[right]) * (right - left)
            # 최대값 갱신
            maxArea = max(maxArea, currentArea)
            print(left, right)
            # 더 작은 값을 가진 포인터를 이동
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return maxArea
