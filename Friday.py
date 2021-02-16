
# Given a linked list, remove the n-th node from the end of list and return its head.
#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 1
        current_node = head
        
        while current_node.next:
            current_node = current_node.next
            count += 1
            
        remove_index = count - n
        current_node = head
        
        if remove_index == 0:
            if count == 1:
                return None
            else:
                head = current_node.next
                current_node.next = None
                return head
        else:
            pre_node = None
            for i in range(remove_index):
                pre_node = current_node
                current_node = current_node.next
            
            if remove_index == count-1:
                pre_node.next = None
            else:
                pre_node.next = current_node.next
            return head

# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
# Function to check parentheses 
#Check for balanced parentheses in Python
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
    else: 
        return "Unbalanced"
  
  
# Driver code 
string = "{[]{()}}"
print(string,"-", check(string)) 
  
string = "[{}{})(]"
print(string,"-", check(string)) 
  
string = "((()"
print(string,"-",check(string)) 

