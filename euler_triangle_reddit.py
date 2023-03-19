with open("triangle.txt") as file:
    rows = file.read().strip().split("\n")

data = [[int(num) for num in row.split()] for row in rows]


x = 2
if x == 2:
    print("The number is 2.")
if x % 2 == 0:
    print("The number is even.")
if x % 2 != 0:
    print("The number is odd.")