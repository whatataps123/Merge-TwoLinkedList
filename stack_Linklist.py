class Node :
    def __init__(self,data): 
        self.data = data 
        self.next=None

class Stack:
    def __init__(self):
        self.top =None

    def push(self,data):
        new_node=Node(data)
        if self.top:            
            new_node.next=self.top
        self.top=new_node
    
    def pop(self):
        if self.top is None:
            return  None
        else: 
            popped_node = self.top 
            self.top = self.top.next
            popped_node.next=None
            return popped_node.data
    def peek(self):
        if self.top:
            return self.top.data 
        else:
            return None
        
    def is_empty(self):
        return self.top is None
    
    def print_stack(self):
        current_node=self.top
        while current_node:
            print(current_node.data)
            current_node=current_node.next
        # print("None")
    
    # PRINTS THE STACK IN THE FORMAT 1 -> 2 -> None
    def print_stack_format(self):
        current_node = self.top
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


    def size(self):
        current_node=self.top
        count=0
        while current_node:
            count+=1
            current_node=current_node.next
        return count

def merge_sorted_lists(list1, list2):
    merged_stack = Stack()

    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            merged_stack.push(list1.data)
            list1 = list1.next
        else:
            merged_stack.push(list2.data)
            list2 = list2.next

    # Add any remaining nodes from list1
    while list1 is not None:
        merged_stack.push(list1.data)
        list1 = list1.next

    # Add any remaining nodes from list2
    while list2 is not None:
        merged_stack.push(list2.data)
        list2 = list2.next

    # Reverse the stack to get the correct order
    result_stack = Stack()
    while not merged_stack.is_empty():
        result_stack.push(merged_stack.pop())

    return result_stack

# Example usage:
# Creating linked lists for list1 and list2
list1 = Node(11)
list1.next = Node(33)
list1.next.next = Node(81)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(9)

# Merging the lists
merged_list = merge_sorted_lists(list1, list2)

# Printing the merged list
print("Merged List:")
merged_list.print_stack_format()

# example usage
# stack=Stack()
# stack.push(1)
# stack.push(2)

# stack.push(3)
# stack.push(4)
# stack.print_stack()
# print("Top element:", stack.peek())  # Output: 4
# print("Stack size:", stack.size())   # Output: 3
# print("Popped element:", stack.pop()) # Output: 4
# print("Popped element:", stack.pop()) # Output: 3
# print("Stack is empty:", stack.is_empty()) # Output: False
# stack.print_stack()


