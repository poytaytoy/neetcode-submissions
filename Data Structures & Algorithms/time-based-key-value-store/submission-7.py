class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (key not in self.storage): 
            self.storage[key] = []

        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if (key not in self.storage):
            return ""

        storage = self.storage[key]

        left = 0 
        right = len(storage) - 1

        time_stamp = lambda x: storage[x][0]

        while (right - left > 1): 
            mid = (left + right) // 2 
            if (time_stamp(mid) > timestamp):
                right = mid 
            else: 
                left = mid 
        
        location = -1
        for i in range(left, right + 1): 
            if (time_stamp(i) <= timestamp):
                location = i 

        if (location == -1):
            return ""
        
        return storage[location][1]
            