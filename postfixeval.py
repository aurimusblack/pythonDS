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
            i = self.ar[-1]
            self.top=self.top-1
            self.ar.pop()
            return i
st=Stack()
ip=str(input())
k=0
def numeric(a):
    if a=='0':
        return 0
    if a=='1':
        return 1
    if a=='2':
        return 2
    if a=='3':
        return 3
    if a=='4':
        return 4
    if a=='5':
        return 5
    if a=='6':
        return 6
    if a=='7':
        return 7
    if a=='8':
        return 8
    if a=='9':
        return 9
    
    return 10
    
    
while True :
    i = ip[k]
    
    if i == 'q':
        break
    if numeric(i) < 10 :
        st.push(numeric(i))
        k = k + 1
        
    else:
        op1 = st.pop()
        op2 = st.pop()
        if i == '+':
            st.push(op1+op2)
            k = k + 1
        if i == '-':
            st.push(op1-op2)
            k = k + 1
        if i == '*':
            st.push(op1*op2)
            k = k + 1
        if i == '/':
            st.push(op1/op2)
            k = k + 1
print(st.ar[st.top])
