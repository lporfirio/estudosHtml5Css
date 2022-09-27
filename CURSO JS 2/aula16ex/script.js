let num = document.querySelector('input#fnum')
let lista = document.querySelector('select#flista')
let res = document.querySelector('div#res')
let valores = []


function isNumero(n) {
    if (Number(n) >= 1 && Number(n) <= 100) {
        return true
    } else {
        return false
    }
}

function inLista(n, l) {
    if (l.indexOf(Number(n)) != -1) {
        return true
    } else {
        return false
    }
}

function adicionar() {
    if (isNumero(num.value) && !inLista(num.value, valores)) { /* 
    só vai adicionar se 'num' for um número válido e se 'num' não estiver na lista
*/
        valores.push(Number(num.value))
        let item = document.createElement('option')
        item.text = `valor ${num.value} adicionado`
        lista.appendChild(item) // para adicionar 'option' no 'select'
        res.innerHTML = ''       // quando adicionar o elemento, limpará o resultado
    } else {
        window.alert('valor inválido ou já encontrado na lista')
    }
    num.value = ''
    num.focus()
}

function finalizar() {
    if (valores.length == 0) {
        window.alert('adicione valores antes de finalizar')
    } else {
        let total = valores.length // valor total de elementos da array
        let maior = valores[0]
        let menor = valores[0]
        let soma = 0
        let media = 0 

        for (let pos in valores) {
            soma = soma + valores[pos]
            if (valores[pos] > maior) { maior = valores[pos] }
            if (valores[pos] < menor) { menor = valores[pos] }
        }

        media = soma / total

        res.innerHTML = ''
        res.innerHTML += `<p>ao todo temos ${total} números cadastrados</p>`
        res.innerHTML += `<p>o maior valor informado foi ${maior}</p>`
        res.innerHTML += `<p>o menor valor informado foi ${menor}</p>`
        res.innerHTML += `<p>somando todos os valore, temos ${soma}</p>`
        res.innerHTML += `<p>a média de todos os valores é ${media}</p> `
    }
}