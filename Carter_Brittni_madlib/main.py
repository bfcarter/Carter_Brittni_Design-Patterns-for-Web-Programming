__author__ = 'brittnicarter'

def welcome():
    print "Hi, welcome to Brittni's Pet Shop Mad Lib"


#Mom gives us money-----
def calcTotal(m,y):
    total = m+y
    return total

t = calcTotal(100,400)
print "I have a total of " + str(t) + "dollars to buy a new pet"


budget = 500

if budget > 600:
    dog = "Puppy"
    print "Our dream has come true, we can buy a new puppy"
elif budget > 450:
    print "Can't get a puppy but at least we can get a rescue dog"
else:
    print "No dog today."


#For Each" LOOP Type of breed ----
breeds = ["Bulldog" "German Shepherd" "Labrador Retriever" "Boxer"]
for b in breeds:
    print "Your new dog will be " + b
