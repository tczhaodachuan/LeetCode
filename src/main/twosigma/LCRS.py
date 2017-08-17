# LCRS representation of trees will solve the problem of multi children storage problem
# each Node still can have various numbers of children, however, the node itself only
# needs 3 pointers.
# We can therefore think of the LCRS representation as offering a time-space tradeoff between data structure storage space and access times.
#  The LCRS representation has less memory overhead than the original multiway tree,
# while the multiway tree gives constant-time lookups of each of its children.
class LCRSNode(object):
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.leftChild = None
        self.rightSiblings = None
