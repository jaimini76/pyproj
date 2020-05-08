class node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class list:
    def __init__(self):
        self.head = None

    def insert(self, value):

        newNode = node(value)

        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode

    def delete(self, value):
        if self.head == None:
            print("List is empty")
            return
        else:
            current = self.head
            # Need this if there is only one element in the list
            # while loop is not entered, so we need to initialize
            # previous.
            previous = current

            while (current.next):
                previous = current
                if current.value == value:
                    break
                else:
                    current = current.next

            # we found the element to delete.
            if current.value == value:
                # Deleting last element in the list
                if current.next == None:
                    # There is only one element in the list
                    if current == previous:
                        self.head = None
                    else:
                        previous.next = None
                # Deleting first element
                elif previous == current:
                    self.head = current.next
                # deleting intermidiate element
                else:
                    previous.next = current.next
            else:
                print("Element not Found.")

    def print_list(self):
        if self.head == None:
            print("List is empty")
        else:
            current = self.head
            while(current.next):
                print(f"{current.value}")
                print("->")
                current = current.next
            # print last element in the list
            print(f"{current.value}")
            print("->Null")

if __name__ == '__main__':

    mylist = list()

    for i in range(0,10):
        mylist.insert(i)
    mylist.print_list()

    for i in range(0,10):
        mylist.delete(i)
    mylist.print_list()

    #mylist.delete(0)
    #mylist.print_list()
    #mylist.delete(9)
    #mylist.print_list()