n = (input('Digite algo: '))
print('O tipo primitivo desse valor é: ', type(n))
print('Só tem espaços? ', n.isspace())
print('A coisa é númerica: ', n.isnumeric())
print('A coisa é alfabetica: ', n.isalpha())
print('É alfanúmerico? ', n.isalnum())
print('A coisa está em minusculo: ', n.islower())
print('A coisa está em maiusculo: ', n.isupper())
print('Está capitalizada? ', n.istitle())
