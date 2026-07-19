import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []

        for num in nums1:
            arr.append(num)
        
        for num in nums2:
            arr.append(num)
        arr.sort()

        return statistics.median(arr)