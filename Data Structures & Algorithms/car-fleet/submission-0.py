class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        
        fleets = 0
        slowest = 0

        position.sort()
        
        for p, s in reversed(cars):
            time = (target - p) / s
            if time > slowest:
                fleets += 1
                slowest = time
                

        return fleets