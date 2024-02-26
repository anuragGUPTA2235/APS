class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
              """ brute force n3
              uni  = set()
              nums.sort()
              for i in range(len(nums)):
                  for j in range(i+1,len(nums)):
                      for k in range(j+1,len(nums)):
                          
                          if nums[i] + nums[j] + nums[k] == 0:
                              uni.add((nums[i],nums[j],nums[k]))
              return list(uni)
              """ 
              print(nums)
              nums.sort()
              print(nums)
              uni = set()
              for i in range(len(nums)-2):
                  target = -nums[i]
                  left = i+1
                  right = len(nums)-1
                  while left < right:
                   if nums[left] + nums[right] > target:
                      right -= 1
                   elif nums[left] + nums[right]  < target:
                      left += 1
                   else:
                      uni.add((nums[i],nums[left],nums[right]))
                      left += 1
                      right -= 1

              return list(uni)           
              

        
        