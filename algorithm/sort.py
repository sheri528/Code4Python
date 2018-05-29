# coding:utf-8

def quicksort(list):
    # 递归结束条件
    if len(list) < 2:
        return list
    else:
        midpivot = list[0]
        lessbeforemidpivot = [i for i in list[1:] if i <= midpivot]
        biggerafterpivot = [i for i in list[1:] if i > midpivot]
        finallylist = quicksort(lessbeforemidpivot) + [midpivot] + quicksort(biggerafterpivot)
        return finallylist


# print quicksort([2,4,6,7,1,2,5])

def bublesort(list):
    len_list = len(list)
    for i in range(len_list):
        #
        flag = 0
        for j in range(len_list - i - 1):
            # j锁定本次排序较大的数; i控制需要比较范围; flag本次无交换，说明相邻元素顺序正确，已排好序
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                flag = 1
        else:
            if not flag:
                break
    return list


# print bublesort([9,4,7,6,1,3,2,8,9])

def selectSort(list):
    len_list = len(list)

    for i in range(len_list):
        min_item_index = i
        for j in range(i + 1, len_list):
            if list[j] < list[min_item_index]:
                min_item_index = j
        list[i], list[min_item_index] = list[min_item_index], list[i]
    return list


# print selectSort([9,4,7,6,1,3,2,8,9])

# 直接插入，折半插入，表插入
# in-place, 需要o(1)的额外空间
def insertSort(list):
    len_list = len(list)

    for i in range(len_list):
        temp = list[i]
        for j in range(i - 1, -1, -1):
            if list[j] > temp:
                list[j + 1] = list[j]
                list[j] = temp
            else:
                break

    return list


# print insertSort([9,4,7,6,1,3,5,2,8,9])

def insertSort_Bin(list):
    len_list = len(list)

    for i in range(len_list - 1):
        temp = list[i + 1]
        left = 0
        right = i
        while left < right:
            mid = (left + right) // 2
            if list[mid] < temp:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if temp > list[left]:
                left += 1

        list.insert(left, temp)
        list.pop(i + 2)
    return list


# print insertSort_Bin([9,4,7,6,1,3,5,2,8,9])

# merge sort
def merge(list_a, list_b):
    '''
        a,b有序
    '''
    merged_list = []
    # 用到a[0],b[0] => 条件必须是and
    while list_a and list_b:
        if list_a[0] > list_b[0]:
            merged_list.append(list_b[0])
            list_b.remove(list_b[0])
        else:
            merged_list.append(list_a[0])
            list_a.remove(list_a[0])
    else:
        merged_list.extend(list_b)
        merged_list.extend(list_a)

    return merged_list


# print(merge([1,2,3], [4,5,6]))
# print(merge([], []))
# print(merge([10], [9]))

def mergeSort(l):
    l_len = len(l)
    # 递归基线条件
    if l_len < 2:
        return l
    else:
        mid = l_len / 2
        left_list = mergeSort(l[:mid])
        right_list = mergeSort(l[mid:])
        # 左右有序后，合并两个有序列表
        return merge(left_list, right_list)


# print(mergeSort([4,9,7,2,1,8,0,3,6,5]))
print(mergeSort([1, 0, 3, 2]))
