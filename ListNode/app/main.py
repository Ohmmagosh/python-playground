
class ListNode:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def add_back(self, next=None):
    if self.next == None:
      self.next = next
    else:
      tmp = self.is_last()
      tmp.next = next

  def is_last(self):
    if self.next == None:
      return self
    else:
      tmp = self
      while tmp.next != None:
        tmp = tmp.next
      return tmp

  def print_list(self):
    tmp = self
    while tmp != None:
      print(tmp.value)
      tmp = tmp.next

def main():
  lst = ListNode(1)
  lst.add_back(ListNode(2))
  lst.add_back(ListNode(3))
  lst.add_back(ListNode(4))
  lst.add_back(ListNode(5))
  lst.print_list()

if __name__ == "__main__":
  main()
