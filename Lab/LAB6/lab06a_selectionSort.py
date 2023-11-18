'''
Nama    : Andrew Devito Aryo
NPM     : 2306152494
Kelas   : C
Asdos   : GAN

Program to Selection-Sort a Prompted List from User
'''
# ***********************
# lab06a_selectionSort.py
#
# Sorting a list of numbers using the Recursive-Selection-Sort Algorithm
# ***********************
##
# Given a list of integers, this program
# sorts the list using the recursive selection sort algorithm.
#
## minIndex(): finds the smallest element in a tail range of a list.
# @param lst: the list to sort
# @param startIndex: the first position in lst to compare
# @return the position of the smallest element in the
# range lst[startIndex] . . . lst[len(lst) - 1]
#

# Function that returns the index of the lowest value of a list
def minIndex(lst, startIndex):
    # base case: only one element to consider
    if startIndex == len(lst) - 1:
        return startIndex
    
    # Find the minimum of remaining elements recursively
    k = minIndex(lst, startIndex + 1)

    # Return the minimum of all
    if lst[startIndex] < lst[k]:
        return startIndex
    else:
        return k
    
## selection_sort( ):
# sorts a list in place, using selection sort recursively.
# @param lst: the list to sort
# @param startIndex: the index of starting element
#

def selection_sort(lst, startIndex=0):
    n = len(lst)
    # when starting index and size of list are the same, return;
    # because there is nothing to sort
    if startIndex == len(lst): return
    # find the index of minimum element
    # from startIndex to the end
    k = minIndex(lst, startIndex)

    # Swapping the corresponding elements
    # when the found index and the current minimum
    # index are not the same
    if k != startIndex:
        lst[k], lst[startIndex] = lst[startIndex], lst[k]

    # Recursively calling selection sort function for the
    # remaining elements
    selection_sort(lst, startIndex + 1)
    # return lst


## main():
# demonstrates the selection sort algorithm by sorting a
# list of integers given by user
def main():
    input_string = input("Type a sequence of numbers (example: 3,100,-5,3): \n")
    if input_string == "":
        values = []
    else:
        values = input_string.split(",")
    #change each element from str to int
    values = [int(i) for i in values]

    print(f"\nInput List:\n{values}")
    selection_sort(values)
    print(f"Sorted List:\n{values}")
if __name__ == '__main__':
    main()