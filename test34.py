class Node:
    max_sum=0
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.value)
            if self.right:
                self.right.inorder()
    
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
            print("Duplication not allowed:")
    
    def max_sum_path(self):
        sm1,sm2=0,0
        if not self:
            return 0
        else:
            if self.left:
                sm1=self.left.max_sum_path()
            if self.right:
                sm2=self.right.max_sum_path()
            Node.max_sum=max(Node.max_sum,sm1+sm2+self.value)
            return max(sm1,sm2)+self.value

if __name__=="__main__":
    print("==============================")
    print("Building the tree:")
    node=Node(12)
    node.insert(18)
    node.insert(20)
    node.insert(25)
    node.insert(16)
    node.insert(28)
    node.insert(-4)
    node.insert(-24)
    node.insert(-10)
    node.insert(-100)
    print("============================")
    print("The inorder traversal of the tree is:")
    node.inorder()
    print("==================================")
    print("The maximum sum path is:")
    msum=node.max_sum_path()
    print(f"{Node.max_sum} is the maximum sum path")
    print("================================")

