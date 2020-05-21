
numArray = [];
for (let i = 0; i < 100; i++) {
    numArray.push(Math.floor(Math.random() * Math.floor(100)));
}
console.log(numArray)

for (let i = 0; i < numArray.length; i++) {
    for (let j = 0; j < numArray.length; j++) {
        if (j + 1 < numArray.length) {
            if (numArray[j] > numArray[j+1]) {
                temp = numArray[j]
                numArray[j] = numArray[j+1]
                numArray[j+1] = temp
            }
        }
    }
}
console.log(numArray)