class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        remaining_asteroids = []
        
        for asteroid in asteroids:
            while remaining_asteroids and asteroid < 0 and remaining_asteroids[-1] > 0:
                difference = asteroid + remaining_asteroids[-1]
                if difference < 0: #Incoming asteroid is about to hit current asteroid completely.
                    remaining_asteroids.pop()
                elif difference > 0:
                    '''
                    Nothing happens because last asteroid in stack is larger, stack remains as it is
                    Only if the difference is negative, then replace the last asteroid with current asteroid.
                    If difference greater than 0 then last asteroid in stack is greater than new asteroid, new asteroid is destroyed
                    '''
                    asteroid = 0 
                else:
                    asteroid = 0 #Asteroid is replaced 
                    remaining_asteroids.pop() 
            
            if asteroid:
                remaining_asteroids.append(asteroid)

        return remaining_asteroids