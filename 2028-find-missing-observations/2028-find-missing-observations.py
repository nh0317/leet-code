class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (n + m) - sum(rolls)
        
        if total > n * 6 or total < 1*n: 
            return []
        
        if total == n * 6:
            return [6] * n
        
        if total == 1 * n:
            return [1] * n
        
        minn = total // n
        
        result = [minn for _ in range(n)]
        
        summ = sum(result)
        idx = 0
        while summ <= n * 6:
            if summ == total:
                return result
            elif summ > total:
                if result[idx] <= 1:
                    idx += 1
                else: 
                    result[idx] -= 1
                    summ -= 1
            else:
                if result[idx] >= 6:
                    idx += 1
                else: 
                    result[idx] += 1
                    summ += 1
        