movies =[
    {"name": "the matrix", "Director":"wachowski"},
    {"name":"A Beautiful Day in the neighbood", "director":"Heller"},
    {"name":"The Irishman", "director": "Scorsese"},
    {"name": "klaus", "director": "pablos"},
    {"name":"1917", "director":"mendes"}
]


def find_movie(expected,finder):
    for movie in movies:
        if finder(movie) == expected:
            return movie


find_by = input("what property are we searching by ")
searching_by = input("what are you looking for? ")
movie2 = find_movie(searching_by,lambda movie: movie[find_by])
print(movie2 or "No movies found")