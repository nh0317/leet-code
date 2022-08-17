class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (n + m) - sum(rolls)
        
        if n * 6 < total or 1 * n > total:
            return []
        
        q, r = divmod(total, n)
        return [q] * (n-r) + [q+1] * r