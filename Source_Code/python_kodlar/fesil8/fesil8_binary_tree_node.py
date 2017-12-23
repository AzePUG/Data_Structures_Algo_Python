# Kod mənbəsi: https://gist.github.com/thinkphp/1450738
# Lakin, iterativ üsullar və bəzi dəyişikliklər edildi.

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
            # Birinci root node print olunur(ziyarət olunur)
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
    
    def inorder_traversal_recursive(self, node):
        if node is not None:
            # Birinci sol altağac emal olunur(ziyarət olunur)
            self.inorder_traversal_recursive(node.left)
            print(node.data, end=" ")
            self.inorder_traversal_recursive(node.right)
    
    def inorder_traversal_iterative(self, node):
        if node is not None:
            stack = []
            while stack or node:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    print(node.data, end=" ")
                    node = node.right
    
    def postorder_traversal_recursive(self, node):
        if node is not None:
            self.postorder_traversal_recursive(node.left)
            self.postorder_traversal_recursive(node.right)
            print(node.data, end=" ")
    
    def postorder_traversal_iterative(self, root):
        solution = []
        used = set()
        stack = []

        if root != None:
            stack.append(root)
        
        while len(stack) > 0:
            node = stack.pop()
        
            if node in used:
                solution.append(node.data)
            else:
                used.add(node)
                stack.append(node)
                if node.right != None:
                    stack.append(node.right)
                if node.left != None:
                    stack.append(node.left)
        return solution

    def level_order_traversal(self, node):
        if node is not None:
            result = []
            q = Queue()
            q.put(node) # root node-u daxil edirik.

            while not q.empty():
                node = q.get() # Dequeue FIFO
                result.append(node.get_data())

                if node.left is not None:
                    q.put(node.left)

                if node.right is not None:
                    q.put(node.right)
        
        return result
        
        

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
    print("InOrder Recursive Traversal - ", end="")
    tree.inorder_traversal_recursive(tree.root)
    print("")
    print("InOrder Iterative Traversal - ", end="")
    tree.inorder_traversal_iterative(tree.root)
    print("")
    print("PostOrder Recursive Traversal - ", end="")
    tree.postorder_traversal_recursive(tree.root)
    print("")
    print("PostOrder Iterative Traversal - ", end="")
    print(tree.postorder_traversal_iterative(tree.root))
    print("LevelOrder Traversal - ", end="")
    print(tree.level_order_traversal(tree.root))