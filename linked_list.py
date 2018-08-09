#LINKED LIST
#Linked list is often compared to arrays.
#Whereas an array is a fixed size of sequence,
#a linked list can have its elements to be dynamically allocated.

#A linked list saves memory
#Linked list nodes can live anywhere in the memory.

#Linear look up time

class Node:
    def __init__(self,val):
        self.val=val            #data in each node
        self.next=None          #Initially only one node
    def traversing(self):
        pass


if __name__=='__main__':
    print('Enter The Option \n')
    option = input(' 1. Create root node \n 2. Add a node \n 3. traversing a node\n 4. Deleting a node \n 5. Break \n')
    option = int(option)
    root = None
    temp=None
    last = None
    while(True):
        if(option==1):#Root Creation
            if(root==None):
                data=input(" Enter the data for root node ")
                root=Node(data)
                last = root
                print(" Root Node Created ")
            else:
                print(" Root Node Already created ")
        if(option==2):#Addition of new node
            if  root == None:
                print(" you dont have root node ")
            else:
                data=input(" Enter the data for the node ")
                temp = Node(data)
                last.next = temp
                last = temp
            
        if(option==3):#traversing nodes
            if root == None:
                print(" No nodes ")
            else:
                temp= root
                print(" \n the nodes are \n")
                while temp:
                    print(temp.val)
                    temp = temp.next
        if(option==4):#deleting node
            if(root!=None):
                data= input("Enter the data to be deleted")
                temp = root
                prev=root
                while temp:
                    if temp.val==data and temp == root:
                        print("root is deleted")
                        root=temp.next
                        temp=root
                        break
                    elif(temp.val==data and temp != root):
                        print(temp.val+ "node is deleted")
                        prev.next = temp.next
                        break
                    
                    else:
                        prev=temp
                        temp =temp.next
            else:
                print("No nodes to delete")
        if(option==5):
            print("Break")
            break
        option = input(' 1. Create root node \n 2. Add a node \n 3. traversing a node\n 4. Deleting a node \n 5. Break \n')
        option = int(option)
        
    
