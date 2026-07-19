import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1) 
        n2 = len(nums2)
        n = n1 + n2

        if n % 2 == 0:
            pass
        else:
            pass

        arr = []
        i = j = 0

        while i <  n1 and j < n2:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        
        arr.extend(nums1[i:])
        arr.extend(nums2[j:])

        if n % 2 != 0:
            return arr[n//2]
        
        return (arr[n//2-1] + arr[n//2])/2
