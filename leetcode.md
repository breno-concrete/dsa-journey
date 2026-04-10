# 242. Valid Anagram

## Complexidade 
- O(n)

## Ideia Central
- Verifica se o tamanho de ambas as strings é igual, caso o contrário retorna falso
- Organiza um hashmap como todas as letras de "s", um letra e quantidade de vezes que ela aparece.
- Compara com a string "t", itera sobre ela. A cada letra igual ele subtrai um do valor do hashmap de "s", até todos zerarem.
- Caso tenha mais letras ou letras que não estão dentro do hash, ele retorna falso.



# Valid Palindrome

## COmplexidade
- O(n)

## Ideia Central
- se a string está vazia retornamos true.
- Setamos os index inciais e finais (start & end).
- Loop while onde ele para caso o start > end.
- Dentro do loop, verificamos se cada um dos characteres (com o index start e end) são digitos ou não. Caso não, adicionamos uma unidade ao index respectivo.
- caso ambos sejam digitos, verificamos se são iguais.
- se forem iguais, o loop conitnua. Se não forem iguais retorna false.


# Two Sum

## COmplexidade
- O(n)

## Ideia Central
- Criamos um HashMap vazio
- Com um loop for, pegamos o primeiro elemento e subtraimos do target, nos gerando um componente;
- se esse componente existe dentro do HashMap, nós retornamos um array com o indice do componente e do numero comparado
- caso não exista dentro do HashMap, nós adicionamos o número que foois comparado.