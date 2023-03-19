my_dict = dict(zip(range(100), map(str, range(100))))

%timeit v = [val for val in my_dict.values()]
%timeit v = [val for key, val in my_dict.items()]
