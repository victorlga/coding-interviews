class TreeNode:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def in_order_succ(node: TreeNode) -> TreeNode:
    
    if not node:
        return None

    if node.right:
        current = node.right

        while current.left:
            current = current.left

        return current

    previous, current = node, node.parent

    while current and current.right == previous:
        previous, current = current, current.parent

    return current