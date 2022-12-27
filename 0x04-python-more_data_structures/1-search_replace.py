def search_replace(my_list, search, replace):
    replaced_list = [0 for _ in range(len(my_list))]
    for i in range(len(my_list)):
        if my_list[i] == search:
            replaced_list[i] = replace
        else:
            replaced_list[i] = my_list[i]
    return replaced_list
