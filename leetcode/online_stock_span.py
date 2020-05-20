class StockSpanner:

    def __init__(self):
        self.stack = []
        self.acc = 0

    def next(self, price: int) -> int:
        goback = 1
        is_big = self.stack and price >= self.stack[0]
        if not is_big:
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i] > price:
                    break
                goback += 1
        if is_big and self.stack:
            self.acc += len(self.stack)
            self.stack = []
            goback = self.acc + 1
        self.stack.append(price)
        return goback 

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
