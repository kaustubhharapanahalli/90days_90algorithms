"""
This program is a generalized program for binary search.
The generalization is on taking user input even for the list of values, also asking for the input of the search element.

This code can be even more generalized by checking condition if we had to take input from the users or from the system
input. But it's not implemented here.
"""

# Function definition takes 4 parameters as input. The parameters are:
# 1. input list
# 2. search element
# 3. length of the complete list
# 4. the starting point for the binary search
def binary_search(input_list, search_element, length, start):

    # sorting the input list in ascending order.
    input_list.sort()

    # First, we check if the list contains only one element or not. If the list contains only one element, then that index
    # value will become the search element index value. If it's greater, we go ahead and perform binary search to get the index
    # value of the search element.
    if length >= start:

        # The middle index value is figured out from the formula below. It's a generalized formula that helps in finding the
        # middle index value of each binary search
        mid = start + (length - start)/2

        # We check if the middle element in the given list is same as the search element
        if search_element == input_list[int(mid)]:
            # If the search element value and the middle value matches, the following sentence is returned.
            return f'The element is present at index {int(mid)}'

        # Else, it checks if the search element value is greater than the middle value. If it's greater, it performs the
        # following action where the index position of the starting element changes to the next index which is greater than
        # the middle index value of the actual list
        elif search_element > input_list[int(mid)]:
            return binary_search(input_list, search_element, mid + 1 , start)

        # If the search element value is lesser than the mid index value, then the end index of the next input list is
        # reduced to a value less than the mid value, by subtracting mid index value by 1.
        else:
            return binary_search(input_list, search_element, length, mid-1)

    # These steps are repeated until the index value is found out. If the search element is not found, then we return the value
    # -1
    else:
        return -1

# Taking the input list as a string and convering it to a list and then taking the search element input.
input_list = list(map(int, input("Enter a string of values seperated by a space: \n").split()))
search_element = int(input("Enter a search element: "))

# Calling the function to perform Binary Search
print(binary_search(input_list, search_element, len(input_list)-1, 0))
