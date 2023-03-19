states_data = [
    {
        "State": "Alabama",
        "Capital": "Montgomery",
        "State Flower": "Camellia",
        "Population": 4887680,
    },
    {
        "State": "Foobar",
        "Capital": "Helloworld",
        "State Flower": "Anyothername Rose",
        "Population": 424242,
    },
]

def update_states_data(states_data):
    return {
        state["State"]: {key: value for key, value in state.items() if key != "State"}
        for state in states_data
    }

def update_population(state):
    try:
        state.update(
            Population=int(user_input := input("Please enter the updated population of {state}"))
        )
    except ValueError:
        print(f"Population must be a positive integer: '{user_input}' given.")


def main():
    # ... other code ...

    # Reformat states_data object from outer list to outer dict
    states_data = update_states_data(states_data)

    # ... other code ...

    # User is updating population
    state = input("Please enter the state to modify:   ").capitalize()
    try:
        update_population(states_data[state])
    except KeyError:
        print(f"{state} is not a valid state entry.")
