class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        road_speed = [0] * target

        for p, s in zip(position, speed):
            road_speed[p] = s

        # we're gonna compute time to reach destination
        # update the new fleet if the behind car cant reac the ahead
        # if the car behind need more time
        # it means it is in another fleet
        # otherwise, it is the same fleet
        time = 0
        slowest_time = 0
        fleet = 0
        for i in range(len(road_speed)-1, -1,-1):
            if road_speed[i] > 0:
                time = (target - i) / road_speed[i]
                if time > slowest_time:
                    fleet += 1
                    slowest_time = time

        return fleet


