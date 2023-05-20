class Node:
    # constructor method
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    
    # toString method
    def __repr__(self):
        return f"({self.value}, {self.next})"

# main function
def remove_dup(lst):
    while lst != None:
        # sorted --> duplicates next to each other
        if lst.value == lst.next.value:
            # link node the node after next (removes next node)
            lst.next = lst.next.next
        lst = lst.next
        
# iterate print values of LinkedList
def out(lst):
    trav = lst
    while trav != None: 
        print(trav.value)
        trav = trav.next
    

lst = Node(1, Node(2, Node(2, Node(3, Node(3)))))

remove_dup(lst)
print(lst)
# (1, (2, (3, None)))