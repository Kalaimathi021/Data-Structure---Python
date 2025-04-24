class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def split_linked_list(head):
    # Initialize heads and tails for odd and even lists
    odd_head = odd_tail = None
    even_head = even_tail = None
    current = head
    index = 1  # Position counter

    while current:
        # Create a new node for the current data
        new_node = Node(current.data)
        
        if index % 2 == 1:  # Odd position
            if not odd_head:  # First odd node
                odd_head = odd_tail = new_node
            else:
                odd_tail.next = new_node
                odd_tail = new_node
        else:  # Even position
            if not even_head:  # First even node
                even_head = even_tail = new_node
            else:
                even_tail.next = new_node
                even_tail = new_node
        
        # Move to the next node and increment the position
        current = current.next
        index += 1

    return odd_head, even_head

# Helper function to print a linked list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next

# Example usage
# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Split the list
odd_list, even_list = split_linked_list(head)

# Output the results
print("Odd list:")
print_list(odd_list)

print("Even list:")
print_list(even_list)
