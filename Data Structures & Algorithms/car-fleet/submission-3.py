class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the connection of position and speed
        sort_cars = sorted(zip(position, speed), reverse=True)
        fleets, fleed_time = 0,0
        for pos, spd in sort_cars:
            time_needed = (target - pos) / spd
            if time_needed > fleed_time:
                fleets += 1
                fleed_time = time_needed
        return fleets
