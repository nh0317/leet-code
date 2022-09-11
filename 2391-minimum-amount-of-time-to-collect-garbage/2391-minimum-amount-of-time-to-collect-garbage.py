class Solution:
    
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        cnt = 0
        g = 0
        p = 0
        m = 0
                
        for i in range(len(garbage)):
            if garbage[i].count("G"):
                while g < i:
                    cnt += travel[g]
                    g += 1
                cnt += garbage[i].count("G")
                
            if garbage[i].count("P"):
                while p < i:
                    cnt += travel[p]
                    p += 1
                cnt += garbage[i].count("P")
                
            if garbage[i].count("M"):
                while m < i:
                    cnt += travel[m]
                    m += 1
                cnt += garbage[i].count("M")
                
        return cnt 
                