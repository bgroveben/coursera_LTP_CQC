# The problem we are tackling is a restaurant recommendation system.
# We are given a list of restaurants that contains:
# 1. The name of the restaurant.
# 2. The percentage of people who recommend that restaurant.
# 3. The price range of the restaurant.
# 4. the type of food served by the restaurant.
# The program will make a recommendation to the user based on this data.

#!# The Problem #!#
# Write a function that has three parameters:
# - a restaurant file that is open for reading,
# - the price range (0ne of $, $$, $$$, $$$$), and,
# - a list of cuisines.
# The function returns a list of restaurants in that price range, serving at least one of those cuisines,
# and their ratings sorted from highest to lowest.
"""
A restaurant recommendation system.

Here are some example dictionaries.
These dicts correspond to the information in restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str, list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str, list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we would produce the following list:

    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

# The file containing the restaurant data.
# FILENAME = 'restaurants_small.txt'
FILENAME = 'restaurants.txt'

def recommend(file, price, cuisines_list):
    """
    (file open for reading, str, list of str) -> list of [int, str] list

    Find restaurants in the file that correspond to price and that are tagged with any of the items in cuisines_list.
    Return a list of lists in the form [rating%, restaurant name] sorted by rating%.
    """

    # Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cuisine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)

    # Look for price or cuisines first?
    # Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]

    # Now we have a list of restaurants in the proper price range.
    # We need a new list of restaurants that serve one of the specified cuisines.
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    # Now we have a list of restaurants that are in the right price range and serve the requested cuisine.
    # We need to look at ratings and sort this list.
    result = build_rating_list(name_to_rating, names_final)

    # Return the sorted list and we're done.
    return list(reversed(sorted(result)))


def build_rating_list(name_to_rating, names_final):
    """
    (dict of {str: int}, list_of_str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name] sorted by rating%.

    >>> name_to_rating = {'Georgie Porgie': 87,
     'Queen St. Cafe': 82,
     'Dumplings R Us': 71,
     'Mexican Grill': 85,
     'Deep Fried Everything': 52}
    >>> names = ['Queen St. Cafe', 'Dumplings R Us']
    >>> build_rating_list(name_to_rating, names)
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """
    result = []
    for name, rating in name_to_rating.items():
        if name in names_final:
            result.append([rating, name])
    return result


def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """
    (list of str, dict of {str: list of str}, list of str) -> list of str

    Return a list of the restaurants in names_matching_price that serve at
    least one of the cuisines in cuisines_list according to cuisine_to_names.

    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = 'Canadian': ['Georgie Porgie'],
     'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
     'Malaysian': ['Queen St. Cafe'],
     'Thai': ['Queen St. Cafe'],
     'Chinese': ['Dumplings R Us'],
     'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    """
    result = []
    for cuisine in cuisines_list:
        for name in names_matching_price:
            if name in cuisine_to_names[cuisine]:
                result.append(name)
    return result


def read_restaurants(file):
    """
    (file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:
    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cuisine: list of restaurant names}
    """
    f = open(file, 'r')
    reviews = f.read().strip()
    restaurants = [entry.split('\n') for entry in reviews.split('\n\n')]
    f.close()

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}

    for name, rating, price, cuisine in restaurants:
        name_to_rating[name] = rating
        price_to_names[price].append(name)
        name_cuisine = [name, cuisine.split(',')]

        for item in name_cuisine[1]:
            if item in cuisine_to_names.keys():
                cuisine_to_names[item].append(name_cuisine[0])
            else:
                cuisine_to_names[item] = [name_cuisine[0]]

    return name_to_rating, price_to_names, cuisine_to_names


print(recommend(FILENAME, '$', ['Chinese', 'Thai',]))
print(recommend(FILENAME, '$$$', ['Canadian', 'Pub Food', 'Chinese']))
