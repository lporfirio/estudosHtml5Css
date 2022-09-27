function verificar() {
    let fnum = document.getElementById('fnum')
    let ano = Number(fnum.value)
    let date = new Date
    let anoAtual = date.getFullYear()
    let idade = anoAtual - ano

    let res = document.getElementById('res')
    res.innerHTML = `${idade} anos de idade`

    if (ano == 0 || idade == anoAtual) {
        window.alert(`Digite um ano válido!`)
        res.innerHTML = `Coloque o ano de nascimento`
    } if (idade < 0) {
        res.innerHTML = `Vamos com calma, nem chegamos neste ano ainda!`
    } if (idade > 115 && idade != anoAtual) {
        res.innerHTML = `${idade} anos!!! Pessoa antiga, né? Que descanse em paz \u{1F64F}`
    }

    if (idade > 0 && idade <= 115) {
        let respostasex = document.getElementsByName('radsex')

        let imagem = document.createElement('img')
        imagem.setAttribute('id', 'foto')
        genero = ""
        if (respostasex[0].checked) {
            genero = 'homem'
            res.innerHTML = `Homem de ${idade} anos!`
            if (idade < 4) {
                res.innerHTML += ` Um bebê`
                imagem.setAttribute('src', 'foto-bebe-m.png')
            }
            else if (idade < 18) {
                res.innerHTML += ` Um jovem`
                imagem.setAttribute('src','foto-jovem-m.png')
            }
            else if (idade < 65) {
                res.innerHTML += " Um adulto"
                imagem.setAttribute('src','foto-adulto-m.png')
            } else {
                res.innerHTML += ' Um idoso'
                imagem.setAttribute('src','foto-idoso-m.png')
            }

        }

        else if (respostasex[1].checked) {
            genero = 'mulher'
            res.innerHTML = `Mulher de ${idade} anos!`
            if (idade < 4) {
                res.innerHTML += ` Uma bebê`
                imagem.setAttribute('src','foto-bebe-f.png')
            }
            else if (idade < 18) {
                res.innerHTML += ` Uma jovem`
                imagem.setAttribute('src','foto-jovem-f.png')
            }
            else if (idade < 65) {
                res.innerHTML += " Uma adulta"
                imagem.setAttribute('src','foto-adulto-f.png')
            } else {
                res.innerHTML += ' Uma idosa'
                imagem.setAttribute('src','foto-idoso-f.png')
            }
        }
        res.innerHTML += `<p></p>`
        res.appendChild(imagem)
    }

}