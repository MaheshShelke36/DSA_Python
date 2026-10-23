class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class stack:
    def __init__(self):
        self.top=None

    def isempty(self):
        return self.top is None

    def push(self,new_node):
        new_node.next = self.top
        self.top=new_node

    def pop(self):
        temp=self.top
        print("poped element: ",temp.data)
        self.top=self.top.next
        temp=None

    def print(self):
        temp=self.top
        print("Stack elements...")
        while temp:
            print(temp.data)
            temp=temp.next

st=stack()
st.push(node(10))            
st.push(node(100))   
st.push(node(45))   
st.push(node(78))   
st.push(node(90))

st.print()
st.pop()
st.print()
st.pop()
st.print()
print("inserting new node")
st.push(node(82))
st.print()