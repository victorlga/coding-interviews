# Do not modify the classes below
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, representation: str):
        '''
        representation: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        if not representation:
            self.root = None
            return
        nodes = []
        for i, value in enumerate(representation):
            node = None
            if value is not None:
                node = TreeNode(value)
                if i > 0:
                    if i % 2 == 1:
                        parent = nodes[(i - 1) // 2]
                        parent.left = node
                    else:
                        parent = nodes[(i - 2) // 2]
                        parent.right = node
            nodes.append(node)
        self.root = nodes[0]


class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self, values):
        self.root = None
        if not values:
            return
        prev = None
        for value in values:
            node = LinkedListNode(value)
            if prev:
                prev.next = node
            if self.root is None:
                self.root = node
            prev = node


# Implement the functions below

def list_sum(l: list[int]) -> int:
    if len(l) <= 0:
        return 0
    return l[0] + list_sum(l[1:])


def digit_sum(n: int) -> int:
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


def tree_sum(root: TreeNode) -> int:
    if not root:
        return 0
    return tree_sum(root.left) + root.value + tree_sum(root.right)


def tree_max(root: TreeNode) -> int:
    if not root:
        return float('-inf')
    return max(tree_max(root.left), root.value, tree_max(root.right))


def k_combinations(l: list[int], k: int) -> list[list[int]]:
    if k == 0:
        return [[]]
    if len(l) < k:
        return []

    res = []
    for i in range(len(l)):
        for tail in k_combinations(l[i+1:], k-1):
            res.append([l[i]] + tail)
    return res


def all_strictly_increasing_sequences(k: int, n: int, **kwargs) -> list[list[int]]:
    start = kwargs.get('start', 1)

    if k == 0:
        return [[]]
    if start > n:
        return []

    res = []
    for i in range(start, n + 1):
        for seq in all_strictly_increasing_sequences(k - 1, n, start=i + 1):
            res.append([i] + seq)
    return res


def create_pattern(n: int) -> list[int]:
    if n <= 0:
        return [n]
    rest = create_pattern(n - 5)
    return [n] + rest + [n]


def find_middle(head: LinkedListNode) -> LinkedListNode:
    # Don't change this function
    return find_middle_rec(head)[1]


def find_middle_rec(head: LinkedListNode, n: int=0) -> tuple[int, LinkedListNode]:
    # Hint: n will be used to count nodes from left to right and
    # the number returned by the function will be used to count the nodes from right to left
    # TODO: Implement this function

    if not head:
        return n, None

    total, node = find_middle_rec(head.next, n+1)

    if n == total // 2:
        return total, head
    elif not node:
        return total, None
    return total, node
    
