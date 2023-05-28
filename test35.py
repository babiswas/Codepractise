class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    
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
        stack=list()
        root=self
        while True:
            if root:
                stack.append(root)
                root=root.left
            elif stack:
                root=stack.pop()
                print(root.value)
                root=root.right
            else:
                break
    
    def topview(self):
        queue=list()
        queue.append((self,0))
        m=dict()
        while queue:
            item=queue.pop(0)
            if item[1] not in m:
                m.update({item[1]:item[0]})
            if item[0].left:
                queue.append((item[0].left,item[1]-1))
            if item[0].right:
                queue.append((item[0].right,item[1]+1))
        print("Top view of the tree is:")
        keys=sorted(m.keys())
        for k in keys:
            print(m.get(k).value)

if __name__=="__main__":
    print("===================================")
    print("The top view of the binary treee is")
    node=Node(12)
    node.insert(6)
    node.insert(10)
    node.insert(4)
    node.insert(2)
    node.insert(5)
    node.insert(20)
    node.insert(25)
    node.insert(18)
    node.insert(26)
    node.insert(22)
    print("============================")
    print("The inorder traversal of the tree:")
    node.inorder()
    print("=================================")
    print("The topview of the binary tree:")
    node.topview()
    print("==================================")


            