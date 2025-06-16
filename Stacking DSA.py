class stack:
    def __init__(self):
        self.stack = []

    def add(self,datav):
        if datav is not self.stack:
            self.stack.append(datav)
            return True
        else:
            return False
        
    def peek(self):
         return self.stack[-1]
    
ASTACK = stack()
ASTACK.add("mon")
ASTACK.add("tue")
ASTACK.add("wed")
print(ASTACK.peek())

class stack:

    def __init__(self):
        self.stack =[]

    def add(self,datas):
        if datas is not self.stack:
            self.stack.append(datas)
            return True
        else:
            return False
        
    def remove(self):
        if len(self.stack)<=0:
            return "No element in stack"
        else:
            return self.stack.pop()
        

ASTACK = stack()
ASTACK.add("mon")
ASTACK.add("tue")
ASTACK.add("wed")
print(ASTACK.remove())
print(ASTACK.remove())

    
