import random

#Initialising array
numArray = []
for i in range(0, 100):
    numArray.append(random.randint(0,100))
print("Random array")
print(numArray)

for i in range(0, len(numArray)):
    for j in range(0, len(numArray)):
        if (numArray[i] < numArray[j]):
            numArray.insert(j, numArray.pop(i))
    
print(numArray)