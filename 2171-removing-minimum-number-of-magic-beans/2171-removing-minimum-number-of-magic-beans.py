class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        min_cnt = float('inf')
        beans.sort(reverse = True)
        summ = sum(beans)
        while beans:
            minn = beans[-1]
            cnt = summ - minn * len(beans)
            min_cnt = min(min_cnt, cnt)
            beans.pop()
                
        return min_cnt