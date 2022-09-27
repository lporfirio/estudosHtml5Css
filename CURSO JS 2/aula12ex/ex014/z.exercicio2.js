function carregar() {

    let data = new Date
    let horas = data.getHours()
    let minutos = data.getMinutes()
    let mostrador = document.getElementById('mostrador')
    let imagem = document.getElementById('imagem')


    mostrador.innerHTML = `Agora são ${horas} horas e ${minutos} minutos. `

    if (horas >= 4 && horas < 12) {
        mostrador.innerHTML += `Bom dia!`
        imagem.src = 'fotomanha.png'
        document.body.style.background = '#ed8e3b'
    }
    if (horas >= 12 && horas < 18) {
        mostrador.innerHTML += `Boa tarde!`
        imagem.src = 'fototarde.png'
        document.body.style.background = '#da7c63'
    }
    if (horas >= 18 || horas < 4) {
        mostrador.innerHTML += `Boa noite!`
        imagem.src = 'fotonoite.png'
        document.body.style.background = '#092437'
    }


}