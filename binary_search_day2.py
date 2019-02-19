def binary_search(input_list, search_element, length, start):

    if length >= start:
        mid = start + (length - start)/2
        input_list.sort()
        
        if search_element == input_list[int(mid)]:
            return f'The element is present at index {mid}'

        elif search_element > input_list[int(mid)]:
            return binary_search(input_list, search_element, mid - 1, start)

        else:
            return binary_search(input_list, search_element, length, mid+1)

    else:
        return -1

input_list = list(map(int, input("Enter a string of values seperated by a space: \n").split()))
search_element = int(input("Enter a search element: "))

print(binary_search(input_list, search_element, len(input_list)-1, 0))
