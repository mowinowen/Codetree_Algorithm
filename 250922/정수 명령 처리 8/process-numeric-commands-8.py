class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0
    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

        else:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
        
        self.node_num += 1
    
    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        
        self.node_num += 1
    
    def pop_front(self):
        if self.head == None:
            print('List is Empty')

        elif self.head.next == None:  # 연결 리스트에 1개만 있을 때
            temp = self.head
            self.head = None
            self.tail = None
            self.node_num -= 1
            return temp.data

        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            self.node_num -= 1
            return temp.data
        

    def pop_back(self):
        if self.tail == None:
            print('List is Empty')
        
        elif self.tail.prev == None:
            temp = self.tail
            self.head = None
            self.tail = None
            self.node_num -= 1
            return temp.data
        
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            self.node_num -= 1
            return temp.data
    
    def size(self):
        return self.node_num

    def empty(self):
        return 1 if self.node_num == 0 else 0
    
    def front(self):
        if self.head == None:
            print('List is Empty')
        else:
            return self.head.data
    
    def back(self):
        if self.tail == None:
            print('List is Empty')
        else:
            return self.tail.data


N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
l = DoublyLinkedList()

for i in range(N):
    if command[i] == 'push_front':
        l.push_front(A[i])
    elif command[i] == 'push_back':
        l.push_back(A[i])
    elif command[i] == 'pop_front':
        print(l.pop_front())
    elif command[i] == 'pop_back':
        print(l.pop_back())
    elif command[i] == 'size':
        print(l.size())
    elif command[i] == 'empty':
        print(l.empty())
    elif command[i] == 'front':
        print(l.front())
    elif command[i] == 'back':
        print(l.back())

