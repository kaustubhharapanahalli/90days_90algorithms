def linear_search(input_list, search_element, length):
    for i in range(0, length):
        if search_element == input_list[i]:
            return i
    return -1

input_list = list(map(int, input("Enter elements of the list seperated by a space: \n").split()))
search_element = int(input("Enter the search element: "))
length = len(input_list)

print(linear_search(input_list=input_list, search_element=search_element, length=length))
