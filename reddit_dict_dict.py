"""
Performing specific operation on individual keys in dictionary with list values

I have a dictionary, and for each key in the dictionary I have a list of lists of values. I want to edit all the values (every value in the list of lists) for each individual key. I am performing division based on the values in another dictionary with the same keys. 

    for key in new_vec:
        for jey in result_two:
            if key == jey:
                new_vec[key] = new_vec[key] / result_two[jey]
                #for list1 in new_vec[key]:
                    #for number in list1:
                        #print(number)
                        #number = number / result_two[jey]

When I try the first solution, I get extremely small numbers, which makes me think that result_two[jey] is being continuously divided in each iteration of the for loop. When I try the commented out code, the values do not become modified at all for some reason. Thanks in advance.
"""

for key, val in new_vec.items():
    val /= result_two[key]
    #for new_vec_list in val:
        #for number in new_vec_list:
            #print(number)
            #number /= number / result_two[key]
