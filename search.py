# Searches for the index of the given element and outputs each time it appears
# This algorithm is viable for both lists and strings
# This algorithm is also viable for substrings, so elements that have a length greater than one
# Returns a list of the indices in which the element appears in
def search(stored, element):
    count_element = 0
    returned = ""
    indices = ""
    i = 0
    while i < len(stored):
        if type(stored) == list:
            if stored[i] == element:
                indices += f"{i}, "
                count_element += 1
        elif type(stored) == str:
            if stored[i:i+len(element)] == element:
                indices += f"{i}, "
                i = (i + len(element) - 1)
                count_element += 1
        i += 1
    if indices == "":
        indices = None

    else:
        if indices[len(indices) - 2: ] == ", ":
            index = [indices[i] for i in range(len(indices)) if i < len(indices) - 2]
            mapped = list(map(str, index))
            for i in range(len(mapped)):
                returned += mapped[i]
            print(f"'{element}' found at indices: {returned}")
        else:
            print(f"'{element}' found at indices: {indices}")

    if count_element == 1:
        print(f"{element} appeared 1 time. ")
    else:
        print(f"'{element}' appeared {count_element} times. ")

    if indices != None:
        # Removes whitespace and commas and converts the indices to type integer then stores them in a list
        index_lst = indices.split(",")
        index_lst.remove(" ")
        map_ = list(map(int, index_lst))
        return map_
    return None

def linear_in(outer, inner):
    in_out = False
    #for i in range(len(outer)):
    for x in range(len(inner)):
        if inner[x] in outer:
            in_out = True
        else:
            in_out = False
    return in_out

print(linear_in(outer=[1,2,6], inner=[4]))

