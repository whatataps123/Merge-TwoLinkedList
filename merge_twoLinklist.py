class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail=new_node


    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head=new_node
    
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
    def printLinkedList(self):
            current_node = self.head
            while current_node:
                print(current_node.data, end="")
                if current_node.next:
                    print(" -> ", end="")
                current_node = current_node.next
    
    def remove_beginning(self):
        if self.head:
            removed_data = self.head.data
            self.head = self.head.next
            if not self.head:
                # If the list becomes empty after removal
                self.tail = None
            return removed_data
        else:
            return None

    def remove_at_end(self):
        if self.head:
            current_node = self.head
            previous_node = None
            while current_node.next:
                previous_node = current_node
                current_node = current_node.next

            if previous_node:
                removed_data = current_node.data
                previous_node.next = None
                self.tail = previous_node
                return removed_data
            else:
                # Only one element in the list
                removed_data = current_node.data
                self.head = None
                self.tail = None
                return removed_data
        else:
            return None

    def remove_at(self, data):
        current_node = self.head
        previous_node = None

        while current_node:
            if current_node.data == data:
                if previous_node:
                    previous_node.next = current_node.next
                    if not current_node.next:
                        self.tail = previous_node
                else:
                    self.head = current_node.next
                    if not current_node.next:
                        self.tail = None
                return current_node.data

            previous_node = current_node
            current_node = current_node.next

        return None
    
    def merge_sorted_lists(self, other_list):
        merged_list = LinkedList()
        current_self = self.head
        current_other = other_list.head

        while current_self is not None and current_other is not None:
            if current_self.data < current_other.data:
                merged_list.insert_at_end(current_self.data)
                current_self = current_self.next
            else:
                merged_list.insert_at_end(current_other.data)
                current_other = current_other.next

        # If one of the lists is not empty, append the remaining nodes
        while current_self is not None:
            merged_list.insert_at_end(current_self.data)
            current_self = current_self.next

        while current_other is not None:
            merged_list.insert_at_end(current_other.data)
            current_other = current_other.next

        return merged_list

list1 = LinkedList()
list1.insert_at_end(5)
list1.insert_at_end(9)
list1.insert_at_end(10)

list2 = LinkedList()
list2.insert_at_end(1)
list2.insert_at_end(3)
list2.insert_at_end(6)

merged_list = list1.merge_sorted_lists(list2)

# Print list1
print("List 1:", end=" ")
list1.printLinkedList()
print()

# Print list2
print("List 2:", end=" ")
list2.printLinkedList()
print()

# Print merged_list
print("Merged List:", end=" ")
merged_list.printLinkedList()
print()
