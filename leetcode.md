

# Contains Duplicate (1)

## Padrão
- HashSet serve para problemas onde não pode haver repetição de itens. Se tem repetido, simplesmente retorna.

## Complexidade
- O(n) para tempo.
- O(n) para espaço.

O pior cenário sobre espaço é quando ele também não tem duplicata, ja que guarda os valores no HashSet.

## ERRO:
- Errei sintaxe do HashSet, não sabia comparar itens iguais. Mas a função retorna falso caso não consiga adicionar.

## REVISÃO



# Two Sum

## Padrão 
- Utilizar dois loops para fazer comparação (O(n²)).
- Utilizar HashMap(valor que falta, index).

## Complexidade
- O(n)

## ERRO:
- SINTAXE: Não sabia com utilizar os métodos de Hash.
- ORDEM DE HASH: Tentei (índice, valor) mas percebi que para retorna a chave é masi cimplicado em Hashs, mas o contains serve em ambos tranquilamente, então mudei para (valor, ínidce)  e ficou mais fácil.

## REVISÃO
LÓGICA: 

    CRIA UM HASHSET
    ITERA SOBRE O ARRAY
    SE ADICIONAR RETORNA FALSE =  NÃO TEM DUPLICATA
    RETORNA TRUE OU FALSE

```java
import java.util.HashSet;

 public boolean containsDuplicate(int[] nums) {
    HashSet<Integer> set = new HashSet<>();

    for(int i = 0; i < nums.length; i++){
        if(!set.add(nums[i])){
            return true;
        } 
    }

    return false;
 }
```