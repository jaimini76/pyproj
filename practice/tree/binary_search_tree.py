class node:
    def __init__(self, value=None):
        self.value = value
        self.count = 0
        self.left_child = None
        self.right_child = None

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, curr_node):

        if value < curr_node.value:
            if curr_node.left_child == None:
                curr_node.left_child = node(value)
            else:
                self._insert(value, curr_node.left_child)
        elif value > curr_node.value:
            if curr_node.right_child == None:
                curr_node.right_child = node(value)
            else:
                self._insert(value, curr_node.right_child)
        else:
            curr_node.count += 1

    def height(self):
        if self.root == None:
            return 0
        else:
            return self._height(self.root, 0)

    def _height(self, curr_node, curr_height):
        if curr_node == None:
            return curr_height
        else:
            left_height = self._height(curr_node.left_child, curr_height+1)
            right_height = self._height(curr_node.right_child, curr_height+1)
            return max(left_height, right_height)

    def print_tree(self):
        if self.root == None:
            return
        else:
            print("Preorder:")
            self._print_tree_preorder(self.root)
            print("Inorder:")
            self._print_tree_inorder(self.root)
            print("Postorder:")
            self._print_tree_postorder(self.root)

    def _print_tree_preorder(self, curr_node):
        # Preorder Traversal (root, left, right)
        if curr_node == None:
            return
        else:
            print(f"{curr_node.value}")
            self._print_tree_preorder(curr_node.left_child)
            self._print_tree_preorder(curr_node.right_child)

    def _print_tree_inorder(self, curr_node):
        # Inorder Traversal (left, root, right)
        if curr_node == None:
            return
        else:
            self._print_tree_inorder(curr_node.left_child)
            print(f"{curr_node.value}")
            self._print_tree_inorder(curr_node.right_child)

    def _print_tree_postorder(self, curr_node):
        # Postorder Traversal (left, right, root)
        if curr_node == None:
            return
        else:
            self._print_tree_postorder(curr_node.left_child)
            self._print_tree_postorder(curr_node.right_child)
            print(f"{curr_node.value}")

def fill_tree(tree, num_elements=10, max_int=100):

    from random import randint

    for _ in range(num_elements):
        curr_element = randint(0, max_int)
        tree.insert(curr_element)

    return(tree)

if __name__  == '__main__':
    tree = binary_search_tree()
    tree = fill_tree(tree)
    tree.print_tree()
    print(f"Height of tree is : {tree.height()}")
