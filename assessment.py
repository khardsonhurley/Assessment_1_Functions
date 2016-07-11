# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def tax_calculator(state,cost,tax = .05):
    """Calculates total cost of item including tax. 

    The default tax percentage is set to 5%. If the person enters "CA"
    for California, it will automatically calculate the tax at 7%.
    Note: User should enter tax as a decimal value."""

    if state == "CA":
        cost = float(cost) + float(cost) * .07
    else:
        cost = float(cost) + float(cost) * float(tax)

    return "Total cost with tax: $" + str(cost)


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def is_berry(fruit_name):
    """Checks if input is "strawberry", "cherry", or "blackberry."

    Returns boolean value of "True" if the input matches. 
    Returns boolean value of "false" if not.
    Also considered if the user inputs all capitals, 
    by changing all caracters to lower before checking."""

    if fruit_name.lower() == "strawberry":
        return True
    elif fruit_name.lower() == "cherry":
        return True
    elif fruit_name.lower() == "blackberry":
        return True
    else:
        return False

def shipping_cost(fruit_name):
    """Determines shipping costs of berrys. 

    Takes in fruit name, uses is_berry function to verify if it is a berry. 
    If it is a berry, shipping cost is 0. If not, shipping cost is 5"""

    if is_berry(fruit_name) == True: 
        return "0"
    else:
        return "5"

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def is_hometown(town):
    """Determines if the town entered is San Diego. 

    Returns True if it is, and False if not."""

    if town.lower() == "san diego":
        return True
    else: 
        return False

def full_name(first,last):
    """Takes in first and last name and prints as one string."""

    first = first.lower()
    last = last.lower()
    return first[0].upper() + first[1:] + " " + last[0].upper() + last[1:]



def hometown_greeting(town,first,last):
    """ Gives a special greeting if the person is from my town.

    If is_hometown returns True, I tell the user we are from the same place!
    If is_hometown returns False, I ask the user where they are from!"""

    if is_hometown(town) == True: 
        print "Hi {}, we're from the same place!".format(full_name(first,last))
    else: 
        print "Hi {}, where are you from?".format(full_name(first,last))


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


def increment(x = 1):
    """Practicing inner functions

    Not quite sure how this works, followed examples found online."""

    def add(y):
        return int(x) + int(y)
    return add

addfive = increment(5) ### Really not sure how this works. 

addfive(5) #This prints 10. Which means it did 5 + 5. HOW???
addfive(20) #This prints 25. Which means it did 20 + 5. HOW??


def add_new_number(int1,list1):
    """Adds a new number to the given list"""

    list1.append(int1)

    return list1



#####################################################################