
function fib(number) {
    if (number > 1) {
        current = 1
        previous = 1
    }
    else {
        return 1
    }
    let next = 0
    for (let i = 0; i < number; i ++) {
        next = current + previous
        previous = current
        current = next
    }
    return next
}

console.log(fib(10000))
