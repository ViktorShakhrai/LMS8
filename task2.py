# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those two,
# with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary to make sure that it works as intended.

# Створення словника.
# Створіть функцію make_country, яка приймає назву країни та столицю як параметри.
# Потім створіть словник із цих двох із «назва» як ключ і «капітал» як параметр.
# Зробіть так, щоб функція друкувала значення словника,
# щоб переконатися, що вона працює належним чином.

country = input("Enter name country: ")
capital = input('Enter name capital this country: ')


def make_country(country_name, country_capital):
    country_info = {country_name: country_capital}
    print(country_info)


make_country(country_capital=capital,country_name=country)