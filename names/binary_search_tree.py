class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        # if the root value is less than the target
        # check to right of tree
        if self.value < target:
            if self.right is None:
                return False
            return self.right.contains(target)
        # if the root value is greater than the target
        # check to the left of the true
        else:
            if self.left is None:
                return False
            return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Initialize max value
        max_value = self.value

        while self.right:
            max_value = max(max_value, self.right.value)
            self = self.right

        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # fn == callback function
        fn(self.value)
        # check is left or right is not none
        # then call for_each and pass the callback to the next node. `recursive`
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
