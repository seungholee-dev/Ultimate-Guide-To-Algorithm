class ListNode:
    def __init__(self):
        self.val = 0
        self.next = None

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
    
    def add(self, val):
        if(head == None):
            self.head = ListNode(val)
            self.last = head
        else:
            self.last.next = ListNode(val)
            self.last = self.last.next
    
    def add_to_front(self.val):
        if(head == None):
            self.head = ListNode(val)
            self.last = head
        else:
            new_head = ListNode(val)
            new_head.next = self.head
            self.head = new_head
            

