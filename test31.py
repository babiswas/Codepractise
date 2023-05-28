from __future__ import annotations
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

    def is_present(self,value):
        node1=None
        node2=None
        if self.value==value:
            return self
        else:
            if self.left:
               node1=self.left.is_present(value)
            if self.right:
               node2=self.right.is_present(value)
            if node1!=None:
                return node1
            elif node2!=None:
                return node2
            else:
                return None
            
    def lca(self,node1:Node,node2:Node):
        test1=None
        test2=None
        if self==node1 or self==node2 or (not self):
              return self
        else:
            if self.left:
                test1=self.left.lca(node1,node2)
            if self.right:
                test2=self.right.lca(node1,node2)
            if test1==None:
                return test2
            elif test2==None:
                return test1
            else:
                return self
            
if __name__=="__main__":
    print("=============================")
    print("The lowest common ancestor of the tree is:")
    node=Node(12)
    node.insert(5)
    node.insert(10)
    node.insert(4)
    node.insert(18)
    node.insert(20)
    node.insert(16)
    node.insert(1)
    print("==============================")
    node1=node.is_present(18)
    node2=node.is_present(1)
    print(f"The value of node1 is {node1.value}")
    print(f"The value of node2 is {node2.value}")
    print("====================================")
    print("The lowest common ancestor of the tree is:")
    print(node.lca(node1,node2).value)
    #print(f"The lowest common ancestor of the tree is:{node3.value}")
    print("=======================================")


            
            
            
        
