
nome = 'Supermercados Plataforma 9 3/4'
print ('Obrigado pela preferência  {}{}{}'.format('\033[;31m', nome, '\033[m'))

ValorTotalCompras = float(input("valor total das compras: R$ "))
while True:
    DinheiroRecebido = float(input("Valor recebido: R$ "))
    if ValorTotalCompras > DinheiroRecebido:
        print('Valor recebido deve ser maior ou igual ao total das compras R${:.2f}'.format(ValorTotalCompras))
    else:
        break

troco = ValorTotalCompras - DinheiroRecebido
if troco <= 0:
    print ("Troco: R$ {:.2f}".format(abs(-troco)))

cedula = 0
valor = troco * -1
ValorCedulaAtual = 100

while True:
    if valor >= ValorCedulaAtual:
        valor -= ValorCedulaAtual
        cedula += 1
    else:
        if cedula > 0:
            if ValorCedulaAtual > 1:
                print ("{} Nota(s) de R$ {:.2f}".format(cedula, ValorCedulaAtual))
            elif ValorCedulaAtual <= 1:
                print ("{} Moeda(s) de R$ {:.2f}".format(cedula, ValorCedulaAtual))
        if ValorCedulaAtual == 100:
            ValorCedulaAtual = 50
        elif ValorCedulaAtual == 50:
            ValorCedulaAtual = 20
        elif ValorCedulaAtual == 20:
            ValorCedulaAtual = 10
        elif ValorCedulaAtual == 10:
            ValorCedulaAtual = 5
        elif ValorCedulaAtual == 5:
            ValorCedulaAtual = 2
        elif ValorCedulaAtual == 2:
            ValorCedulaAtual = 1
        elif ValorCedulaAtual == 1:
            ValorCedulaAtual = 0.50
        elif ValorCedulaAtual == 0.50:
            ValorCedulaAtual = 0.25
        elif ValorCedulaAtual == 0.25:
            ValorCedulaAtual = 0.10
        elif ValorCedulaAtual == 0.10:
            ValorCedulaAtual = 0.05
        elif ValorCedulaAtual == 0.05:
            ValorCedulaAtual = 0.01
        elif ValorCedulaAtual == 0.01:
            ValorCedulaAtual = 0            
        cedula = 0
        if valor == 0:
            break
        
