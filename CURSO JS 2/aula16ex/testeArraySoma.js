let valores = []

valores.push(5)
valores.push(6)
valores.push(4)

console.log(valores)

/*
let soma = 0
soma = soma + valores[0]
soma = soma + valores[1]
soma = soma + valores[2]
*/

//----- parte da soma com for in ------ 

let soma = 0
for (let pos in valores) {
    soma = soma + valores[pos]
}





console.log(`somando todos os valores temos ${soma}`)