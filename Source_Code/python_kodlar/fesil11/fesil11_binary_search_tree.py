class BSTNode:
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

class BSTree:

    def __init__(self):
        self.root = None

    def create_tree(self, val):
        # Ağacın özünü burda yaradırıq.
        if self.root is None:
            # Birinci elementi root element edirik
            self.root = BSTNode(data=val)

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
                        current.left = BSTNode(data=val)
                        break;
                # Əgər verilmiş qiymət hal-hazırkı qiymətdən böyükdürsə,
                # Onu sağ node edirik
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = BSTNode(data=val)
                else:
                    break

    def find_element(self, root, data):
        # Axtarışa root-dan başlayırıq.
        current_node = root
        while current_node is not None and data != current_node.get_data():
            # Yoxlayırıq ki, axtardığımız element hal-hazırkı node data-sından böyükdür ya yox.
            # Əgər böyükdürsə, o zaman sağ altağaca keçirik.
            if data > current_node.get_data():
                current_node = current_node.get_right_child()
            # Əgər kiçikdirsə, o zaman sol altağaca keçirik.
            else:
                current_node = current_node.get_left_child()
        return current_node

    # Rekursiv üsul
    def find_min_element(self, root):
        current_node = root
        if current_node.get_left_child() == None:
            return current_node
        else:
            return self.find_min_element(current_node.get_left_child())

    # Rekursiv olmayan üsul
    def find_min_element_non_recursive(self, root):
        current_node = root
        if current_node is None:
            return None
        while current_node.get_left_child() is not None:
            current_node = current_node.get_left_child()
        return current_node

    # Rekursiv üsul
    def find_max_element(self, root):
        current_node = root
        if current_node.get_right_child() == None:
            return current_node
        else:
            return self.find_max_element(current_node.get_right_child())

    # Rekursiv olmayan üsul
    def find_max_element_non_recursive(self, root):
        current_node = root
        if current_node is None:
            return None
        while current_node.get_right_child() is not None:
            current_node = current_node.get_right_child()
        return current_node


    def predecessor_bst(self, root):
        temp = None
        if root.get_left_child():
            temp = root.get_left_child()
            while temp.get_right_child():
                temp = temp.get_right_child()
        return temp


    def successor_bst(self, root):
        temp = None
        if root.get_right_child():
            temp = root.get_right_child()
            while temp.get_left_child():
                temp = temp.get_left_child()
        return temp


if __name__ == "__main__":
    tree = BSTree()
    arr = [8, 3, 1, 6, 4, 7, 10, 14, 13]
    for i in arr:
        tree.create_tree(i)
    print("Mövcud elementi axtarmaq -> ", tree.find_element(tree.root, 13))
    print("Mövcud olmayan elementi axtarmaq -> ", tree.find_element(tree.root, 85))

    print("Minimal elementi axtarmaq rekursiya -> ", tree.find_min_element(tree.root).data)
    print("Minimal elementi axtarmaq rekursiv olmayan -> ", tree.find_min_element_non_recursive(tree.root).data)

    print("Maximal elementi axtarmaq rekursiv -> ", tree.find_max_element(tree.root).data)

    print("Maximal elementi axtarmaq rekursiv olmayan -> ", tree.find_max_element_non_recursive(tree.root).data)

    print("Inorder Predecessor -> ", tree.predecessor_bst(tree.root).data)
    print("Inorder Successor -> ", tree.successor_bst(tree.root).data)
