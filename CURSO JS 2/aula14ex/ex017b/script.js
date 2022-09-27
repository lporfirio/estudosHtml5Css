function tabuada() {
    let num = document.getElementById('txtn')
    let res = document.getElementById('res')
    let tabu = document.getElementById('tab')

    if (num.value.length == 0) {
        res.innerHTML = '<p></p>Por favor, digite um número!'
    } else {
        let n = Number(num.value)
        let c = 1  
        tabu.innerHTML = ""
        while (c <= 10) {
            let item = document.createElement('option')
            item.text = `${n} x ${c} = ${n*c}`
            tabu.appendChild(item)
            c++
        }
    }
}