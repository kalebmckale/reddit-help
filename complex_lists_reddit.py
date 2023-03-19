# assuming var is a list, where len(var) == len(mylist)
#mylist = [[item] for item in var]
# assuming len(num) == len(mylist) and num is a list of lists
#for index, sublist in enumerate(num):
#    mylist[index].extend(sublist)
    
var = [0, 1, 2]
num = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

print(list(map(list, zip(var, *num))))

mylist = list(map(list, zip(var, *num)))