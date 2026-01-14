## Arrays/Two Sum

- ERRO: Confundi o uso do hashmap ao adicionar um par chave valor usando o complement "hashMap[complement] = idx".
- CORRETO: (hashMap[num] = idx).
- MOTIVO: complement é apenas para consulta.


## Arrays/ Prefix Sum
- ERRO: COnfundi o uso do "or" e do "and" na estrutura de decisão para decidir se usava o range sum.
- CORRETO: "if right > 0 and left > 0:"
- MOTIVO: assim ele garante que o que está sendo pedido é um intervalo "fatiado" e não um que começa no índice 0

## Arrays/ Kadane
- ERRO: Não atualizar o "currentSum" após atribuir a ele o valor 0, ou seja, não começei um novo subarray como a lógica pede
- CORRETO: "currentSum += i" dentro do loop
- MOTIVO: assim ele garante que o que está começando um novo Subarray de somas, pois coloca o próximo elemento para ser somado.


## Array/ Binary Search
- ERRO: Não atualizar os índices corretamente (Low & HIGH)
- CORRETO: Se guess > target; low = mid + 1.  Se guess < target; high = mid - 1.
- MOTIVO: Assim ele descarta as metades corretas. 