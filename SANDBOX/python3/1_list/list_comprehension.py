'''
https://www.youtube.com/watch?v=AhSvKGTh28Q&t=19s
'''
# list of squares without list comprehension
my_squares = []
for i in range(1, 101):
    my_squares.append(i ** 2)
print(my_squares)

# list of squares using list comprehension
squares_list_comprehension = [i ** 2 for i in range(1, 101)]
print(squares_list_comprehension)

print()

# list remainder of squares
my_remainders_mod5 = []
for i in range(1, 101):
    my_remainders_mod5.append(i ** 2 % 5)
print(my_remainders_mod5)

# list remainder of squares using list comprehension
remainders_mod5_list_comprehension = [i ** 2 % 5 for i in range(1, 101)]
print(remainders_mod5_list_comprehension)

print()

# if statements without list comprehension
movies = ['Jurassic Park', 'Jaws', 'Psycho', 'Scream', 'I know what you did last summer', 'Fluber']
filtered_movie = []
for movie in movies:
    if movie.startswith('J'):
        filtered_movie.append(movie)
print(filtered_movie)

filtered_movie_lc = [movie for movie in movies if movie.startswith('J')]
print(filtered_movie_lc)

print()

# filtered tuple movies
movie_by_year = [('Lord of the rings', 2001), ('Spirited Away', 2001), ('The Aviator', 2004), ('Gattaca', 1997), ]
movie_selected = [movie for (movie, year) in movie_by_year if year < 2004]
print(movie_selected)

print()

# scalar multiplication using list comprehension
v = [2, -3, 1]
#product = v * 4
product = [4 * number for number in v]
print(product)

