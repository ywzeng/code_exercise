class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        # Check whether the the adjacent line segment (coordinates[i:i+1] and coordinates[i-1:i]) have the same slop.
        # k = (y2-y1) / (x2-x1)
        # If k1 == k2, we get (y1-y0) / (x1-x0) == (y2-y1) / (x2-x1).
        # Because two adjacent coordinates may have the same x-coordinate, we can transfer the divide-equation to multiple-equation.
        # Get (y1-y0)(x2-x1) == (y2-y1)(x1-x0).
        for i in range(2, len(coordinates)):
            if (coordinates[i][1]-coordinates[i-1][1])*(coordinates[i-1][0]-coordinates[i-2][0]) != (coordinates[i-1][1]-coordinates[i-2][1])*(coordinates[i][0]-coordinates[i-1][0]):
                print(i)
                return False
        return True
