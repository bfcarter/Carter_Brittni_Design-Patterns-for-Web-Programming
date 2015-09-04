__author__ = 'brittnicarter'

def welcome():
    print "Brittni's Pet Shop Mad Lib"

def name():
    name = raw_input("Enter your name")
    print "Hello ", name, "welcome to Brittni's Pet Shop"


# FUNCTION Mom gives us money-----
def calcTotal(m,y):
    total = m+y
    return total

t = calcTotal(100,400)
print "You have a total of " + str(t) + " dollars to buy a new pet"

# CONDITIONAL STATEMENT budget-----

budget = 500

if budget > 600:
    dog = "Puppy"
    print "Our dream has come true, we can buy a new puppy"
elif budget > 450:
    print "You can't get a puppy but at least we can get a rescue dog"
else:
    print "No dog today."


# For Each" LOOP Type of breed ----
breeds = ["Bulldog", "German Shepherd", "Labrador Retriever", "Boxer"]
for b in breeds:
    print "One of your choices for a new dog will be " + b


food = dict() # dictionary----------
food = {"Blue Buffalo":"Life Protection Form","Simply Nourish":"Limited Ingredient Diet" }
print "Don't forget to pick up " + food["Blue Buffalo"] + " dog food for your new friend"

