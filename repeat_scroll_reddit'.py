string = "Carpe Diem"
max_length = 19
num_repeats = round(max_length / len(string))
longer_string = " ".join(string for _ in range(num_repeats))
print(longer_string)


''