sum = (a, b) => {
    return a + b;
}

appendToJSON = (original, key, value) => {
    original[key] = value
    return original
}

randInt = (lower, upper) => {
    return Math.floor((Math.random() * upper) + lower);
}

const functions = {
    sum,
    appendToJSON,
    randInt
}

module.exports = functions;