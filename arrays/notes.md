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