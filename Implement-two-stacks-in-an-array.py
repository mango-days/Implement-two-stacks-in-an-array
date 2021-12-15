# Implement two stacks in an array

# Your task is to implement  2 stacks in one array efficiently.

stack1 = []
stack2 = []

def push ( stack , data ) :
    stack.insert ( 0 , data )

def pop ( stack ) :
    print ( stack [ 0 ] )
    stack.pop(0)

def print_stack ( stack ) :
    print ( stack )
    
def top ( stack ) :
    print ( stack [ 0 ] )
    
def copy_stack ( stackA , stackB ) :
    stackA = stackB.copy()
    
push ( stack1 , 1 )
push ( stack1 , 2 )
push ( stack1 , 3 )
print_stack ( stack1 )
top ( stack1 )
pop ( stack1 )
print_stack ( stack1 )

push ( stack2 , 4 )
push ( stack2 , 5 )
push ( stack2 , 6 )
print_stack ( stack2 )
top ( stack2 )
pop ( stack2 )
print_stack ( stack2 )