__author__ = 'brittnicarter'


# FUNCTION------
def welcome():
    print "Brittni's Pet Shop Mad Lib"
    firstname = raw_input("Enter your first name")
    lastname = raw_input("Enter your last name")
    print "Hello ", firstname, lastname, "Welcome to Brittni's Pet Shop"


# FUNCTION Mom gives us money----
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
food = dict()
food = {"Blue Buffalo": "Life Protection Form", "Simply Nourish": "Limited Ingredient Diet"}
print "Don't forget to pick up " + food["Blue Buffalo"] + " dog food for your new friend"

# CONDITIONAL STATEMENT toys----

extra = 25

if extra > 26:
    print "And you have enough extra money to get your pet a large Kong toy!"
elif extra > 24:
    print "And you have enough to get a small Kong toy!"
else:
    print "Save up for a few days and get a toy next time."
