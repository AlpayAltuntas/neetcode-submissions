class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort = sorted(zip(position, speed), reverse=True)
        fleets, fleet_time = 0,0
        for pos,spd in sort:
            time = (target-pos) / spd
            if time > fleet_time:
                fleets += 1
                fleet_time = time
        return fleets
 