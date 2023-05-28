class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def inorder_trav(self):
        if self:
            if self.left:
                self.left.inorder_trav()
            print(self.value)
            if self.right:
                self.right.inorder_trav()

    def insert(self,value):
        if self.value>value:
            if self.left:
                self.left.insert(value)
            else:
                self.left=Node(value)
        elif self.value<value:
            if self.right:
                self.right.insert(value)
            else:
                self.right=Node(value)
        else:
            print("Duplication not allowed")


    def inorder(self):
        root=self
        while root:
            if root.left==None:
                print(root.value)
                root=root.right
            else:
                temp=root.left
                while temp.right!=None and temp.right!=root:
                    temp=temp.right
                if temp.right==None:
                    temp.right=root
                    root=root.left
                elif temp.right==root:
                    temp.right=None
                    print(root.value)
                    root=root.right


if __name__=="__main__":
    print("==========================")
    print("Building the tree:")
    node=Node(12)
    node.insert(8)
    node.insert(10)
    node.insert(6)
    node.insert(7)
    node.insert(4)
    node.insert(18)
    node.insert(20)
    node.insert(25)
    node.insert(14)
    print("=========================")
    node.inorder()
    print("=============================")
    print("Depth first search traversal:")
    node.inorder_trav()
    print("================================")
