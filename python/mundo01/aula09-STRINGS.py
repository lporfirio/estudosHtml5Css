''' 
frase = 'Curso em Video Python'

len(frase) -- lenght
frase.count('o') -- contar
frase.find('deo') -- encontra a posição
'curso' in frase -- true or false

frase.replace('python', 'android')
frase.upper() -- transforma em maiúsculo
frase.lower() -- transorma em minísculo
frase.capitalize() -- só a primeira letra em maiuscula
frase.title() -- as primeiras letras das palabras em maiscula

frase = '   aprenda python  '

frase.strip() -- retira os espaços inúteis (começo e final de string)
frase.rstrip() -- retira os espaços somente do lado direito
frase.lstrip() -- retira os espaços somente do lado esquerdo

frase = 'Curso em Video Python'

frase.split() -- divide a string(pelos espaços ** padrão), gerando uma lista(array)
'-'.join(frase) -- une as strings.... ficaria Curso-em-Video-Python
 

inverter = frase[::-1] -- inverte a string

'''
frase = 'Curso em Video Python'
print(frase[3])
print(frase[3:])
print(frase[3:14])
print(frase[:21])
print(frase[1:15])
print(frase[1:15:3])

print("""Lorem ipsum dolor sit amet consectetur adipisicing elit. Non ut assumenda, aliquid doloremque tenetur dignissimos eius, ipsum vel voluptates earum beatae saepe quae, quaerat esse qui maiores ducimus eligendi nihil! Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus mollitia amet praesentium neque libero, iure soluta delectus veritatis itaque nobis quos quo explicabo quaerat numquam eligendi animi quia, at culpa?""")

print(frase.count('o'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))

dividido = (frase.split())
print(dividido)
junto = ' '.join(dividido)
print(junto)