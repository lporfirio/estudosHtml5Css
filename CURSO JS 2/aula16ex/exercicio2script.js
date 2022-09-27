let num = document.getElementById('fnum')
let sel = document.querySelector('select#sel')
let res = document.getElementById('res')
let valores = []

function isNumero(n) {
    if (Number(n) > 0 && Number(n) < 101) {
        return true
    } else {
        return false
    }
}

function isLista(n, l) {
    if (l.indexOf(Number(n)) != -1) {
        return true
    } else {
        return false
    }

}

function adicionar() {
    if (isNumero(num.value) && !isLista(num.value, valores)) {
        valores.push(Number(num.value))
        let item = document.createElement('option')
        sel.appendChild(item) // adicionando 'option' no 'select'
        item.text = `valor de ${num.value} adicionado`
        res.innerHTML = 'Pode adicionar mais números, se quiser!'

    } else {
        window.alert('Número inválido!')
    }
    num.value = ''
    num.focus()

}
/* valores é uma ARRAY 
total de números cadastrados
maior valor informado
menor valor informado
soma dos valores
a média dos valores
*/
function finalizar() {
    if (valores.length == 0) {
        window.alert('Adicione algum número antes de finalizar!')
    } else {
        let total = valores.length
        let maior = valores[0]
        let menor = valores[0]
        let soma = 0
        let media = 0
        
        for (let pos in valores) {
            soma = soma + valores[pos]
            if (valores[pos] > maior) {
                maior = valores[pos]
            }
            if (valores[pos] < menor) {
                menor = valores[pos]
            }
        }
        media = soma / total


        res.innerHTML = `temos um total de ${total} números cadastrados<p></p>`
        res.innerHTML += `o maior número na lista é ${maior}<p></p>`
        res.innerHTML += `o menor número na lista é ${menor}<p></p>`
        res.innerHTML += `a soma dos números é ${soma}<p></p>`
        res.innerHTML += `a média dos números é ${media}<p></p>`
    }

}