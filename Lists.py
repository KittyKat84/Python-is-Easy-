# Global variables

myUniqueList = []
myLeftOvers = []

# Function to add items to myUniqueList if item is not in the list
# and to add the repeat items to myLeftOvers list
def addToList(item):
    global myUniqueList
    if item not in myUniqueList:
        myUniqueList.append(item)
        return True
    else: 
        myLeftOvers.append(item)
        return False

# Test case

print(addToList("Karen"))
print(addToList("Leon"))
print(addToList("Clara"))
print(addToList("Tenica"))
print(addToList("Tobias"))
print(addToList("Karen"))
print(addToList("Clara"))
print(addToList("Leon"))
print(addToList("Riana"))
print(addToList("Marie"))

# Print the final result of both lists
print("This is my list: ", myUniqueList)
print ("This is my left overs: ", myLeftOvers)

