# A Great Problem
# You are given a stream of points on the X-Y plane. Design an algorithm that:

# Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
# Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

# Implement the DetectSquares class:

# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.

class DetectSquares:
    def __init__(self):
        # Only a hashmap, no list
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        # Increment count of this point
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        # Iterate over unique points and their frequencies
        for (x, y), freq in list(self.ptsCount.items()):
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue

            # freq = how many times (x, y) exists
            res += freq * self.ptsCount[(x, py)] * self.ptsCount[(px, y)]

        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)