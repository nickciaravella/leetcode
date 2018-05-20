# https://leetcode.com/problems/product-of-array-except-self/description/
# Medium

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product_except_self = []

        product = 1        
        for i in range(len(nums)):
            # product of everything to the left, without multiplying by nums[i]
            product_except_self.append(product) 
            product *= nums[i]

        product = 1
        for i in range(len(nums)-1, -1, -1):
            # product of everything to the right, without multiplying by nums[i]
            product_except_self[i] *= product
            product *= nums[i]

        return product_except_self

s = Solution()
print(s.productExceptSelf([1,2,3,4]))