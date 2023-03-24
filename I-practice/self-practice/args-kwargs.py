def sample_function(a, x, z, *args, **kwargs):
    print("\nStandard arguments:", a, x, z, end="\n\n")
    print(f"Args arguments: {args}", end="\n\n")
    print(f"Kwargs arguments: {kwargs.items()}", end="\n\n")
    print(f"Length of args: {len(args)}", end="\n\n")
    print(f"Length of kwargs: {len(kwargs)}", end="\n\n")
    for num, a in enumerate(args):
        print(num, ")", a)
    print()
    for k, v in kwargs.items():
        print("Key: ", k)
        print("Vale: ", v)


sample_function(1, 2, 3,  5, 6, 6, "kot", "noga", "boli", "pstro", d=8, g="dupa", h="samolot")


