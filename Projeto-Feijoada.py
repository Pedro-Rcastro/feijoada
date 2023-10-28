#Exercício 3 de 4 aula prática

#Inicio da função volumeFeijoada()
def volumeFeijoada():
  print('-------------------Menu de 1 de 3 - volume feijoada--------------------')
  while True:
    try:
      volumeF = int(input('Digite a quantidade desejada (ml): '))
      if(volumeF >= 300) and (volumeF <= 5000):# if 300 <= volumeF <= 5000
        return volumeF * 0.08
      else:
        print('Pare de digitar valores abaixo de 300 e acima de 5000.')
    except ValueError:#caso usuário digite uma letra por exemplo
      print('Pare de digitar números não inteiros')
#Fim da função volumeFeijoada()

#Inicio da função opçãoFeijoada()
def opçãoFeijoada():
  print('-------------------Menu de 2 de 3 - opção feijoada--------------------')
  while True:
    opçãoF = input('Qual opção de feijoada deseja \n'+
                   'b - Básica(Feijão + paiol + costelinha) \n'  +
                   'p - Prémio(Feijão + paiol + costelinha + partes de porco) \n'  +
                   's - suprema(Feijão + paio + costelinha + partes de porco + charque + calabresa + bacon)'    +
                   '  >>')
    opçãoF = opçãoF.lower()#trata maiúsculas
    opçãoF = opçãoF.strip()#trata espeço digitado
    if opçãoF == 'b':
      return  1.00
    elif opçãoF == 'p':
      return  1.25
    elif opçãoF == 's':
      return  1.50
    else:
      print('Pare de digita opções dierentes de b,p,s')
    continue# se cair nesse aqui volte para o inicio do laço
#Fim da função opçãoFeijoada()

#Inicio da função acompanhamentoFeijoada()
def acompanhamentoFeijoada():
  print('-------------------Menu de 3 de 3 - acompanhamento feijoada--------------------')
  acumulador = 0
  while True:
    acompanhamentoF = input('Deseja mais algum adicional?:\n' +
                          '0 - Não desejo mais acompanhamento(Encerrar pedido) \n' +
                          '1 - 200g de aroz \n' +
                          '2 - 150g de faroa especial \n'  +
                          '3 - 100g de couve cozido \n'  +
                          '4 - 1 laranja descascada \n'   +
                          '  >>')
    if acompanhamentoF == '0':
      return acumulador # aqui é o único pois não quero mais que repita

    elif acompanhamentoF == '1':
      acumulador = acumulador +5
      continue#volta para o inicio do while True desse laço

    elif acompanhamentoF == '2':
      acumulador = acumulador +6
      continue#volta para o inicio do while True desse laço

    elif acompanhamentoF == '3':
      acumulador = acumulador +7
      continue#volta para o inicio do while True desse laço

    elif acompanhamentoF == '4':
      acumulador = acumulador +3
      continue#volta para o inicio do while True desse laço

    else:
      print('Pare de digita opções diferentes de 0/1/2/3/4!')
#Fim da função acompanhamentoFeijoada()

#Inicio Main
print('------------bem-vindo ao programa de feijoada de Pedro Rogério de O. Castro RU 4505802------------')
volume = volumeFeijoada()
opção = opçãoFeijoada()
acompanhamento = acompanhamentoFeijoada()
total = volume * opção + acompanhamento
print('O total ficou:{:.2f}(volume:{:.2f},opção:{:.2f}),acompanhamento:{:.2f}'.format(total,volume,opção,acompanhamento))