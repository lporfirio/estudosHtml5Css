function verificar(){
var data = new Date()
var ano = data.getFullYear()
var fano = document.getElementById('txtano')
var res = document.getElementById('res')
if (fano.value.length == 0 || Number(fano.value) > ano) {
    window.alert('[ERRO] Verifique os dados e tente novamente!')
} else {
    var fsex = document.getElementsByName('radsex')
    var idade = ano - Number(fano.value)
    //res.innerHTML = `Idade calculada: ${idade}`
    var genero = ''
    var img = document.createElement('img')
    img.setAttribute('id', 'foto')
    if (fsex[0].checked) {
        genero = 'Homem'
        res.style.color = 'green'
        if (idade >=0 && idade < 3) {
            //bebe
            img.setAttribute('src', 'foto-bebe-m.png')
        } else if (idade < 21) {
            //jovem
            img.setAttribute('src','foto-jovem-m.png')
        } else if (idade < 60) {
            //adulto
            img.setAttribute('src','foto-adulto-m.png')
        } else {
            //idoso
            img.setAttribute('src','foto-idoso-m.png')
        }
    } else if (fsex[1].checked) {
        genero = 'Mulher'
        res.style.color = 'purple'
        if (idade >=0 && idade < 3) {
            //bebe
            img.setAttribute('src', 'foto-bebe-f.png')
        } else if (idade < 21) {
            //jovem
            img.setAttribute('src', 'foto-jovem-f.png')
        } else if (idade < 61) {
            //adulto
            img.setAttribute('src', 'foto-adulto-f.png')
        } else {
            //idoso
            img.setAttribute('src', 'foto-idoso-f.png')
        }
    }
    res.style.textAlign = 'center'
    //res.style.color = 'green'
    res.innerHTML = `Detectamos ${genero} com ${idade} anos<p></p>`
    res.appendChild(img)
}
}