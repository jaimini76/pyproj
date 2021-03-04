class BstNode:
    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None


class BstTree:

    bst_node_count: int = 0

    def __init__(self):
        self.root = None

    def _insert(self, data, curr_node: BstNode):
        if data <= curr_node.data:
            if curr_node.left_child is None:
                new_node = BstNode(data)
                curr_node.left_child = new_node
                self.bst_node_count += 1
            else:
                self._insert(data, curr_node.left_child)
        else:
            if curr_node.right_child is None:
                new_node = BstNode(data)
                curr_node.right_child = new_node
                self.bst_node_count += 1
            else:
                self._insert(data, curr_node.right_child)

    def insert_node(self, data: int):
        if self.root is None:
            new_node = BstNode(data)
            self.root = new_node
        else:
            self._insert(data, self.root)

    def delete_node(self, data):
        pass

    def _search(self, data, curr_node: BstNode):
        if curr_node is None:
            print("no data found")
            return None
        if curr_node.data == data:
            print("node found with data {}".format(curr_node.data))
            return curr_node.data
        elif curr_node.data > data:
            self._search(data, curr_node.left_child)
        else:
            self._search(data, curr_node.right_child)

    def search_node(self, data):
        if self.root.data == data:
            print("root node found.")
        else:
            self._search(data, self.root)

    def _find_minimum(self, curr_node: BstNode):
        if curr_node.left_child is None:
            print("Minimum is {}".format(curr_node.data))
            return curr_node.data
        else:
            self._find_minimum(curr_node.left_child)

    def find_minimum(self):
        if self.root is None:
            print("Binary tree is empty")
        elif self.root.left_child is None:
            print("Minimum is {}".format(self.root.data))
            return self.root.data
        else:
            self._find_minimum(self.root.left_child)

    def _find_maximum(self, curr_node: BstNode):
        if curr_node.right_child is None:
            print("Maximum is {}".format(curr_node.data))
            return curr_node.data
        else:
            self._find_maximum(curr_node.right_child)

    def find_maximum(self):
        if self.root is None:
            print("Binary tree is empty")
        elif self.root.right_child is None:
            print("Maximum is {}".format(self.root.data))
            return self.root.data
        else:
            self._find_maximum(self.root.right_child)

    def _find_height(self, curr_node: BstNode):
        if curr_node is None:
            return -1
        else:
            return max(self._find_height(curr_node.left_child), self._find_height(curr_node.right_child)) + 1

    def find_height(self):
        if self.root is None:
            print("Binary tree is empty")
        else:
            tree_height = self._find_height(self.root)
            print("Tree height is : {}".format(tree_height))

    def _level_order_traversal(self, curr_node: BstNode):
        queue = []
        if self.root is None:
            print("Binary tree is empty")
        else:
            queue.append(self.root)
            while len(queue) > 0:
                curr_node = queue.pop(0)
                print("'{}'->".format(curr_node.data), sep=' ', end='')
                if curr_node.left_child is not None:
                    queue.append(curr_node.left_child)
                if curr_node.right_child is not None:
                    queue.append(curr_node.right_child)

    def level_order_traversal(self):
        if self.root is None:
            print("Binary tree is empty")
        else:
            print("\nLevel order traversal:")
            self._level_order_traversal(self.root)

    def _pre_order_traversal(self, curr_node: BstNode):
        if curr_node is None:
            return
        else:
            print("'{}'->".format(curr_node.data), end='', sep=' ')
            self._pre_order_traversal(curr_node.left_child)
            self._pre_order_traversal(curr_node.right_child)

    def pre_order_traversal(self):
        if self.root is None:
            print("Binary tree is empty")
        else:
            print("\nPre order traversal:")
            self._pre_order_traversal(self.root)

    def _in_order_traversal(self, curr_node: BstNode):
        if curr_node is None:
            return
        else:
            self._in_order_traversal(curr_node.left_child)
            print("'{}'->".format(curr_node.data), end='', sep=' ')
            self._in_order_traversal(curr_node.right_child)

    def in_order_traversal(self):
        if self.root is None:
            print("Binary tree is empty")
        else:
            print("\nIn order traversal:")
            self._in_order_traversal(self.root)

    def _post_order_traversal(self, curr_node: BstNode):
        if curr_node is None:
            return
        else:
            self._post_order_traversal(curr_node.left_child)
            self._post_order_traversal(curr_node.right_child)
            print("'{}'->".format(curr_node.data), end='', sep=' ')

    def post_order_traversal(self):
        if self.root is None:
            print("Binary tree is empty")
        else:
            print("\nPost order traversal:")
            self._post_order_traversal(self.root)


bst_tree = BstTree()
bst_tree.insert_node(15)
bst_tree.insert_node(10)
bst_tree.insert_node(20)
bst_tree.insert_node(25)
bst_tree.insert_node(8)
bst_tree.insert_node(12)
bst_tree.insert_node(11)
bst_tree.insert_node(6)
bst_tree.insert_node(36)
bst_tree.search_node(11)
bst_tree.search_node(36)
# bst_tree.find_minimum()
# bst_tree.find_maximum()
# bst_tree.find_height()
bst_tree.level_order_traversal()
bst_tree.pre_order_traversal()
bst_tree.in_order_traversal()
bst_tree.post_order_traversal()
