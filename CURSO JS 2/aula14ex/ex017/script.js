function gerart() {
    var numero = document.getElementById('txtnum')
    var res = document.getElementById('res')
    var tab = document.getElementById('seltab')

    if (numero.value.length == 0) {
        window.alert('Por favor, digite um número!')
    } else {
        let n = Number(numero.value)
        let c = 1 // contador
        tab.innerHTML = " "
        while (c <= 10) {
            let item = document.createElement('option')
            item.text = `${n} x ${c} = ${n*c}`
            item.value = `tab${c}`
            tab.appendChild(item)
            c++
        }
    }

}

