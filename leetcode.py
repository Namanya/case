def removeDuplicates(nums):
    if not nums:
        return 0

    nums.sort()
    numbers = []
    j = 0
    for i in range(len(nums)):
        if nums[i] != nums[i-1]:
            numbers.append(nums[i])
        else:
            i = i + 1
            
    return numbers


def twoSum( nums, target):
    c = []
    for i, num in enumerate(nums):
        numer = target - num
        self = numer
        if numer in nums:
            a = i
            b = nums.index(numer)
            if i != nums.index(numer):
                c.append([a, b])
            i = i + 1
            
    return c[0]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    l3 = ListNode()
    current = l3
    carry = 0

    while l1 or l2 or carry:  
        if l1:
            val1 = l1.val
            l1 = l1.next
        else:
            val1 = 0
        if l2:
            val2 = l2.val
            l2 = l2.next
        else:
            val2 = 0
        

        summed = val1 + val2 + carry
        if summed > 9:
            carry = 1
            summed = summed % 10
        else:
            carry = 0
    
        current.next = ListNode(summed)
        current = current.next
       
       
    return l3.next
        
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

results = addTwoNumbers(l1, l2)

Ll = []
current = results 
while current:
    Ll.append(current.val)
    current = current.next



def lengthOfLongestSubstring(s):
    len_s = len(s)
    sub_set = set()
   
    if len_s == 0:
        return 0
    right = left = max_len = 0

    while right < len_s:
        if s[right] not in sub_set:
            sub_set.add(s[right])
            right += 1
            max_len = max(max_len, right-left)
        else:
            sub_set.remove(s[left])
            left += 1
    return max_len

s = ""
def findMedianSortedArrays(nums1, nums2):
        nums3 = nums1 + nums2
        nums3.sort()
        n = len(nums3)
        if n == 0:
            return None
        elif n % 2 == 1:
            return nums3[n//2]
        else:
            return ((n//2 - 1), (n//2))

nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))