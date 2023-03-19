MAX_DIGITS = 4

def palindrome_finder(max_num):
    count = 0
    for number in range(1, max_num + 1):
        num_digits = sum(number // 10 ** digit > 0 for digit in range(MAX_DIGITS))
        reversed = sum(
            number // 10 ** digit % 10 * 10 ** max(0, num_digits - digit - 1)
            for digit in range(MAX_DIGITS)
        )
        if reversed == number:
            count += 1
            print(reversed, end=("\n" if count % 10 == 0 else " "))

def palindrome_finder2(max_num):
    count = 0
    for num in range(1, max_num + 1):
        num_digits = 0
        while num // 10 ** num_digits:
            num_digits += 1
        reversed = sum(
            num // 10 ** digit % 10 * 10 ** (num_digits - digit - 1)
            for digit in range(num_digits)
        )
        if reversed == num:
            count += 1
            print(reversed, end=("\n" if count % 10 == 0 else " "))