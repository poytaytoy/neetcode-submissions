import math 
def time_needed(piles, k): 
    
    counter = 0

    for i in piles: 
        counter += math.ceil(i / k)
    
    return counter 

class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        smallest = math.inf 
        largest = -math.inf 
        average_per_hour = len(piles) / h

        for i in piles: 
            smallest = min(smallest, i)
            largest = max(largest, i)

        smallest = 1
        largest = math.ceil(largest / average_per_hour)

        while (largest - smallest > 1):
            mid = smallest + math.floor((largest - smallest) / 2)
            time = time_needed(piles, mid)

            if (time > h): 
                smallest = mid 
            elif (time <= h):
                largest = mid 

        for i in range(smallest, largest + 1):
            if (time_needed(piles, i) <= h):
                return i



