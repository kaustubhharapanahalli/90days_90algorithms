# Function definition of linear search algorithm. The function takes in three parameters
# 1. The input list
# 2. The search element value
# 3. the length of the input list

def linear_search(input_list, search_element, length):

    # Looping over the index values of the list
    for i in range(0, length):
        # Checking if the input_list element is same as the search element
        if search_element == input_list[i]:
            # If the search element is same, return the index value which is stored in the variable 'i'
            return i
    # If in the for loop, none of the values in the list match the search element, then return -1
    return -1

# Taking the input values as a complete string and using the map method, convert the string into a map function and type cast it to return a list of integer values.
input_list = list(map(float, input("Enter elements of the list seperated by a space: \n").split()))
# Taking the input value of the search element.
search_element = float(input("Enter the search element: "))
# Calculating the length of the input list
length = len(input_list)

# Printing the output state of the returned value from the function.
print(linear_search(input_list=input_list, search_element=search_element, length=length))
