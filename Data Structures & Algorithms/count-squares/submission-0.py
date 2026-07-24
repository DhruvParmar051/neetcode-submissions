class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x,y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0

        for (px,py), freq in self.points.items():
            if px != x  or py == y:
                continue 
            
            side = py - y

            ans += (
                freq *
                self.points.get((x + side, y), 0) *
                self.points.get((x + side, py), 0)
            )

            ans += (
                freq *
                self.points.get((x - side, y), 0) *
                self.points.get((x - side, py), 0)
            )

        return ans