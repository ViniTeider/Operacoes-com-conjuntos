#Aluno: Vinicius Teider

#Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a 
#linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  apresentar  os  resultados  de 
#operações que serão realizadas entre dois conjuntos de dados.  


# Abre o arquivo na variavel comandos
comandos = open("comandos1.txt","r")

#--------------------FUNÇÔES----------------------------------------------------

#---Cria Conjuntos----- 
def criar_conjuntos():
  first_set = []
  second_set = []
  
  temp_value = (((comandos.readline()).rstrip("\n")).replace(" ",""))
  first_set = temp_value.split(",")
  temp_value = (((comandos.readline()).rstrip("\n")).replace(" ",""))
  second_set = temp_value.split(",")
    
  return(first_set,second_set)

#---Operação:União-------
def uniao(A,B):
  final_set = []

  for i in A:
    final_set.append(i)
  for i in B:
    if i not in A:
      final_set.append(i)
      
  str_A = ",".join(A)
  str_B = ",".join(B)
  str_final_set = ",".join(final_set)
  
  print(f"União: conjunto 1 {{{str_A}}}, conjunto 2 {{{str_B}}}. Resultado: {{{str_final_set}}}")
  return(final_set)

#----Operação:Interseção-------
def intersecao(A,B):
  final_set = []
  
  for c in A:
      if c in B:
        final_set.append(c)

  str_A = ",".join(A)
  str_B = ",".join(B)
  str_final_set = ",".join(final_set)

  print(f"Interseção: conjunto 1 {{{str_A}}}, conjunto 2 {{{str_B}}}. Resultado: {{{str_final_set}}}")
  return(final_set)

#---Operação: Diferença-----
def diferenca(A,B):
  final_set = []
  
  for c in A:
      if c not in B:
        final_set.append(c)

  str_A = ",".join(A)
  str_B = ",".join(B)
  str_final_set = ",".join(final_set)

  print(f"Diferença: conjunto 1 {{{str_A}}}, conjunto 2 {{{str_B}}}. Resultado: {{{str_final_set}}}")
  return(final_set)

#---Operação: Produto Cartesiano-----
def cartesiano(A,B):
  final_set = []
  count = 0

  for c in A:
    for l in B:
      final_set.append([])
      
      final_set[count].append(c)
      final_set[count].append(l)

      count += 1

  str_A = ",".join(A)
  str_B = ",".join(B)

  aux = ","
  final_result = aux.join([aux.join([str(c) for c in l]) for l in final_set])
  
      
  print(f"Produto Cartesiano: conjunto 1 {{{str_A}}}, conjunto 2 {{{str_B}}}. Resultado: {{{final_result}}}")
  return(final_set)
#---------------------------------------------------------------------------------

for c in comandos:
  value = (c).rstrip("\n").replace(" ","")

#verifica e resolve a operação
  
  #União
  if "U" in value[0]:
    A,B = criar_conjuntos()
    uniao(A,B)
    
  #Interseção
  elif "I" in value[0]:
    A,B = criar_conjuntos()
    intersecao(A,B)
    
  #Diferença
  elif "D" in value[0]:
    A,B = criar_conjuntos()
    diferenca(A,B)
    
  #Produto Cartesiano
  elif "C" in value[0]:
    A,B = criar_conjuntos()
    cartesiano(A,B)
      
comandos.close()