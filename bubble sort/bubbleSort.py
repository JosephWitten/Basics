import random

#Initialising array
numArray = []
for i in range(0, 100):
    numArray.append(random.randint(0,100))
print("Random array")
print(numArray)

#sort
for i in range(0, len(numArray)):
    for j in range(0, len(numArray)):
        if(j+1 < len(numArray)):
            if (numArray[j] > numArray[j+1]):
                temp = numArray[j]
                numArray[j] = numArray[j+1]
                numArray[j+1] = temp

print("Sorted array")
print(numArray)