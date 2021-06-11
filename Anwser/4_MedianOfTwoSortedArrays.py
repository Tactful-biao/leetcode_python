from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = sorted(nums1 + nums2)
        arrayLen = len(res)
        if arrayLen % 2 == 1:
            return res[arrayLen//2]
        else:
            return (res[arrayLen//2-1] + res[arrayLen//2])/2

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        res = sorted(nums1 + nums2)
        arrayLen = len(res)
        mid = arrayLen // 2
        return (res[mid] + res[~mid])/2

nums1 = [1, 3]
nums2 = [2, 4]

solution = Solution()
result = solution.findMedianSortedArrays2(nums1, nums2)
print(result)