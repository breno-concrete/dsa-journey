## Two Sum - Padrão Hash Map

# Quando usar?
- quando pede dois elmentos que somados deêm um número específico
- reduzir força bruta

# Ideia central
- percorrer o array uma vez O(n)
- para cada número, calcula o complemento
- verficia se ja foi visto

# Complexidade 
- O(n)

# Armadilhas comuns
- adicioanar par no hash antes de verificar

## Prefix Sum 

# Quando usar? 
- quando queremos a soma de determinados dados de um array
- queremos definir um "range" para essa soma

# Ideia central
- criar na memória um array que contém as somas predefinidas nas respectivas posições do array original, indo direto no índice encontramos a resposta
- caso peça por "range", pegamos a soma do número mais a direita (no prefix sum)  e subtraímos pelo número da soma do número antérior ao primeiro número do intervalo.

# Complexidade
- O(1)

# Armadilhas comuns
- Não cosniderar a subtração pelo índice anterior ao do início do intervalo

## Kadane

# Quando usar? 
- quando queremos o subarray com a maior soma entre eles

# Ideia central
- Criar variáveis "maxSub" e "currentSum", que serão atualizadas a cada iteração sobre o array.
- Iterar sobre o array, se "currentSum" for menor que zero, nós atirbuimos a ela o valor 0 para dar início a um novo subarray (a lógica diz que quando a soma atual é um número negativo, sempre teremos que comeaçar um novo subarray).
- Vemos qual o maior valor entre "maxSub" e "currentSum" e atribuimos o resultado a "maxSub".
- Ao final, a função retorna maxSub.
# Complexidade
- O(n)

# Armadilhas comuns
- Não inciar um novo subarray (currentSum = 0)


## Binary Search

# Quando usar?
- quando temos um array e queremos um determinado valor dentro dele.

# Ideia central
- index do centro do array.
- caso o valor buscado não seja o valor do meio, analisamos se o valor buscado é maior ou menor que o valor do meio.
- if MAIOR : descartamos metade dos valores (todos as esquerda do valor central).
- if MENOR : descartamos metade dos valores (todos as direita do valor central).
- repetindo até se encotrar o valor.

# Complexidade 
- O(logn)

# Armadilhas comuns
- não atualizar os index (low e high) corretamente ao descartar uma "metade".

## Selection Sort

# Quando usar?
- quando temos um array e queremos ordená-lo de forma crescente ou decrescente.

# Ideia central
- Criamos uma função que retorna o menor número de uma lista.
- Achamos o menor número e colocamos em um array vazio (array.append), e tiramos o respectivo valor do array antigo (array.pop).
- Por meio de um loop, faze-se isso com todos os valores

# Complexidade 
- O(n²)

# Armadilhas comuns
- COnfundir a lógica da função que acha o menor valor
- Não retirar o menor valor do array original ao colocar no novo array.

## Recursion

# Quando usar?
- quando queremos simplificar uma tarefa repetitiva sem a utilização de um loop, não visando perfomance mas sim clareza ao desenvolvedor.

# Ideia central
- Criar uma função e chamá-la dentro dela mesma.
- Base case: Quando a recursão para de agir, cenário mais "simples", "fácil".
- Recursion case: Quando a recursão age


# Armadilhas comuns
- Não colocar base case, criando um loop infinito.


## Call Stack

# Ideia central
- Estrutura de dados "pilha"
- Como a memória se comporta diante de um função que chama outras funções
- Uma função ocupa um espaço an memória. Outra função, dentro da função executada, ganha uma prioridade de execução e um outro espaço na memória, enquanto a função "principal" está em "pausa" até o fim da execução da função "filha", e assim sucessivamente.


# Armadilhas comuns
- Em casos de muitos dados pode-se sobrecarregar o sistema

## Linked Lists

# Quando usar?
- quando queremos adicionar, excluir itens de uma lista de forma mais eficiente O(1).
- Quando não priorisamos Random Access.

# Ideia central
- Um bloco de memória aponta para o endereço de outro bloco de memória, não sendo sequenciados "um ao lado do outro", facilitando a movimentação de elementos na lista.


# Complexidade 
- Random Access O(n)
- Adicionar/ Remover elemento O(1)

## Quick Sort

# Quando usar?
- quando queremos ordenar uma lista numérica.

# Ideia central
- Escolhemos um valor da lista para se tornar o "pivô", a partir dele separamos em dois arrays, um que contêm valores menores que o pivô e outro que contêm valores maiores que o pivô. Usamos recursividade para os subarrays, ordenando a lista inteira. 


# Complexidade 
- Worst case: O(n²)
- Best/Avarage case: O(n log n )
