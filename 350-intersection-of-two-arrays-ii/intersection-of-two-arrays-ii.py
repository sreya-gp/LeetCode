class Solution(object):
    def intersect(self, nums1, nums2):
        # Count frequencies in the first array
        counts = {}
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
            
        result = []
        # Check against the second array
        for num in nums2:
            if counts.get(num, 0) > 0:
                result.append(num)
                counts[num] -= 1
                
        return result
