moms =[
        ("jane", "jude"),
        ("jovia", "Oprah"),
        ("jenny", "Jesca")
    ]

kid_name = input("please enter kid's name ")


def find_moms():

    for mom, kid in moms:
        if kid_name == kid:
            return mom
    return "Kid doesnt exist"


find_m = find_moms()
print(find_m)

