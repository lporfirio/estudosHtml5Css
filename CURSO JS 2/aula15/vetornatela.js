let valores = [8, 1, 7, 4, 2, 9]

console.log(valores)

console.log(valores[0])
console.log(valores[1])
console.log(valores[2])
console.log(valores[3])
console.log(valores[4])
console.log(valores[5])

 for(let pos=0; pos<valores.length; pos=pos+1) {
    console.log(`a posição ${pos} tem o valor ${valores[pos]}`)
}

let space = ""
console.log(space)
console.log(space)

//************/

for (let pos in valores) { // para cada posição em num
    console.log(`a posição ${pos} tem o valor ${valores[pos]}`)
}