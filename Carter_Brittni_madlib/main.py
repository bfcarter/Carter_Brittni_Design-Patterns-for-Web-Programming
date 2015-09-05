__author__ = 'brittnicarter'


# FUNCTION welcome------
def welcome():
    print "Brittni's Pet Shop Mad Lib"

firstname = raw_input("Enter your first name")
lastname = raw_input("Enter your last name")
print "Hello ", firstname, lastname, "Welcome to Brittni's Pet Shop"


# FUNCTION Mathematical Operation Mom gives us money----


def calcTotal(m, y):
    total = m + y
    return total


t = calcTotal(100, 400)
print "You have a total of " + str(t) + " dollars to buy a new pet"

# CONDITIONAL STATEMENT funds-----

funds = 500

if funds > 600:
    print "Our dream has come true, we can buy a new puppy"
elif funds > 450:
    print "You can't get a puppy but at least we can get a rescue dog"
else:
    print "No dog today."


# For Each" LOOP Type of breed ----
breeds = ["Bulldog", "German Shepherd", "Labrador Retriever", "Boxer"]
for b in breeds:
    print "One of your choices for a new dog will be " + b

# dictionary----------
bags = raw_input("Enter a number")

food = dict()
food = {"Blue Buffalo": "Life Protection Form", "Simply Nourish": "Limited Ingredient Diet"}
print "Don't forget to pick up " + bags + food["Blue Buffalo"] + " dog food for your new friend"

# Mathematical Operation Pet Insurance----

def calcInsure (m, p):
    total = m * p
    return total
t = calcInsure(12, 20)
print "It is requested that you get your new friend pet insurance, it will cost " + "$" + str(t) + " for 12 months"



# CONDITIONAL STATEMENT toys----

extra = 25

if extra > 26:
    print "And you have enough extra money to get your pet a large Kong toy!"
elif extra > 24:
    print "And you have enough to get a small Kong toy!"
else:
    print "Save up for a few days and get a toy next time."

# ARRAY dog name------

name = ["Ziggy", "Esther", "Linc", "Diamond"]
print "Your new dog will be named", name [1]


# dogs age----

age = raw_input("Enter a number between 1-10")
print "Your new dog is " + str(age)

# color of bow----

color = raw_input("Enter a color")
print "Our pet shop has even you a FREE " + color + " hair bow!"

print "Enjoy your new best friend!"
