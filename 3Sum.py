class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            # 중복된 수를 건너뛰기 위한 조건
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # nums[i]가 양수일 경우 합이 0이 될 수 없으므로 종료
            if nums[i] > 0:
                break
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                Sum = nums[i] + nums[left] + nums[right]
                
                if Sum > 0:
                    right -= 1
                elif Sum < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    
                    # 중복된 left와 right 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        
        return answer
