

# Contains Duplicate (1)

## Padrão
- HashSet serve para problemas onde não pode haver repetição de itens. Se tem repetido, simplesmente retorna.

## Complexidade
- O(n) para tempo.
- O(n) para espaço.

Porque o pior cenário de tempo é aquele em que não tem duplicata. O pior cenário sobre espaço é quando ele também não tem duplicata, ja que guarda os valores no HashSet.

## ERRO:
- Errei sintaxe do HashSet, não sabia comparar itens iguais. Mas a função retorna falso caso não consiga adicionar.

## REVISÃO
... REIMPLEMENTAR DE CABEÇA