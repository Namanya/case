#changing intenger to binary format using recursion
def change_int(n, base):
    convert_string = "01"
    if n < base:
        return convert_string [n]
    else:
        return change_int(n // base, base) + convert_string [n % base]



#insertion sort ds
def insertion_sort(lst):
    lst2 = []
    for i in range(1, len(lst)): 
        key = lst[i]
        j = i-1

        while j >= 0 and key <= lst[j]:
            lst[j + 1] = lst[j]
            j =- 1
        lst[j + 1]  = key
        
    return lst2


# Driver code to test above
if __name__ == '__main__':
    lst = [12, 5, 8, 11]
    print(insertion_sort(lst))