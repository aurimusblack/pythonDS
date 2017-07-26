import sys
class Stack:
    top=-1
    ar=[]
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    def isFull(self):
        if self.top==19:
            return True
        else:
            return False

    def push(self,setn):
        if self.isFull():
            print("the stack is full")
            return
        else:
            self.top=self.top+1
            self.ar.append(setn)
            print("record is inserted")

    def pop(self):
        if self.isEmpty():
            print("no items in stack")
            return
        else:
            self.top=self.top-1
            self.ar.pop()

st=Stack()
st.push(10)
st.push(20)
print(st.ar[0])
st.pop()
print(st.top)


    
    
