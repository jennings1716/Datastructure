#Circular linked list is a linked list where all nodes are connected to form
#a circle. There is no NULL at the end. A circular linked list can be
#a singly circular linked list or doubly circular linked list.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

if __name__=='__main__':
    print('Enter The Option \n')
    option = input(' 1. Create root node \n 2. Add a node \n 3. traversing a node\n 4. Deleting a node \n 5. Break \n')
    option = int(option)
    root = None
    last=None
    while(True):
        if(option==1):#Root Creation
            if(root==None):
                data=input(" Enter the data for root node ")
                root=Node(data)
                root.next=root
                last=root
                last.next=root
            else:
                print('Root node already created')
        if(option==2):
            if(root!=None):
                data=input(" Enter the data for new node ")
                node = Node(data)
                last.next=node
                node.next=last
                last=node
            else:
                print("Please create a root node")
        if(option==3):
            if(root!=None):
                temp=root
                print("The nodes are")
                while temp:
                    if(temp.data==last.data):
                        print(temp.data)
                        break
                    else:
                        print(temp.data)
                    temp=temp.next
            else:
                print("You dont have root node")
        if(option==4):
            if(root!=None):
                data=input(" Enter the data of the node to be deleted")
                temp=root
                while temp:
                    if temp.data==data and temp == root:
                        root_next=root.next
                        if(root_next.data!=root.data):
                            print("root")
                            root=temp.next
                            last.next=root
                            temp=root
                        else:
                            root.next=None  
                            root=None
                            temp=None
                        break
                        print("root is deleted")
                        print(temp.next)
                        
                    elif(temp.data==data and temp != root):
                        print(temp.data+ "node is deleted")
                        prev.next = temp.next
                        if(last.data==data):
                            last=prev
                        break
                    
                    else:
                        prev=temp
                        temp =temp.next
            else:
                print("You have no nodes")
        if(option==5):
            print("break")
            break
        option = input(' 1. Create root node \n 2. Add a node \n 3. traversing a node\n 4. Deleting a node \n 5. Break \n')
        option = int(option)

