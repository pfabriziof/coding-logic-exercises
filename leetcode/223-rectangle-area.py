class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # 1. Calculate the area of both rectangles
        a_area = (ax2 - ax1) * (ay2 - ay1)
        b_area = (bx2 - bx1) * (by2 - by1)

        # 2. Calculate the width and height of the overlapping rectangle
        overlap_width = max(0, min(ax2,bx2) - max(ax1,bx1)) # if difference is negative, there's no overlap
        overlap_height = max(0, min(ay2,by2) - max(ay1,by1)) # if difference is positive, there's an overlap
        overlap_area = overlap_width * overlap_height

        # 3. Substract the overlap to find the total area
        total_area = a_area + b_area - overlap_area
        return total_area

