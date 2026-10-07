class Solution:
    def getHours(self, piles, mid):
        ans = 0

        for pile in piles:
            ans += (pile + mid - 1)// mid

        return ans
    
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        k = right

        while left <= right:
            mid = (left + right) // 2

            if self.getHours(piles, mid) > h:
                left = mid + 1
            else:
                k = mid
                right = mid - 1
        
        return k