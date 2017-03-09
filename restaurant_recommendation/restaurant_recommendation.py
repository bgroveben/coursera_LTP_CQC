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
