var amigo = {
    nome: 'José',
    sexo: 'M',
    peso: 85.4,
    engordar(p=0){
        console.log('engordou')
        this.peso += p // this se refere ao objeto em questão
    }


}

//console.log(typeof amigo)
amigo.engordar(4)
console.log(`${amigo.nome} pesa ${amigo.peso}kg`)