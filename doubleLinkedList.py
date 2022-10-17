class DoubleLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.previous = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        array_DLL = []
        current_node = self.head
        while current_node is not None:
            array_DLL.append(current_node.value)
            current_node = current_node.next
        return array_DLL

    def unshift_node(self, value):
        new_node = self.Node(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def push_node(self, value):
        new_node = self.Node(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1

    def shift_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        elif self.head != None:
            remove_node = self.head
            self.head = remove_node.next
            remove_node.next = None
            self.length -= 1

    def pop_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            remove_node = self.tail
            self.tail = remove_node.previous
            self.tail.next = None
            remove_node.previous = None
            self.length -= 1

    def get_node_value(self, index):
        if index < 1 or index > self.length:
            print('No se encontro')
        elif index == 1:
            return self.head.value
        elif index == self.length:
            return self.tail.value
        else:
            current_node = self.head
            node_counter = 1
            #Validar que el nodo a consultar sea el mismo del contador
            while (index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node.value

    def get_node(self, index):
        if index < 1 or index > self.length:
            return None
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            node_counter = 1
            while (index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node

    def update_node_value(self, index, new_value):
        search_node = self.get_node(index)
        if search_node != None:
        #Encontro el nodo y se puede actualizar
            search_node.value = new_value
        else:
        #No encuentra el nodo
            return None

    def remove_node(self, index):
        if index == 1:
            self.shift_node()
        elif index == self.length:
            self.pop_node()
        else:
            remove_node = self.get_node(index)
            if remove_node != None:
                previous_node = self.get_node(index - 1)
                next_node = self.get_node(index + 1)
                previous_node.next = next_node
                next_node.previous = previous_node
                self.length -= 1

    def insert_node(self, index, value):
        if index <= 0 or index > self.length + 1:
            print('posicion erronea')
        elif index == 1:
            self.unshift_node(value)
        elif index == self.length + 1:
            self.push_node(value)
        else:
            new_node = self.Node(value)
            previous_node = self.get_node(index - 1)
            next_node = self.get_node(index)
            new_node.next = next_node
            previous_node.next = new_node
            new_node.previous = previous_node
            next_node.previous = new_node
            self.length += 1

    def reverse_node(self):
        i = 1
        tamaño = self.length - 1
        while i <= tamaño:
            self.insert_node(i, self.tail.value)
            self.pop_node()
            i += 1