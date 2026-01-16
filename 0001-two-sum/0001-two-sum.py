class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}

        for i,element in enumerate(nums):
            need = target - element

            if need in seen:
                return [seen[need],i]
            seen[element] = i
            
