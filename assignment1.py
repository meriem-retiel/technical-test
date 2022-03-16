
# DEFINING A NODE
class SinglyLinkedListNode:
   def __init__(self, data):
      self.data = data
      self.next = None

# FUNCTION TO COMPARE TWO LISTS
def compare_lists (list1,list2):
    equal=1;
    while((list1 is not  None) & (list2 is not None)):
        if(list1.data!=list2.data):
            equal=0;
            break;
        else:
            list1 = list1.next;
            list2 = list2.next; 
        # If we didn't get to the end when looping on one of the two lists then they are for sure different
    if((list1 is not None) | (list2 is not None)):
        return 0
    else:
        return equal

#TESTING THE FUNCTION

#Function to create a list with n nodes
def newList(n):
    list = None
    for i in range(n):
        dataVal=int(input(""))
        if(i==0):
            list=SinglyLinkedListNode(dataVal)
            node=list
        else:
            node.next=SinglyLinkedListNode(dataVal)
            node=node.next
    return list

#Number of tests
t= int(input(""))

#Creatinf t tests
for i in range(t):

    n=int(input(''));
    list1=newList(n);

    m=int(input(''));
    list2=newList(m);

    print(compare_lists(list1,list2))





