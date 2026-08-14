class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        fleets = 1
        #The car closest to the target
        prev_time = (target - pairs[0][0])/ pairs[0][1]

        for i in range(1, len(pairs)):
            currCar = pairs[i] #Cars before the car closest to the target
            currTime = (target - currCar[0])/ currCar[1]
            if currTime > prev_time:
                fleets +=  1  #Slower, takes longer, so not considered as one fleet
                prev_time  = currTime
        
        return fleets