#Double Linked List
#A Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer,
#together with next pointer and data which are there in singly linked list.
import time
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next= None

if __name__=='__main__':
    print('Enter The Option \n')
    option = input(' 1. Create root node \n 2. insert a node  \n 3. traversing \n 4. Delete a node'+
                       '\n 5. Break \n')
    option = int(option)
    root = None
    while(True):
        if(option==1):
            if(root==None):
                data=input(" Enter the data for root node ")
                root=Node(data)
                root.prev=None
                root.next=None
                last=root
                print(" Root Node Created ")
            else:
                print(" Root Node Already created ")

        if(option==2):
            flag=0
            t=root
            while t:
                if t.next==None: 
                    last=t
                    break
                t=t.next
            
            if(root!=None):
                data=input(" Enter the data near to which you have to enter")
                t=root
                while t:
                    if t.data==data:
                        flag=1
                        break
                    t=t.next
                if(flag==0):
                        print("Data is not found")
                if(flag==1):     
                    new_data = input(" Enter the data of new node")
                    pos = input(" Enter the position \n 1.before \n 2.After")
                    node = Node(new_data)
                    temp = root
                    while temp:
                        if temp.data == data:
                            if(pos=='1'):
                                if(temp.data==root.data):
                                    temp.prev=node
                                    node.next=root
                                    root=node
                                    break
                                else:
                                    previous = temp.prev
                                    previous.next=node
                                    node.prev=previous
                                    node.next=temp
                                    previous=node
                                    break
                            if(pos=='2'):
                                if(temp.data==last.data ):
                                    node.prev=last
                                    last.next=node
                                    last=node
                                    break
                                else:
                                    node.next=temp.next
                                    temp.next.prev=node
                                    temp.next = node
                                    node.prev= temp
                                    break
                        temp=temp.next
                    
            else:
                print("You have no root node please create a root")
                
        if(option==3):
            if(root!=None):
                temp=root
                print("\n The Nodes are")
                while temp:
                    print(temp.data)
                    temp=temp.next
            else:
                print("You have no root node please create a root node")
        
        if(option==4):
            if(root!=None):
                del_node = input(" Enter the data of node to be deleted")
                temp=root
                while temp:
                    previous=temp.prev
                    next_node=temp.next
                    if(temp.data==del_node):
                        if(next_node==None and previous==None):
                            root=None
                            print("Root node deleted")
                        elif(next_node==None):
                            previous.next=None
                        elif(previous==None):
                            next_node.prev=None
                            root=next_node                            
                        else:
                            previous.next=next_node
                            next_node.prev=previous
                    temp=temp.next
            else:
                print("You have no nodes to delete")
        if(option==5):
            print("Break")
            break
        time.sleep(0.4)
        print('\n')
        option = input(' 1. Create root node \n 2. insert a node \n 3. traversing \n 4. Delete a node'+
                       '\n 5. Break \n')
        option = int(option)
                
                
                

