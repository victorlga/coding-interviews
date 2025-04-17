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


class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []


class Graph:
    def __init__(self, adjacency: list[list[bool]]):
        '''
        adjacency: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        self.nodes = [GraphNode(i) for i in range(1, len(adjacency) + 1)]
        for node1, row in zip(self.nodes, adjacency):
            for node2, adjacent in zip(self.nodes, row):
                if adjacent and node1 is not node2:
                    node1.adjacent.append(node2)


# Implement the functions below

def pre_order_recursive(root: TreeNode) -> None:
    if not root:
        return None
    
    print(root.value)

    pre_order_recursive(root.left)
    pre_order_recursive(root.right)


def pre_order_iterative(root: TreeNode) -> None:
    
    stack = [ root ]

    while stack:

        curr = stack.pop()
        if not curr:
            continue

        print(curr.value)
        stack.append(curr.right)
        stack.append(curr.left)


def in_order_recursive(root: TreeNode) -> None:
    if not root:
        return None

    in_order_recursive(root.left)
    print(root.value)
    in_order_recursive(root.right)


def post_order_recursive(root: TreeNode) -> None:
    if not root:
        return None

    post_order_recursive(root.left)
    post_order_recursive(root.right)
    print(root.value)


def breadth_first(root: TreeNode) -> None:

    queue = [ root ]

    while queue:
        curr = queue[0]
        del queue[0]

        if not curr:
            continue

        queue.append(curr.left)
        queue.append(curr.right)

        print(curr.value)


def graph_depth_first_recursive(node: GraphNode, visited=None) -> None:
    if visited is None:
        visited = set()
        visited.add(node)

    print(node.value)

    for a in node.adjacent:
        if a in visited:
            continue

        visited.add(a)
        graph_depth_first_recursive(a, visited)


def graph_depth_first_iterative(node: GraphNode) -> None:
    visited = set()
    visited.add(node)
    stack = [ node ]

    while stack:

        top = stack.pop()
        print(top.value)

        for a in top.adjacent:
            if a in visited:
                continue

            stack.append(a)
            visited.add(a)


def graph_breadth_first(node: GraphNode) -> None:

    visited = set()
    visited.add(node)
    queue = [ node ]

    while queue:
        first = queue[0]
        del queue[0]

        print(first.value)

        for a in first.adjacent:
            if a in visited:
                continue

            queue.append(a)
            visited.add(a)


