def return_letter(num_grade):
    letter_grade = {9: "A", 8: "B", 7: "C", 6: "D"}

    if num_grade == 100:
        return "A"
    return letter_grade.get(num_grade // 10, "F")


def main():
    while True:
        try:
            num_grade = int(
                user_input := input(
                    "Please enter grade as a whole number between 0 and 100: "
                )
            )
        except ValueError:
            print(f"'{user_input}' is not a valid whole number.")
            continue

        if num_grade in range(0, 101):
            break

        print(f"{num_grade} is outside of the requested range.")

    print(f"{num_grade} earns a letter grade of {return_letter(num_grade)}.")
