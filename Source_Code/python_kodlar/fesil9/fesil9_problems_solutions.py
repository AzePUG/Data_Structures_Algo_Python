from queue import Queue

class Node:
    def __init__(self, data):
        # root node
        self.data = data
        # Sol övlad(left child)
        self.left = None
        # Sağ övlad(right child)
        self.right = None

    def get_data(self):
        return self.data

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right


class BinaryTree:
    
    def __init__(self):
        self.root = None
        self.max_data = 0.0
    
    def create_tree(self, val):
        # Ağacın özünü burda yaradırıq.
        if self.root is None:
            # Birinci elementi root element edirik
            self.root = Node(data=val)
        
        else:
            # Root-u hazırkı node edirik
            current = self.root

            while True:
                # Əgər verilmiş qiymət hal-hazırkı qiymətdən kiçikdirsə,
                # Onu sol node edirik  
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(data=val)
                        break;
                # Əgər verilmiş qiymət hal-hazırkı qiymətdən böyükdürsə,
                # Onu sağ node edirik  
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(data=val)
                else:
                    break
    
    def find_max_recursive(self, node):
        if not node:
            return self.max_data

        if node.get_data() > self.max_data:
            self.max_data = node.get_data()
        
        self.find_max_recursive(node.left)
        self.find_max_recursive(node.right)

        return self.max_data

    def find_max_level_order_traversal(self, node):
        if node is not None:
            q = Queue()
            q.put(node) # root node-u daxil edirik.

            while not q.empty():
                node = q.get() # Dequeue FIFO
                # növbədən çıxartdıqdan sonra müqayisə edirik.
                if node.get_data() > self.max_data:
                    self.max_data = node.get_data()

                if node.left is not None:
                    q.put(node.left)

                if node.right is not None:
                    q.put(node.right)
        
        return self.max_data

    def find_data_recursive(self, node, data):
        if node is None:
            return 0

        if node.get_data() == data:
            return 1
        else:
            temp = self.find_data_recursive(node.left, data)
            if temp == 1:
                return temp
            else:
                self.find_data_recursive(node.right, data)
                

        

if __name__ == "__main__":
    tree = BinaryTree()
    arr = [8, 3, 1, 6, 4, 7, 10, 14, 13]
    for i in arr:
        tree.create_tree(i)
    print("find_max_recursive() -> ", end='')
    print(tree.find_max_recursive(tree.root))
    print("find_max_level_order_traversal() -> ", end='')
    print(tree.find_max_level_order_traversal(tree.root))
    print("find_data_recursive() -> ", end='')
    print(tree.find_data_recursive(tree.root, 14))