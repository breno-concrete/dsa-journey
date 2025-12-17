## Arrays/Two Sum

- ERRO: Confundi o uso do hashmap ao adicionar um par chave valor usando o complement "hashMap[complement] = idx".
- CORRETO: (hashMap[num] = idx).
- MOTIVO: complement é apenas para consulta.


## Arrays/ Prefix Sum
- ERRO: COnfundi o uso do "or" e do "and" na estrutura de decisão para decidir se usava o range sum.
- CORRETO: "if right > 0 and left > 0:"
- MOTIVO: assim ele garante que o que está sendo pedido é um intervalo "fatiado" e não um que começa no índice 0

