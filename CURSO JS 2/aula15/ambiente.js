let num = [5, 8, 9, 3]
num[4] = 7
num.push(6) // MÉTODO para acrescentar valores no array
num.length // para descobrir quantos elementos tem no array

console.log(`nosso vetor é o ${num}`)
console.log(`número de elementos é ${num.length}`)
console.log(`o primeiro valor do vetor é ${num[0]}`)

num.sort() // sort() coloca os valores do vetor em ordem crescente
console.log(num)
0
let pos = 0 // pos = posição
for (let pos = 0; pos < num.length; pos++) {
    console.log(num[pos])
}
var space = ""
console.log(space)
console.log(num)

let pos1 = num.indexOf(8) /* indexOf() busca um valor no vetor..... 
caso não seja encontrado, será igual a -1
*/

if (pos1 == -1) {
    console.log(`o valor não foi encontrado!`)
} else {
    console.log(`o valor 8 está na posição ${pos1}`)
}