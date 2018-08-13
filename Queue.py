import queue

option = input("Enter the options \n 1. Create a queue \n 2. Add element \n 3. Remove"+
      " Element \n 4. Break")
option = int(option)
global length
L=None
while(True):
    if(option==1):
        print
        if((L==None)):
            length=input("Enter the maximum length of the queue")
            L = queue.Queue(maxsize=int(length))
            print("Queue is created")
        else:
            print("Queue is already created")
    if(option==2):
        if(L.full()):
            print("The queue is full")
        else:
            data = input("Enter the data")
            L.put(int(data))
            print("You can enter "+str(int(length)-L.qsize())+" more elements")
    if(option==3):
        if(L.empty()):
                L=None
                print("Queue is empty")
        else:
            print("The deleted element is "+str(L.get()))
        
    if(option==4):
        break
    option = input("Enter the options \n 1. Create a queue \n 2. Add element \n 3. Remove"+
      " Element \n 4. Break")
    option = int(option)
    print(option)
    
    
