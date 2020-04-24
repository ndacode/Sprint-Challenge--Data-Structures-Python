class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Add value to tree

    def insert(self, value):
        current = self
        node = BinarySearchTree(value)

            if value > current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = BinarySearchTree(value)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = BinarySearchTree(value)
                    break


# See if tree contains value

    def contains(self, target):
       current = self
       while True:
           if target == current.value:
               return True
           if target < current.value:
               if current.left:
                   current = current.left
               else:
                    return False
           else:
               if current.right:
                   current = current.right
               else:
                   return False


# Get max value

    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.value


# Callback for each node value

    def recall(self, cb):
        cb(self.value)
        if self.left:
            self.left.recall(cb)
        if self.right:
            self.right.recall(cb)