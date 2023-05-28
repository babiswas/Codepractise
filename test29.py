class Node:

    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

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

    def height(self):
        count=0
        queue=list()
        queue.append(self)
        while queue:
            q_len=len(queue)
            if q_len:
                count+=1
            while q_len:
                m=queue.pop(0)
                if m.left:
                    queue.append(m.left)
                if m.right:
                    queue.append(m.right)
                q_len-=1
        return count

    
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

    def spiral_trav(self):
        stack1=list()
        stack2=list()
        stack1.append(self)
        while stack1 or stack2:
            while stack1:
                m=stack1.pop()
                print(m.value)
                if m.left:
                   stack2.append(m.left)
                if m.right:
                   stack2.append(m.right)
            while stack2:
                n=stack2.pop()
                print(n.value)
                if n.right:
                    stack1.append(n.right)
                if n.left:
                    stack1.append(n.left)

if __name__=="__main__":
    print("===========================")
    print("Building the tree:")
    node=Node(12)
    node.insert(18)
    node.insert(5)
    node.insert(20)
    node.insert(16)
    node.insert(8)
    node.insert(4)
    node.insert(10)
    node.insert(6)
    print("===========================")
    print("The inorder order traversal of the tree is:")
    node.inorder()
    print("The spiral order traversal of the tree is:")
    node.spiral_trav()
    print("================================")
    print("The height of the tree is:")
    ht=node.height()
    print(f"The height of the tree is {ht}")
    print("==================================")

            
    
