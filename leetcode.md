# 242. Valid Anagram

## Complexidade 
- O(n)

## Ideia Central
- Verifica se o tamanho de ambas as strings é igual, caso o contrário retorna falso
- Organiza um hashmap como todas as letras de "s", um letra e quantidade de vezes que ela aparece.
- Compara com a string "t", itera sobre ela. A cada letra igual ele subtrai um do valor do hashmap de "s", até todos zerarem.
- Caso tenha mais letras ou letras que não estão dentro do hash, ele retorna falso.
