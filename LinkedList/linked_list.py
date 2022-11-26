class Node:
    def __init__(self, data = None, next = None):
        self.data=data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head=node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        if temp.next is None:
            temp.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, position, data):
        list_len = self.get_lengh()
        if position<0 or position> list_len:
            raise Exception
        if position ==0:
            self.insert_at_start(data)
            return
        if position == list_len:
            self.insert_at_end(data)
            return
        count = 0
        node = Node(data, None)
        temp = self.head
        while temp:
            if count == position-1:
                node.next = temp.next
                temp.next = node
                return
            count +=1
            temp = temp.next


    def remove_at(self, position):
        list_len = self.get_lengh()
        if position<0 or position>list_len:
            raise Exception
        count = 0
        temp = self.head
        while temp:
            if count == position-1:
                temp.next=temp.next.next
                return
            count +=1
            temp = temp.next



    def insert_after_value(self, data_after, data_insert):
        if self.head is None:
            print("linked list is empty do you want to insert at start? (Y/N)")
            if input() == 'Y':
                self.insert_at_start(data_insert)
                return
            return
        temp = self.head
        node = Node(data_insert, None)
        while temp:
            if temp.next is None and temp.data != data_after:
                print(f"Given number{data_after} is not there")
                return
            if temp.data == data_after:
                node.next = temp.next
                temp.next = node
                return
            temp = temp.next




    def remove_by_value(self, data):
        if self.head is None:
            print("linked list is empty")
            return

        temp = self.head
        while temp:
            if temp.next is None and temp.data != data:
                print(f"Given number{data} is not there")
                return
            if temp.next.data == data:
                if temp.next.next is None:
                    temp.next = None
                    return
                else:
                    temp.next = temp.next.next
                    return
            temp = temp.next





    def get_lengh(self):
        if self.head is None:
            print("linked list is empty")
            return 0
        count = 0
        temp = self.head
        while temp:
            count +=1
            temp=temp.next
        return count

    def print_list(self):
        if self.head is None:
            print('Linked list is empty')
            return
        temp = self.head
        listl = ""
        while temp:
            listl += str(temp.data)+"--->"
            temp=temp.next
        print(listl)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_start(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    ll.insert_at_start(6)
    ll.print_list()
    ll.insert_at(6, 10)
    ll.print_list()
    ll.insert_at(0, 0)
    ll.print_list()
    ll.remove_at(1)
    ll.print_list()
    ll.remove_by_value(10)
    ll.print_list()
    ll.remove_by_value(3)
    ll.print_list()
    ll.insert_at(3, 3)
    ll.print_list()
    ll.insert_at(2, 0)
    ll.print_list()
    ll.remove_at(2)
    ll.print_list()
    ll.insert_at(3, 17)
    ll.print_list()
    ll.remove_by_value(17)
    ll.print_list()
    ll.insert_after_value(1,10)
    ll.print_list()
    ll.insert_after_value(3, 11)
    ll.print_list()
    ll.insert_after_value(5, 12)
    ll.print_list()
    ll.insert_after_value(2, 13)
    ll.print_list()
    ll.insert_after_value(0, 15)
    ll.print_list()
    ll.insert_after_value(22, 15)
    ll.remove_by_value(10)
    ll.print_list()
    ll.remove_by_value(11)
    ll.print_list()
    ll.remove_by_value(12)
    ll.print_list()
    ll.remove_by_value(13)
    ll.print_list()
    ll.remove_by_value(14)
    ll.print_list()
    ll.remove_by_value(15)
    ll.print_list()
    print("length: ", ll.get_lengh())