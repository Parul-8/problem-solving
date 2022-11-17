class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        l1 = ax1 - ax2
        b1 = ay1 - ay2
        
        l2 = bx1 - bx2
        b2 = by1 - by2
        
        a1 = abs(l1) * abs(b1)
        a2 = abs(l2) * abs(b2)
        
        w = min(ax2,bx2)-max(ax1,bx1)
        h = min(ay2, by2)-max(ay1,by1)
        if w<=0 or h<=0:
            return a1 + a2
        else:
            return a1 + a2 - w*h