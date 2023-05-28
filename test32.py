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

    def btree_dll(self):
        stack=list()
        head=None
        prev=None
        temp=self
        while True:
            if temp:
               stack.append(temp)
               temp=temp.left
            elif stack:
                temp=stack.pop()
                if head==None:
                    head=temp
                    prev=temp
                else:
                    if temp.left==prev:
                        prev.right=temp
                        prev=temp
                    elif prev.right==temp:
                        temp.left=prev
                        prev=temp
                    elif temp.right!=prev and temp.left!=prev:
                         prev.right=temp
                         prev=temp
                temp=temp.right
            else:
                break
        return head
    
if __name__=="__main__":
    print("================================")
    print("Building the tree")
    node=Node(12)
    node.insert(18)
    node.insert(20)
    node.insert(16)
    node.insert(25)
    node.insert(19)
    node.insert(8)
    node.insert(10)
    node.insert(6)
    node.insert(3)
    node.insert(7)
    print("==================================")
    print("Convert binary tree to DLL")
    head=node.btree_dll()
    temp=head
    while temp!=None:
        print(temp.value)
        temp=temp.right
    print("DLL traversal completed:")
    print("================================")

            
