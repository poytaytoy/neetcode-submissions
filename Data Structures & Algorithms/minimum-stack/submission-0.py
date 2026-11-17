class MinStack:

    def __init__(self):
        self.array = []
        self.min_index = []

    def push(self, val: int) -> None:
        self.array.append(val)

        if len(self.min_index) == 0 or (self.array[self.min_index[-1]] >= val):
            self.min_index.append(len(self.array) - 1)

    def pop(self) -> None:
        
        if len(self.min_index) != 0 and (len(self.array) - 1 == self.min_index[-1]):
            self.min_index.pop() 
        self.array.pop() 

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.array[self.min_index[-1]]
