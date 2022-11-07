const a = (name) => {
    return `hello, ${name}`
}
console.log(a('ss'))

const numbers = [1,2,3,4,5]

const c = numbers.forEach((number) => {
    return number * 2
})
console.log(c) 

const d = numbers.map((number) => {
    return number * 2
})
console.log(d)