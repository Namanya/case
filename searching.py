def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else: 
            pos = pos + 1 
    return found
    

def num_searc(l, i):
    n_l = []
    for x in l:
        if x == i:
            n_l.append(x)  
    return len(n_l)

l = [15, 18, 2, 19, 18, 0, 8, 14, 19, 14]



def binary_search(i_list, item):
    first = 0 
    last = len(i_list) - 1
    found = False

    while first < last and not found:
        mid_index = (first + last)//2
        if i_list[mid_index] == item:
            found = True
        elif i_list[mid_index] < item:
            last = mid_index -1 
        else:
            first = mid_index + 1 

    return found
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]


def bubble_sort(i_list):
    
    for i in range(len(i_list) -1, 0, -1):
        for x in range(i):

            if i_list[x] > i_list[ x + 1]:
                temp = i_list[x +1]
                i_list[x + 1] = i_list[x]
                i_list[x] = temp
    return  i_list
i_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(bubble_sort(i_list))


