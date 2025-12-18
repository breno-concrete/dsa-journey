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
