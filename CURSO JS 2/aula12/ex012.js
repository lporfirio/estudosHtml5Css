var agora = new Date()
var hora = agora.getHours() 
var minutos = agora.getMinutes()
console.log(`agora são exatamente ${hora} horas e ${minutos} minutos`)

if (hora < 5) {
    console.log("boa madrugada")
}
else if (hora < 12) {
    console.log('bom dia!')
} else if (hora <= 18) {            // você pode criar quantos else if quiser!!!!
    console.log('boa tarde!')
} else if (hora < 24) {
    console.log('boa noite!')
}

