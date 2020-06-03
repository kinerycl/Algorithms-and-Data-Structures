"""
PROJECT 3 - Merge Sort
Name: Clare Kinery
"""
from Project3.LinkedList import LinkedList

def merge_lists(lists, threshold):
    """
    Merges a list of linked lists together
    :param lists: list of linked lists
    :param threshold: int number
    :return: linked list
    """
    big_list = LinkedList() #return list, empty
    for list in lists:
        list = merge_sort(list, threshold)
        big_list = merge(big_list, list)

    return big_list

def merge_sort(linked_list, threshold):
    """
    Uses merge sort to sort a linked list, when
    list length is less than or equal to
    threshold uses insertion sort
    :param linked_list: linked list
    :param threshold: int number
    :return:
    """
    if linked_list.length() <= threshold:
        linked_list.insertion_sort()
        return linked_list

    else:
        list_tup = split_linked_list(linked_list)
        list1 = list_tup[0]
        list2 = list_tup[1]
        list1 = merge_sort(list1, threshold)
        list2 = merge_sort(list2, threshold)
        ret_list = merge(list1, list2)

    return ret_list


def split_linked_list(linked_list):
    """
    Intakes a linked list and splits it
    into two.
    :param linked_list: linked list
    :return: a tuple of two linked lists
    """
    length = linked_list.length()
    split_num = length/2
    ll1 = LinkedList()
    ll2 = LinkedList()

    count = 0 #keeps track of node

    while linked_list.is_empty() is False:
        val = linked_list.pop_front()
        count += 1
        if count <= split_num:
            ll1.push_back(val)
        else:
            ll2.push_back(val)

    return (ll1, ll2)



def merge(list1, list2):
    """
    Merges two sorted linked lists to one
    :param list1: sorted linked list
    :param list2: sorted linked list
    :return: sorted linked list
    """
    llnew = LinkedList()

    while (list1.is_empty() is False) and (list2.is_empty() is False):
        if list1.front_value() < list2.front_value():
            val = list1.pop_front()
        else:
            val = list2.pop_front()
        llnew.push_back(val)

    if list1.is_empty() is False:
        while list1.is_empty() is False:
            val = list1.pop_front()
            llnew.push_back(val)

    if list2.is_empty() is False:
        while list2.is_empty() is False:
            val = list2.pop_front()
            llnew.push_back(val)

    return llnew
