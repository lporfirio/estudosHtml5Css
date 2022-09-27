function contar() {
    let inicio = document.getElementById('txti')
    let fim = document.getElementById('txtf')
    let passo = document.getElementById('txtp')
    let res = document.getElementById('res')

    let i = Number(inicio.value)
    let f = Number(fim.value)
    let p = Number(passo.value)
    if (inicio.value.length == 0 || fim.value.length == 0 || passo.value.lenght == 0) {
        res.innerHTML = `Está faltando dados!!! \u{1F643}`

    } else {
        res.innerHTML = "contando... "
        if (p <= 0) {
            res.innerHTML = "o passo precisa ser maior que 1"
        }
        if (i < f) {
            let c = ""
            for (c = i; c < f; c += p) {
                res.innerHTML += `${c} \u{1F449} `
            }
        }
        if (i > f) {
            let c = ''
            for (c = i; c > f; c -= p) {
                res.innerHTML += `${c} \u{1F449} `
            }
        }
        res.innerHTML += `\u{1F3C1}`
    }
}