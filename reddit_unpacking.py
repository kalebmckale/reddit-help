def f(lst):
    for x, y, z in map(lambda tup: [*tup, *((3 - len(tup))*[None])], lst):
        print(f"lst: {lst}")
        print(f"x: {x}")
        print(f"y: {y}")
        print(f"z: {z}")