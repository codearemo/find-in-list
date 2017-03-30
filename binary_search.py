def binary_search(my_list, search_item):
    #Divides the list into two eqaul lists
    half_the_list = int(len(my_list)/2)
    
    if half_the_list % 2 == 0:
        #Get the centre item needed to use for comparing search_item
        middle_item = my_list[half_the_list + 1]
        #Getting the index of the centre item
        middle_index = my_list.index(middle_item)
        
        if middle_item > search_item:
            new_list1 = my_list[:(middle_index + 1)]
            binary_search(new_list1, search_item)
            
        elif middle_item < search_item:
            new_list1 = my_list[middle_index :]
            binary_search(new_list1, search_item)
        else:
            print (search_item, "Found")
            

    else:
        middle_item = my_list[half_the_list + 1]
        middle_index = my_list.index(middle_item)
        if middle_item > search_item:
            new_list2 = my_list[:(middle_index + 1)]
            binary_search(new_list2, search_item)

        elif middle_item < search_item:
            new_list2 = my_list[middle_item :]
            binary_search(new_list2, search_item)
        else:
            print (search_item, "Found")
