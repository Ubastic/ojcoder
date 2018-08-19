class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        
        # slicing array into two parts
        # Calculate left product first
        product = 1
        for i in nums:
            output.append(product)
            product *= i
            
        product = 1
        # Calculate right product
        for i in xrange(len(nums)-2,-1,-1):
            product *= nums[i + 1]
            output[i] *= product
        
        return output