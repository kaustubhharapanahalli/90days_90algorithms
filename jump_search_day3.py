import math

def jump_search(input_list, search_element, length):

    step = int(math.sqrt(length))
    previous = 0
    end = length/step

    index = 0
    for i in range(int(end)):
        # print(i)
        if search_element > input_list[step+previous]:
            previous += step

        if search_element == input_list[step + previous]:
            return input_list.index(input_list[step + previous])

        if search_element < input_list[step+previous]:
            for i in range(previous, step+previous):
                if search_element == input_list[i]:
                    return input_list.index(input_list[i])


input_list = list(map(int, input("Enter a list of elements as a string seperated by commas(,): \n").split(',')))
search_element = int(input("Enter a search element: "))

print(f"The search element is present at the index: {jump_search(input_list, search_element, len(input_list))}")
