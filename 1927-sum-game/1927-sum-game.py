class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        cnt = 0
        summ = 0
        for i in range (n//2):
            if num[i].isdigit():
                summ += int(num[i])
            else: 
                cnt += 1
                
        for i in range(n//2, n):
            if num[i].isdigit():
                summ -= int(num[i])
            else: 
                cnt -= 1
        
        print(cnt, summ)
        
        if cnt > 0  and summ > 0:
            return True
        
        else:
            return abs(summ) != abs(cnt) * 4.5