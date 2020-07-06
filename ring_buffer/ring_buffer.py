class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_index = None
        self.storage = [None for i in range(0, capacity)]

    def append(self, item):
        if self.current_index == None:
            self.storage[0] = item
            self.current_index = 1
        else:
            self.storage[self.current_index] = item
            self.current_index += 1
            if self.current_index == self.capacity:
                self.current_index = 0

    def get(self):
        return list(filter(lambda item: item != None, self.storage))
