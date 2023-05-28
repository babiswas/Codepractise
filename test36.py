class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def trav(self):
        if self:
            if self.left:
                self.left.trav()
            print(self.value)
            if self.right:
                self.right.trav()

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
    
    def balanced(self):
        lh,rh=0,0
        if not self:
            return 0
        else:
            if self.left:
                lh=self.left.balanced()
            if self.right:
                rh=self.right.balanced()
            if abs(lh-rh)>1:
                return -1
            if lh==-1 or rh==-1:
                return -1
            return (1+max(lh,rh))
        
if __name__=="__main__":
    print("==============================")
    print("Building the tree:")
    node=Node(12)
    node.insert(6)
    node.insert(10)
    node.insert(4)
    node.insert(5)
    node.insert(1)
    node.insert(20)
    node.insert(18)
    node.insert(25)
    print("===========================")
    print("Verify if the tree is balanced:")
    num=node.balanced()
    if num==-1:
        print("The tree is not height balanced:")
    elif num!=-1:
        print("The tree is height balanced")
        print(f"The height of the tree is {num}")
    print("==============================")
    print("The inorder traversal of the tree is:")
    node.trav()
    print("===================================")
    print("Inorder by morris method:")
    node.inorder()
    print("==================================")
        

