print(
    "Enter the integers you want to average. To stop input, enter a blank line."
)
integers = []
while True:
    user_input = input("> ")
    if not user_input:
        break
    try:
        integers.append(int(user_input))
    except ValueError:
        print(f"Integer-value expected. User entered '{user_input}'.")

print(f"Values to average: {integers}")


"""
    Enter the integers you want to average. To stop input, enter a blank line.
    > 1
    > 4
    > 7
    > 3
    > u
    Integer-value expected. User entered 'u'.
    > d
    Integer-value expected. User entered 'd'.
    > 7
    > 4
    > 
    Values to average: [1, 4, 7, 3, 7, 4]
"""