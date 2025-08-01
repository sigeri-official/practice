# Leetcode problem: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Difficulty: Hard
# Runtime beat: 63.84%
# Memory beat: 82.67%
# © Sigeri

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged_list = nums1 + nums2  # Create a merged list
        merged_list.sort()  # Sort the merged list
        if len(merged_list) % 2 == 0:  # Checking pairity
            return (merged_list[int(len(merged_list) / 2)] + merged_list[int((len(merged_list)-2) / 2)]) / 2  # Selecting both central numbers
        else:
            return merged_list[int((len(merged_list)-1) / 2)]  # Selecting the exact central number

sol = Solution()
print(sol.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))  # Call the findMedianSortedArrays func
