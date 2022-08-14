class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        maxx = max(0, arr[0])
        
        if max(arr) <= 0: return max(arr)
        
        continuous = [ 0 for _ in range(len(arr))]
        skip = [ 0 for _ in range(len(arr))]
        
        continuous[0] = arr[0]
        for i in range(1,len(arr)):
            continuous[i] = max(continuous[i-1]+ arr[i], arr[i])
            skip[i] = max(continuous[i-1], skip[i-1] + arr[i])
            maxx = max(continuous[i], skip[i], maxx)
        
        return maxx