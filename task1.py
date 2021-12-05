# Task 1
# A simple function.
# Create a simple function called favorite_movie,
# which takes a string containing the name of your favorite movie.
# The function should then print “My favorite movie is named {name}”.

# Завдання 1
# Проста функція.
# Створіть просту функцію під назвою favorite_movie, яка приймає рядок, що містить назву вашого улюбленого фільму.
# Потім функція має надрукувати «Мій улюблений фільм називається {ім’я}»

my_movie = input("Enter your favorite movie: ")


def favorite_movie(movie):
    print(f'Мій улюблений фільм називається {movie}')


favorite_movie(my_movie)