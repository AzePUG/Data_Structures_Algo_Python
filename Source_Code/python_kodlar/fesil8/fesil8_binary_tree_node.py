# DİQQƏT! İşlək olmayan kod nümunəsi!

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
    
    
    def preorder_traversal_recursive(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder_traversal_recursive(node.left)
            self.preorder_traversal_recursive(node.right)
  
    
    def preorder_traversal_iterative(self, node):
        if node is not None:
            stack = []
            # root node-u listə daxil edirik.
            stack.append(node)
            while stack:
                node = stack.pop()
                print(node.data, end=" ")
                if node.right:
                    stack.append(node.right)
                # Ən son node.left-i append edirik çünki bizə lazımdı sol node-u pop() etsin.
                if node.left:
                    stack.append(node.left)



if __name__ == "__main__":
    tree = BinaryTree()
    arr = [8, 3, 1, 6, 4, 7, 10, 14, 13]
    for i in arr:
        tree.create_tree(i)
    
    print("PreOrder Recursive Traversal - ", end="")
    tree.preorder_traversal_recursive(tree.root)
    print("")
    print("PreOrder Iterative Traversal - ", end="")
    tree.preorder_traversal_iterative(tree.root)
    print("")
    