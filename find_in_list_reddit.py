names = ["Sally", "Tom", "Sameer", "Rishika", "Fernando", "Camilio"]

def main():
    search_value = input("Enter a name to search for in the array: ")

    try:
        search_index = [name.lower() for name in names].index(search_value.lower())
        print(f"That name was found at subscript {search_index}.")
    except ValueError:
        print("That name was not found in the array.")

    if input("Do you want to search again? (Y/N): ").lower() == "y":
        main()
