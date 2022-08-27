class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        dp1 = [0 for _ in range(len(arr))]
        dp2 = [0 for _ in range(len(arr))]
        
        
        for i in range(1,len(arr)):
            if arr[i-1] < arr[i] :
                dp1[i] = dp1[i-1] + 1
        
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > arr[i+1] :
                dp2[i] = dp2[i+1] + 1
        
        maxx = 0
        for i in range(len(arr)):
            if dp1[i] > 0 and dp2[i] > 0:
                maxx = max(dp1[i]+dp2[i]+1, maxx)
        
        return maxx