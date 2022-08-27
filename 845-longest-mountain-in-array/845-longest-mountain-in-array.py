class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        maxx = 0
        g = 0
        start = 1
        end = 0
        for i in range(1, len(arr)):
            if arr[i-1] < arr[i]:
                if g == 0:
                    g = 1
                    start = i-1
                elif g == -1:
                    maxx = max(maxx, end - start + 1)
                    start = i-1
                    g *= -1
                
            elif arr[i-1] > arr[i]:
                if g == 1:
                    g *= -1
                    end = i
                elif g == -1:
                    end = i
            else:
                if g == -1:
                    maxx = max(maxx, end - start + 1)
                g = 0
                start = i
            # print(arr[i-1],arr[i],start, end, g)
                    
        # print(start, end, g)
        if end - start > 0 and g == -1:
            maxx = max(maxx, end - start + 1)
        return maxx