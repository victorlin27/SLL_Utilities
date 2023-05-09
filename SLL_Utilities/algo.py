class Node:
    def __init__(self,datal):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head =None

# Add a method contains(value) to your SLL class, which is given a value as a parameter.  Return a boolean (true/false); true, if the list possesses a node that contains the provided value.
    def contain(self,val):
        current = self.head
        while current:
            if current.data ==val:
                return True
            current = current.next
        return False

# Create a new SLL method length() that returns number of nodes in that list.
    def length(self):
        current = self.head
        count = 0
        while current:
            count +=1
            current = current.next
        return count

# Create display() that returns a string containing all list values. Build what you wish console.log(myList) did!
    def display(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return ' '.join(values)