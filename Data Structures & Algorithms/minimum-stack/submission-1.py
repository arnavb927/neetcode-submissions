class MinStack:

    def __init__(self):
        self.min_n = None
        self.nums = []

    def push(self, val: int) -> None:
        if not self.nums and not self.min_n:
            self.min_n = val
        self.nums.append(val)
        self.min_n = min(self.min_n, val)


    def pop(self) -> None:
        if len(self.nums) <= 0:
            return
        elif self.nums[-1] != self.min_n:
            self.nums.pop()
        else:
            self.nums.pop()
            if not self.nums:
                self.min_n = None
                return
            self.min_n = min(self.nums)

        if not self.nums:
            self.min_n = None



    def top(self) -> int:
        if len(self.nums) > 0:
            return self.nums[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.min_n

        
