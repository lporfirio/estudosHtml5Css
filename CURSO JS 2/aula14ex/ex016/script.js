function contar() {

    var num1 = document.getElementById('txti')
    var num2 = document.getElementById('txtf')
    var num3 = document.getElementById('txtp')
    var res = document.getElementById('res')

    if (num1.value.length == 0 || num2.value.length == 0 || num3.value.length == 0) {
        res.innerHTML = `Impossível contar! \u{1F610} estão faltando dados!`
        //alert('Estão faltando dados!!!')

    } else {
        res.innerHTML = "Contando: <br>"
        var i = Number(num1.value)
        var f = Number(num2.value)
        var p = Number(num3.value)
        if (p <= 0) {
            res.innerHTML = `passo inválido! Considerando PASSO 1 <p></p>`
            p = 1
        }
        if (i < f) {
            //contagem crescente
            res.innerHTML += 'Subindo!!! <p></p> '
            for (let c = i; c <= f; c += p) {
                res.innerHTML += `${c} \u{1F449} ` // Para emojis  U+1F601 >>> \u{1F601} -- só funciona entre crases
            }
        }

        else {
            //contagem regressiva
            res.innerHTML += 'Descendo!!! <p></p> '
            for (let c = i; c >= f; c -= p) {
                res.innerHTML += `${c} \u{1F449} `
            }
        }
        res.innerHTML += `\u{1F3C1}`



    }
}








