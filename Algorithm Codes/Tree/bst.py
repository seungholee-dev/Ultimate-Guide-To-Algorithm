from collections import deque

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.val = value
        self.right = None

    # Print tree (Inorder traversal)
    def print_tree(self):
        def print_given_level(node, level):
            if node is None:
                if level == 1:
                    print(None , end=" ")
                if level > 1:
                    print_given_level(None, level - 1)
                    print_given_level(None, level - 1)
                return

            if level == 1:
                print(node.val, end=" ")
                return

            print_given_level(node.left, level - 1)
            print_given_level(node.right, level - 1)

        max_height = self.get_height(self)

        for i in range(1, max_height + 1):
            print_given_level(root, i)
            print("/", end=" ")
        print()

    
    # Return height of the tree
    def get_height(self, node):
        if node is None:
            return 0
        right = self.get_height(node.right) + 1
        left = self.get_height(node.left) + 1
        return max(right, left)

    # Show tree
    def display(self):
        pass
    
    def delete_node(self):
        pass

    def insert_node(self, node):
        if node.val < self.val:
            if self.left is None:
                self.left = node
            else:
                self.left.insert_node(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert_node(node)
        
    
    def clear_tree(self):
        self.root = None
    

# In-order traversal
def dfs_recursive(node):
    if node is None:
        return
    dfs_recursive(node.left)
    print(node.val, end=" ")
    dfs_recursive(node.right)

# In-order traversal
def dfs_iterative(node):
    if node is None:
        return
    
    stack = deque([root])
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if node.left:
            stack.append(node.left)
            continue
        # The node.left is None
        else:
            node = stack.pop()
            print(node.val)
            stack.append(node.right)
        
        

def bfs_recursive():
    pass

def bfs_iterative(root):
    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        

if __name__ == "__main__":
    root = TreeNode(5)
    root.insert_node(TreeNode(3))
    root.insert_node(TreeNode(1))
    root.insert_node(TreeNode(4))
    root.insert_node(TreeNode(7))
    root.insert_node(TreeNode(6))
    root.insert_node(TreeNode(8))

    root.print_tree()

    dfs_recursive(root)
    # dfs_iterative(root)
    print()
    bfs_iterative(root)
