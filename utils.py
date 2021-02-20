import os


def clear():
    cls = 'cls' if os.name == 'nt' else 'clear'
    os.system(cls)


def header():
    print("******************************************************")
    print("\t\tEm um dia, que série melhor\n\t\t representa você")
    print("******************************************************")
