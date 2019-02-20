"""
The algorithm is about writing a logic to implement jump search.

To implement it first, we have to look at how the jump search algorithm works:
- First we consider a list in a sorted manner.
- Next we find the square root of the total length of the list. This gives us the best value to implement jump search.
- We create slices of these small blocks in the list.
- We perform the operation that is present inside the function to figure out the index value of the search element.
"""

# Importing math module to calculate the square root of the length of the input list
import math


# Defining the function jump_search to find the index value by implementing jump search
def jump_search(input_list, search_element, length):

    # We find out the square root value to basically figure out how many blocks the list should be split into
    step = int(math.sqrt(length))

    # Initializing the starting position to consider the implementation of jump search
    start = 0

    # Calculating the total number of blocks that are supposed to be created to implement jump search
    block = length/step

    # Creating a for loop to jump in blocks of data. Each value of i obtained is the index position of the end of a
    # batch. Suppose if there were 16 elements in our input list, the total number of blocks will be 4. So we are
    # going to loop over every batch of data. This batch gets created by slicing the input list.
    for i in range(int(block)):

        # We are going to check if the search element is greater than the element present the end of the first block.
        # If the search element is greater, we add the step size to the start value to start the next batch of
        # data from the list.
        if search_element > input_list[step+start]:
            start += step

        # Here, we check if the value of the search element is same as the element that is present at the start
        # of the block. If the elements are same, then we return the index value. We are going to use the try and
        # except clause to handle the IndexError that we'd get if an element which is present is posted.
        try:
            if search_element == input_list[step + start]:
                return input_list.index(input_list[step + start])
        except IndexError:
            return -1

        # At last, we check if the search element is less than the element present at the end of the block. If its so
        # we check what is the index for the search element and return that value.
        if search_element < input_list[step+start]:
            for i in range(start, step+start):
                if search_element == input_list[i]:
                    return input_list.index(input_list[i])

# Taking the input list values to evaluate the function
input_list = list(map(int, input("Enter a list of elements as a string seperated by commas(,): \n").split(',')))
# Taking input for the search element
search_element = int(input("Enter a search element: "))

print(f"The search element is present at the index: {jump_search(input_list, search_element, len(input_list))}")
