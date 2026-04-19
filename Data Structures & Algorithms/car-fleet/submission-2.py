class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # catch up is right behind or same position ?
        # i think right behind
        # + "at the same speed as the car AHEAD of it"

        # [0,0,0,0,0,0,0,0,0,0]
        # [0,3,0,0,3,0,0,3,2,0]

        # fleet if it reaches destination or its adjacence
        # when it becomes a fleet, the speed is synchronous

        # --> find a fleet:
        # 1. chasing phase: the ratio between pos and speed
        # 2. destination: is there any fleet

        # fleet --> count+1

        # destination phase (destination + merging)
        # position and speed
        # reaching each other --> car at low position has higher speed
        # how much is higher ? 
        # --> 9 // 3   6 // 2      
        # --> 6 // 2   9 // 2     10 // 1      3 // 1

        # chasing phase (merging)
        # the ratio or the steps[-1] <= step[-2]
        # target=12
        # position=[10,8,0,5,3]
        # speed=[2,4,1,1,3]
        # steps to reach destination 4->4 5->7 3->3
        # ratio to reach each other  4/4 == 3/3 > 5/7
        
        car_w_speed = [0] * target
        for p,s in zip(position,speed):
            car_w_speed[p] = s

        time = 0
        slowest = 0
        res = 0
        for i in range(target - 1, -1, -1):
            if car_w_speed[i] > 0:
                time = (target - i) / car_w_speed[i] # distance / speed
                if time > slowest:
                    res += 1
                    slowest = time
        return res




