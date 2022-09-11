class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        cnt = 0
        g, p, m = 0, 0, 0
        for i in range(len(garbage)):
            if "G" in garbage[i]:
                g = i
            if "P" in garbage[i]:
                p = i
            if "M" in garbage[i]:
                m = i
            cnt += len(garbage[i])
        
        for i in [g,p,m]:
            cnt += sum(travel[:i])
        return cnt 
                