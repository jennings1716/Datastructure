class stack:
    def __init__(self):
        self.stack=list()
    def append(self,data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
    def display(self):
        print(self.stack)
option = input("Enter the option \n 1. Create a List \n 2. Push an element"+
                   "\n 3. Pop an element \n 4. display \n 5. Break \n")
option = int(option)
while True:
    if(option==1):
        s = stack()
        print(s)
        print("Stack is created")
    if(option==2):
        data =  input("Enter the data to be pushed")
        s.append(data)
    if(option==3):
        if len(s.stack)<= 0:
            print("Stack is empty")
        else:
            print(str(s.pop())+"is the popped element")
    if(option==4):
        s.display()
    if(option==5):
        break
    option = input("Enter the option \n 1. Create a List \n 2. Push an element"+
                   "\n 3. Pop an element \n 4. display \n 5. Break \n")
    option = int(option)
