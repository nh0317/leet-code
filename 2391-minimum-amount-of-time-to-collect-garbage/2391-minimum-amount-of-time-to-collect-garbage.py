class Solution:
    def travel_home(self, garbage, travel, g_type):
        cnt = 0
        g = 0
        for i in range(len(garbage)):
            if garbage[i].count(g_type):
                while g < i:
                    cnt += travel[g]
                    g += 1
                cnt += garbage[i].count(g_type)
        return cnt
        
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        cnt = self.travel_home(garbage, travel, "G")
        cnt += self.travel_home(garbage, travel, "P")
        cnt += self.travel_home(garbage, travel, "M")
                
        return cnt 
                