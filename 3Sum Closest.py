class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = None
        diff = float('inf') # 양의 무한대, float에만 가능

        for i in range(len(nums) - 2) :
            left = i+1
            right = len(nums) - 1

            while left < right :
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == target :
                    return target
                else :
                    curr_diff = abs(target - three_sum)
                    if curr_diff < diff :
                        diff = curr_diff
                        answer = three_sum
                    if three_sum < target :
                        left += 1
                    else :
                        right -= 1
        
        return answer