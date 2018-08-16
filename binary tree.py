class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def inorder(node):
     if (node != None):
         inorder(node.left);
         print(node.data)          
         inorder(node.right);
         

      
option = input("Enter the option \n 1. create a root node \n 2. add a node \n 3.Traversing a tree"+
               " \n 4. Break")
option = int(option)

root=None
while True:
    if(option==1):
        if root==None:
            data= input("Enter the data")
            node = Node(data)
            root=node
            print("Root Node created")
        else:
            print("You have a root node")
    if(option==2):
        if(root != None):
            data= input("Enter the data")
            node = Node(data)
            temp=root
            while temp:
                if(int(temp.data)>int(data)):
                    if(temp.left==None):
                        flag="left"
                        break
                    else:
                        temp=temp.left
                elif(int(temp.data)<int(data)):
                    if(temp.right==None):
                        flag="right"
                        break
                    else:
                        temp=temp.right
            if(flag=="left"):
               temp.left=node
            else:
               temp.right=node
    
    if(option==3):
        inorder(root)
   
    if(option==4):
            break
                    

    option = input("Enter the option \n 1. create a root node \n 2. add a node \n 3.Traversing a tree"+
               " \n 4. Break")
    option = int(option)
