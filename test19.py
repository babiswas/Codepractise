class Node:
    def __init__(self,value:int)->None:
        self.value=value
        self.left=None
        self.right=None

    def postorder(self)->None:
        stack=list()
        temp=self
        while True:
            if temp:
                stack.append(temp)
                temp=temp.left
            else:
                if not stack:
                    break
                if stack[-1].right==None:
                    temp=stack.pop()
                    print(temp.value)
                    while stack[-1].right==temp:
                        temp=stack.pop()
                        print(temp.value)
                        if not stack:
                            break
                if stack:
                    temp=stack[-1].right
                else:
                    break

    def insert(self,value:int)->None:
        if self.value>value:
            if self.left:
                self.left.insert(value)
            else:
                self.left=Node(value)
        if self.value<value:
            if self.right:
                self.right.insert(value)
            else:
                self.right=Node(value)
        else:
            print("Duplication not allowed:")

    def preorder(self):
        stack=list()
        temp=self
        stack.append(temp)
        while stack:
            temp=stack.pop()
            print(temp.value)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
    
    def inorder(self):
        stack=list()
        temp=self
        while True:
            if temp:
                stack.append(temp)
                temp=temp.left
            elif stack:
                temp=stack.pop()
                print(temp.value)
                temp=temp.right
            else:
                break

if __name__=="__main__":
    print("=============================")
    print("Binary tree traversal:")
    node=Node(12)
    node.insert(18)
    node.insert(22)
    node.insert(25)
    node.insert(20)
    node.insert(30)
    node.insert(15)
    node.insert(8)
    node.insert(6)
    node.insert(10)
    node.insert(11)
    node.insert(5)
    print("==============================")
    print("Inorder traversal of the graph is:")
    node.inorder()
    print("================================")
    print("preorder traversal of the graph:")
    node.postorder()
    print("===================================")
    print("Preorder traversal of the graph is:")
    node.preorder()
    print("===============================")
