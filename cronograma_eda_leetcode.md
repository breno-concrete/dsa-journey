# 🗺️ Roadmap Definitivo — 30 Dias até Maestria em Árvores

> **Tempo:** 1h30/dia, 6 dias/semana, 1 descanso.
> **Premissa:** Você conhece a teoria. Falta prática, fluência e profundidade.
> **Meta:** Implementar qualquer estrutura até AVL sem consulta. Ensinar. Passar entrevista.

---

## Rotina Fixa — 4 Blocos, Todos os Dias

```
📖  10 min  →  Conceito (ler/assistir/entender o fundamento do dia)
🔵  30 min  →  C (implementar a estrutura/algoritmo)
🟩  35 min  →  Java (5 min papel + 30 min LeetCode)
📝  15 min  →  Caderno (padrão + complexidade + erro + revisão espaçada)
─────────────
    1h30
```

### Detalhamento de cada bloco:

**📖 Conceito (10 min):** Antes de codar, ENTENDER. Ler slides do professor, assistir 1 vídeo curto no "Programação Descomplicada" ou visualizar no [visualgo.net](https://visualgo.net). Nunca pule isso — é o que separa "copiar código" de "entender o que faz".

**🔵 C (30 min):** Implementar do zero. Sem copiar. Se travou, relê o conceito. Se não saiu em 30 min, continua amanhã de onde parou.

**🟩 Java (35 min):**
- Primeiros 5 min: LER o problema, DESENHAR no papel, LISTAR 2 abordagens, ESCOLHER uma e escrever em pseudocódigo
- Próximos 25 min: Codar a solução
- Últimos 5 min: Se não resolveu, ler a dica. Se resolveu, otimizar ou pensar em alternativa

**📝 Caderno (15 min):**
```
1. PADRÃO:       "[Técnica X] serve pra [tipo de problema Y]"
2. COMPLEXIDADE:  "Tempo O(___) Espaço O(___) porque ___"
3. ERRO:          "Errei em [Z] porque [motivo]"
4. REVISÃO:       Reimplementar de cabeça 1 função de semana anterior (5 min)
```

---

## Dias Especiais (fixos toda semana)

| Dia da semana | O que muda |
|---|---|
| **Dia 3** (toda semana) | Bloco C = **tracing manual no papel** (sem computador) |
| **Dia 6** (toda semana) | Bloco Caderno = **gravar áudio de 3 min ensinando** o tópico da semana |
| **Domingo** | **Teste de maestria** (30 min extra, sem consulta, papel e caneta) |

---

# ═══════════════════════════════════════
# SEMANA 1 — Arrays, Strings, Recursão
# ═══════════════════════════════════════

> Você já sabe isso. O objetivo é **velocidade, fluência e Big O automático.**

---

## ~~Dia 1 — Array Dinâmico (Criação)~~

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Ler sobre **alocação dinâmica em C**: `malloc` aloca bytes no heap, `realloc` redimensiona, `free` libera. Abrir [visualgo.net/array](https://visualgo.net/en/array) e ver a animação de inserção/remoção |
| 🔵 C | Criar `my_vector.c`. Definir: `typedef struct { int* data; int size; int capacity; } Vector;`. Implementar `Vector* create(int initial_capacity)` e `void push(Vector* v, int value)` — quando `size == capacity`, fazer `realloc` com `capacity * 2`. Implementar `void print(Vector* v)`. Testar: criar vetor de capacidade 2, inserir 5 valores, verificar que cresceu |
| 🟩 Java | **Papel (5 min):** Ler [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/). Desenhar: input `[1,2,3,1]`. Listar abordagens: (A) dois loops O(n²), (B) ordenar O(n log n), (C) HashSet O(n). Escolher C. **Código (25 min):** Implementar com `HashSet`. **Refletir (5 min):** Implementar com sort também. Comparar |
| 📝 Caderno | **Padrão:** "HashSet.contains() → verificar existência em O(1)". **Complexidade:** "Tempo O(n) — percorre array 1x. Espaço O(n) — HashSet armazena até n elementos". **Erro:** ___. **Revisão:** — (primeiro dia) |

---

## ~~Dia 2 — Array Dinâmico (Operações)~~

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Entender **custo amortizado** do array dinâmico: por que dobrar a capacidade faz push ser O(1) amortizado, não O(n). Pesquisar: "amortized analysis dynamic array" |
| 🔵 C | Adicionar ao `my_vector.c`: `int get(Vector* v, int index)` — retorna -1 se index inválido. `void remove_at(Vector* v, int index)` — faz shift dos elementos à direita pra esquerda. `void free_vector(Vector* v)` — libera data e o struct. Testar: inserir `{10,20,30,40,50}`, remover index 2, imprimir = `{10,20,40,50}` |
| 🟩 Java | **Papel (5 min):** Ler [1. Two Sum](https://leetcode.com/problems/two-sum/). Input `[2,7,11,15]`, target 9. Abordagens: (A) dois loops O(n²), (B) HashMap: pra cada num, checar se `target - num` já tá no map. Escolher B. **Código (25 min):** Implementar. **Refletir (5 min):** Por que guardar `{valor → índice}` e não `{índice → valor}`? |
| 📝 Caderno | **Padrão:** "HashMap pra encontrar complemento → evita dois loops, O(n)". **Complexidade:** "Tempo O(n). Espaço O(n)". **Erro:** ___. **Revisão:** reler anotação do Dia 1 |

---

## Dia 3 — Strings em C + Tracing Manual 🖊️

terminar a seção de C do dia anterior

| Bloco | Tarefa exata |
|---|---|
| ~~📖 Conceito~~ | Ler sobre **strings em C**: `char[]` vs `char*`, terminador `\0`, por que `strlen` é O(n) (precisa percorrer até achar `\0`). Diferença pra Java onde `.length()` é O(1) |
| ~~🔵 C | ⚠️ **TRACING MANUAL (sem computador).** Pegar papel e caneta. Desenhar a memória (array de chars) pra string `"hello\0"`. Depois simular no papel: "como `my_strlen` percorre essa memória?". Desenhar o ponteiro avançando byte a byte. Depois: implementar `my_strlen()` e `my_strcmp()` em `my_string.c` no computador |
| 🟩 Java | **Papel (5 min):** Ler [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/). Input: "anagram", "nagaram". Abordagem: array de 26 int, incrementar pra s1, decrementar pra s2, verificar se tudo é 0. **Código (25 min):** Implementar. NÃO usar HashMap — usar `int[26]`. **Refletir (5 min):** Qual a complexidade? Por que `int[26]` é melhor que HashMap aqui? |
| 📝 Caderno | **Padrão:** "Array de frequência (int[26]) → contar chars em O(n), espaço O(1) pois 26 é constante". **Complexidade:** "Tempo O(n). Espaço O(1)". **Erro:** ___. **Revisão:** reler Dia 2 + tentar reescrever `push()` do array dinâmico de cabeça (5 min) |

---

## Dia 4 — Strings (Continuação) + Two Pointers

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Ler sobre **Two Pointers**: técnica onde dois índices caminham pelo array (do início ou um de cada ponta). Visualizar: reverter string com pointer_left e pointer_right se aproximando |
| 🔵 C | Adicionar ao `my_string.c`: `void my_strcpy(char* dest, char* src)` e `void my_strrev(char* str)` — reverter in-place usando two pointers (trocar `str[left]` com `str[right]`). Testar: `my_strrev("hello")` → `"olleh"` |
| 🟩 Java | **Papel (5 min):** Ler [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/). Input: "A man, a plan, a canal: Panama". Two pointers: left do início, right do fim, ignorar não-alfanuméricos, comparar lowercase. **Código (25 min):** Implementar. **Refletir (5 min):** E se a string fosse `""`? E `"a"`? Edge cases |
| 📝 Caderno | **Padrão:** "Two Pointers (pontas opostas) → palíndromos, reverter, arrays ordenados. Evita O(n²)". **Complexidade:** "Tempo O(n). Espaço O(1)". **Erro:** ___. **Revisão:** reler Dia 3 |

---

## Dia 5 — Recursão

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Ler sobre **pilha de chamadas** (call stack): cada chamada recursiva empilha um frame. Desenhar no papel a call stack de `factorial(4)` — 4 frames empilhados, depois desempilhando com os resultados. Entender: por que recursão infinita causa stack overflow? |
| 🔵 C | Criar `recursion.c`. Implementar: `int factorial(int n)`, `int fibonacci(int n)`, `int binary_search_rec(int* arr, int low, int high, int target)`. Pra cada função, adicionar um `printf` no início mostrando os parâmetros (pra ver a pilha de chamadas). Rodar `fibonacci(6)` e observar quantas chamadas faz (dica: muitas — é O(2^n)) |
| 🟩 Java | **Papel (5 min):** Ler [704. Binary Search](https://leetcode.com/problems/binary-search/). Desenhar array `[-1,0,3,5,9,12]`, target 9. Simular: mid=3→5, vai pra direita, mid=4→9, achou. **Código (25 min):** Implementar iterativo E recursivo. **Refletir (5 min):** Iterativo usa O(1) espaço. Recursivo usa O(log n) espaço (call stack). Qual é melhor? |
| 📝 Caderno | **Padrão:** "Binary Search → dividir espaço pela metade = O(log n). Funciona só em array ORDENADO". **Complexidade:** "Tempo O(log n). Espaço O(1) iterativo, O(log n) recursivo". **Erro:** ___. **Revisão:** reler Dia 4 + escrever `my_strrev` de cabeça no caderno (5 min) |

---

## Dia 6 — Merge Sort + Áudio de Ensino 🎙️

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Abrir [visualgo.net/sorting](https://visualgo.net/en/sorting), selecionar Merge Sort, assistir a animação completa. Entender: dividir até ter 1 elemento, depois mergear em ordem. **Por que é O(n log n)?** → log n níveis de divisão, cada nível processa n elementos |
| 🔵 C | Criar `merge_sort.c`. Implementar: `void merge(int* arr, int left, int mid, int right)` — usa arrays temporários pra mergear. `void merge_sort(int* arr, int left, int right)` — divide e chama recursivo. Testar com `{38, 27, 43, 3, 9, 82, 10}` → deve imprimir `{3, 9, 10, 27, 38, 43, 82}` |
| 🟩 Java | **Papel (5 min):** Ler [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/). Input: `[-2,1,-3,4,-1,2,1,-5,4]`. Kadane's: pra cada elemento, decidir: continuar o subarray atual ou começar novo? `current = max(num, current + num)`. **Código (25 min):** Implementar. **Refletir (5 min):** Simular no papel com o input acima, passo a passo |
| 📝 Caderno | ⚠️ **ÁUDIO (substitui a revisão):** Gravar 3 minutos no celular explicando: "O que é Merge Sort, como funciona passo a passo, e por que é O(n log n)". Ouvir depois. Se gagejou ou ficou confuso, anotar o que precisa melhorar |

---

## 🏁 Teste de Maestria — Semana 1 (Domingo, 30 min)

Sem consulta. Papel e caneta.

| Teste | Tempo | Passou? |
|---|---|---|
| Escrever `push()` do array dinâmico com `realloc` em C | 5 min | ☐ |
| Escrever Merge Sort completo em C (merge + merge_sort) | 12 min | ☐ |
| Resolver [Two Sum](https://leetcode.com/problems/two-sum/) em Java no papel | 5 min | ☐ |
| Escrever a complexidade de: busca linear, binary search, merge sort, two sum com hashmap | 3 min | ☐ |
| Explicar em voz alta: "O que é custo amortizado do array dinâmico?" | 2 min | ☐ |

**Passou em 4/5? Avança. Menos que 4? Repete os itens que falhou durante a semana 2.**

**Problemas LeetCode acumulados: 6** ✓

---

# ═══════════════════════════════════════
# SEMANA 2 — Listas Encadeadas
# ═══════════════════════════════════════

> A estrutura que mais testa ponteiros. Se dominar aqui, o resto é mais fácil.

---

## Dia 7 — Node + Insert Head + Print

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Ler sobre **lista encadeada vs array**: array = acesso O(1) por índice, inserção O(n). Lista = acesso O(n), inserção no início O(1). Abrir [visualgo.net/list](https://visualgo.net/en/list), assistir inserção e remoção |
| 🔵 C | Criar `linked_list.c`. Definir: `typedef struct Node { int data; struct Node* next; } Node;`. Implementar: `Node* create_node(int value)` — aloca com `malloc`, seta `next = NULL`. `Node* insert_head(Node* head, int value)` — cria novo, `novo->next = head`, retorna novo. `void print_list(Node* head)` — percorre imprimindo. Testar: inserir 5, 4, 3, 2, 1 no head → imprimir: `1 → 2 → 3 → 4 → 5 → NULL` |
| 🟩 Java | **Papel (5 min):** Ler [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/). Desenhar: `1→2→3→NULL`. Simular com 3 ponteiros: `prev=NULL, curr=1, next=2`. Trocar `curr.next=prev`. Avançar. Desenhar cada passo. **Código (25 min):** Implementar iterativo. **Refletir (5 min):** Qual a complexidade? O(n) tempo, O(1) espaço |
| 📝 Caderno | **Padrão:** "Reverter lista = 3 ponteiros: prev, curr, next. Sempre salvar next antes de trocar curr.next". **Complexidade:** "O(n) tempo, O(1) espaço". **Erro:** ___. **Revisão:** escrever `binary_search_rec` de cabeça (da semana 1) |

---

## Dia 8 — Insert Tail + Insert At

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Entender a diferença de complexidade: `insert_head` é O(1), `insert_tail` é O(n) (precisa percorrer tudo). Por que? Porque só temos ponteiro pro head. Se tivéssemos ponteiro pro tail, tail seria O(1) também |
| 🔵 C | Adicionar: `Node* insert_tail(Node* head, int value)` — se head é NULL, retorna novo nó. Senão, percorre até `current->next == NULL`, seta `current->next = novo`. `Node* insert_at(Node* head, int value, int pos)` — inserir na posição pos (0-indexed). Pos 0 = insert_head. Testar: `insert_at(head, 99, 2)` no meio da lista |
| 🟩 Java | **Papel (5 min):** Ler [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/). Desenhar: `1→2→4` e `1→3→4`. Criar dummy node, comparar heads, linkar o menor. **Código (25 min):** Implementar. **Refletir (5 min):** Por que dummy node simplifica? (evita if especial pro primeiro elemento) |
| 📝 Caderno | **Padrão:** "Dummy node → criar nó fake antes do head, retornar dummy.next. Evita edge case de lista vazia/primeiro nó". **Complexidade:** "O(n+m) tempo, O(1) espaço". **Erro:** ___. **Revisão:** reler Dia 7 |

---

## Dia 9 — Delete + Search + Free 🖊️

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Entender os **edge cases de delete**: deletar o head (precisa atualizar o head), deletar nó do meio (nó anterior aponta pro próximo), deletar nó que não existe (retorna sem fazer nada). Desenhar cada caso no papel |
| 🔵 C | ⚠️ **TRACING MANUAL PRIMEIRO (10 min no papel).** Desenhar lista `1→2→3→4→NULL`. Simular no papel: deletar o valor 3. Mostrar: prev=2, current=3, `prev->next = current->next`, `free(current)`. Resultado: `1→2→4→NULL`. **DEPOIS (20 min):** Implementar: `Node* delete_value(Node* head, int value)`, `int search(Node* head, int value)`, `void free_all(Node* head)`. Testar: deletar head, deletar meio, deletar fim, deletar valor que não existe |
| 🟩 Java | **Papel (5 min):** Ler [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/). Desenhar lista com ciclo. Fast anda 2 passos, slow anda 1. Se tem ciclo, fast alcança slow. Se não tem, fast chega em null. **Código (25 min):** Implementar. **Refletir (5 min):** Por que funciona matematicamente? (fast reduz a distância em 1 a cada iteração) |
| 📝 Caderno | **Padrão:** "Fast & Slow → detectar ciclo. Fast anda 2x, slow 1x. Se se encontram = ciclo". **Complexidade:** "O(n) tempo, O(1) espaço". **Erro:** ___. **Revisão:** reler Dia 8 + escrever `merge()` do Merge Sort de cabeça (Semana 1) |

---

## Dia 10 — Edge Cases + Middle

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Ler sobre **Fast & Slow pra achar o meio**: quando fast chega no fim, slow tá no meio. Funciona porque fast percorre 2x a velocidade. Visualizar com lista de 5 e 6 elementos (par e ímpar) |
| 🔵 C | Revisar TODO o `linked_list.c`. Criar `test_edge_cases()`: testar deletar de lista vazia, deletar o único elemento, deletar head, buscar em lista vazia, free_all em lista vazia. Corrigir TODO bug que aparecer. Adicionar: `Node* find_middle(Node* head)` usando fast & slow |
| 🟩 Java | **Papel (5 min):** Ler [876. Middle of Linked List](https://leetcode.com/problems/middle-of-the-linked-list/). Simular Fast & Slow em `1→2→3→4→5`. Fast=1,Slow=1 → Fast=3,Slow=2 → Fast=5,Slow=3. Slow tá no meio! **Código (20 min):** Implementar. **Depois (10 min):** Resolver [160. Intersection](https://leetcode.com/problems/intersection-of-two-linked-lists/) — calcular diferença de tamanho, avançar a maior, depois andar juntos |
| 📝 Caderno | **Padrão:** "Fast & Slow → achar meio = quando fast chega no fim, slow tá no meio". **Complexidade:** "O(n) tempo, O(1) espaço — ambos". **Erro:** ___. **Revisão:** reler Dia 9 |

---

## Dia 11 — Lista Dupla + Remove Nth

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Ler sobre **lista duplamente encadeada**: cada nó tem `prev` e `next`. Vantagem: deletar é mais fácil (não precisa rastrear o anterior). Desvantagem: usa mais memória (2 ponteiros por nó). Quando usar? Quando precisa navegar nos dois sentidos (ex: LRU Cache, editor de texto) |
| 🔵 C | Criar `doubly_linked.c`: `typedef struct DNode { int data; struct DNode *prev, *next; } DNode;`. Implementar: `insert_head`, `insert_tail`, `delete_value` (notar: agora deletar o meio é mais fácil: `node->prev->next = node->next; node->next->prev = node->prev`). Testar: inserir 5 valores, deletar do meio |
| 🟩 Java | **Papel (5 min):** Ler [19. Remove Nth From End](https://leetcode.com/problems/remove-nth-node-from-end-of-list/). Abordagem: Two Pointers com gap de N. Primeiro ponteiro avança N passos. Depois ambos andam juntos. Quando o primeiro chega no fim, o segundo tá N passos antes do fim. **Código (25 min):** Implementar com dummy node. **Refletir (5 min):** Por que precisa de dummy? (caso n = tamanho da lista, precisa deletar o head) |
| 📝 Caderno | **Padrão:** "Two Pointers com gap → encontrar Nth do fim sem saber tamanho total". **Complexidade:** "O(n) tempo, O(1) espaço". **Erro:** ___. **Revisão:** reler Dia 10 + escrever `insert_head` da lista simples de cabeça |

---

## Dia 12 — Reimplementação + Problema Hard + Áudio 🎙️

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Reler rapidamente suas anotações de caderno dos Dias 7-11. Repassar mentalmente: insert_head, insert_tail, delete, search, free_all, find_middle, reverse |
| 🔵 C | **TESTE CRONOMETRADO:** Arquivo novo `list_v2.c`. Reimplementar do zero, sem consultar `linked_list.c`: `create_node`, `insert_head`, `insert_tail`, `delete_value`, `search`, `print_list`, `free_all`. Anotar tempo: meta < 15 min |
| 🟩 Java | **Papel (5 min):** Ler [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/). Desenhar: `2→4→3` + `5→6→4` = 342+465=807 = `7→0→8`. Cuidar do carry! **Código (30 min):** Implementar. Edge case: listas de tamanhos diferentes, carry no final |
| 📝 Caderno | ⚠️ **ÁUDIO (substitui revisão):** Gravar 3 min explicando: "O que é lista encadeada, quando usar em vez de array, e como funciona Fast & Slow". Ouvir. Anotar pontos fracos. **Tempo da reimplementação:** ___ min |

---

## 🏁 Teste de Maestria — Semana 2 (Domingo, 30 min)

| Teste | Tempo | Passou? |
|---|---|---|
| Implementar lista encadeada em C no papel: `insert_head` + `delete_value` + `search` | 10 min | ☐ |
| Resolver [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) em Java no papel (iterativo, 3 ponteiros) | 5 min | ☐ |
| Explicar em voz alta: "Array vs Lista — quando usar cada? 3 cenários" | 3 min | ☐ |
| Explicar: "O que é Fast & Slow? Pra que serve? 2 usos diferentes" | 2 min | ☐ |
| **REVISÃO SEMANA 1:** Escrever Merge Sort em C no papel | 8 min | ☐ |

**Passou em 4/5? Avança. Problemas LeetCode acumulados: ~13** ✓

---

# ═══════════════════════════════════════
# SEMANA 3 — Pilhas e Filas
# ═══════════════════════════════════════

> Duas estruturas, uma semana. Pilha = LIFO. Fila = FIFO. Simples, mas os problemas são elegantes.

---

## Dia 13 — Pilha com Array

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Ler sobre **Stack (LIFO)**: último a entrar, primeiro a sair. Aplicações: verificar parênteses, undo/redo, call stack de recursão. Abrir [visualgo.net/list](https://visualgo.net/en/list) → Stack → assistir push e pop |
| 🔵 C | Criar `stack.c`: `typedef struct { int* data; int top; int capacity; } Stack;`. Implementar: `Stack* create(int cap)`, `void push(Stack* s, int val)` — verifica `is_full` antes, `int pop(Stack* s)` — verifica `is_empty` antes, `int peek(Stack* s)`, `int is_empty(Stack* s)`, `int is_full(Stack* s)`, `void free_stack(Stack* s)`. Testar: push 1,2,3 → peek=3 → pop=3 → pop=2 → peek=1 |
| 🟩 Java | **Papel (5 min):** Ler [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/). Estratégia: abrir (`{[(`) = push. Fechar (`)]}`) = pop e comparar com o esperado. Se stack vazia no final = válido. **Código (25 min):** Implementar. Testar: `"([]{})"` ✓, `"([)]"` ✗, `""` ✓, `"("` ✗ |
| 📝 Caderno | **Padrão:** "Stack → matching de pares (parênteses, tags HTML). Abrir=push, fechar=pop+verificar". **Complexidade:** "O(n) tempo, O(n) espaço — stack pode ter até n/2 elementos". **Erro:** ___. **Revisão:** escrever `delete_value` da lista encadeada de cabeça |

---

## Dia 14 — Pilha com Lista + Min Stack

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Entender que pilha pode ser implementada com lista encadeada: `push` = `insert_head`, `pop` = `remove_head`. Ambos O(1). Vantagem sobre array: sem limite de tamanho. Desvantagem: overhead de ponteiros |
| 🔵 C | Criar `stack_list.c`: pilha usando lista encadeada. Reutilizar o conceito de `Node` da semana 2. `push` = inserir no head, `pop` = remover head, `peek` = retornar head->data. Testar com os mesmos testes do Dia 13 — deve dar o mesmo resultado |
| 🟩 Java | **Papel (5 min):** Ler [155. Min Stack](https://leetcode.com/problems/min-stack/). Problema: getMin() em O(1). Solução: usar stack auxiliar que rastreia o mínimo atual. A cada push, push o min(valor, minStack.peek()) na minStack. **Código (25 min):** Implementar. **Refletir (5 min):** E se usasse só 1 stack? Possível com pares (valor, min_até_aqui) |
| 📝 Caderno | **Padrão:** "Stack auxiliar → rastrear min/max em O(1). Sempre manter sincronizada com a principal". **Complexidade:** "Todas operações O(1). Espaço O(n) — stack auxiliar". **Comparação:** stack com array vs lista: array = acesso O(1) mas tamanho fixo; lista = tamanho dinâmico mas mais memória. **Revisão:** reler Dia 13 |

---

## Dia 15 — Pós-fixa + Tracing 🖊️

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Ler sobre **notação pós-fixa** (RPN): `3 4 +` = `3+4` = `7`. Sem parênteses, sem precedência. Regra: número = push, operador = pop dois, opera, push resultado. Computadores usam isso internamente |
| 🔵 C | ⚠️ **TRACING (10 min no papel):** Avaliar `5 1 2 + 4 * + 3 -` no papel. Desenhar a stack a cada passo: push 5, push 1, push 2, pop 2 e 1, 1+2=3, push 3, push 4, pop 4 e 3, 3*4=12, push 12, pop 12 e 5, 5+12=17, push 17, push 3, pop 3 e 17, 17-3=14. Resultado: 14. **DEPOIS (20 min):** Implementar `int eval_postfix(char* expr)` em C usando sua stack |
| 🟩 Java | **Papel (5 min):** Ler [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/). Mesmo conceito do C. **Código (25 min):** Implementar. Dica: `Integer.parseInt()` pra converter token em número. Cuidado: divisão em Java trunca pra zero. **Refletir (5 min):** Comparar seu código Java com seu código C — qual ficou mais simples? Por quê? |
| 📝 Caderno | **Padrão:** "Pós-fixa + Stack → avaliar expressões sem ambiguidade. Número=push, operador=pop2+opera+push". **Complexidade:** "O(n) tempo — percorre cada token 1x". **Erro:** ___. **Revisão:** reler Dia 14 + escrever `insert_head` de lista de cabeça |

---

## Dia 16 — Monotonic Stack

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Ler sobre **Monotonic Stack**: stack onde os elementos são sempre crescentes ou decrescentes. Uso: encontrar o "próximo maior elemento" ou "próximo menor elemento" em O(n). Sem isso, seria O(n²). Assistir: NeetCode "Daily Temperatures" no YouTube (7 min) |
| 🔵 C | Implementar em C: `void next_greater(int* arr, int n, int* result)` — pra cada posição, encontrar o próximo elemento maior à direita. Se não existe, -1. Usar stack de ÍNDICES (não valores). Input: `{4,5,2,10,8}` → Output: `{5,10,10,-1,-1}` |
| 🟩 Java | **Papel (5 min):** Ler [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/). Input: `[73,74,75,71,69,72,76,73]`. Desenhar a stack a cada passo (guardar ÍNDICES). Quando temperatura atual > stack.peek(), pop e calcular diferença de índices. **Código (25 min):** Implementar. **Refletir (5 min):** Por que guardar índices e não valores? |
| 📝 Caderno | **Padrão:** "Monotonic Stack decreasing → próximo maior elemento em O(n). Guardar ÍNDICES na stack, não valores". **Complexidade:** "O(n) tempo — cada elemento é pushed e popped no máximo 1x. O(n) espaço". **Erro:** ___. **Revisão:** reler Dia 15 |

---

## Dia 17 — Fila Circular

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Ler sobre **fila (FIFO)**: primeiro a entrar, primeiro a sair. Fila circular: usar `% capacity` pra evitar desperdício de espaço. `rear = (rear + 1) % capacity`. Abrir [visualgo.net/list](https://visualgo.net/en/list) → Queue |
| 🔵 C | Criar `queue.c`: `typedef struct { int* data; int front; int rear; int size; int capacity; } Queue;`. Implementar: `create`, `enqueue` (insere no rear), `dequeue` (remove do front), `front_value`, `is_empty`, `is_full`. O truque: `rear = (rear + 1) % capacity`. Testar: enqueue 1,2,3 → dequeue=1 → enqueue 4 → dequeue=2 |
| 🟩 Java | **Papel (5 min):** Ler [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/). Truque: stack_in recebe pushes, stack_out serve pops. Quando stack_out vazia, transferir tudo de stack_in pra stack_out (inverte a ordem). **Código (25 min):** Implementar. **Refletir (5 min):** Qual a complexidade amortizada do dequeue? O(1) amortizado |
| 📝 Caderno | **Padrão:** "Fila circular → `% capacity` pra wrap-around. Evita shift de O(n)". **Padrão 2:** "2 stacks → simular fila. Amortized O(1)". **Complexidade:** "Todas ops da fila: O(1)". **Revisão:** reler Dia 16 + escrever `push` e `pop` da stack de cabeça |

---

## Dia 18 — BFS com Fila + Áudio 🎙️

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Ler sobre **BFS (Breadth-First Search)**: explora nível por nível usando fila. Enfileira o root, desenfileira, enfileira os filhos. Garante menor caminho em grafos sem peso. Diferença de DFS: DFS vai fundo primeiro (usa stack/recursão), BFS vai largo primeiro (usa fila) |
| 🔵 C | Usar seu `queue.c` pra implementar BFS numa árvore representada como array: `{1, 2, 3, 4, 5, 6, 7}` onde filhos de i são `2i+1` e `2i+2`. Imprimir na ordem BFS: `1, 2, 3, 4, 5, 6, 7` |
| 🟩 Java | **Papel (5 min):** Ler [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/). BFS com Queue, mas agrupar por nível: antes do loop interno, `int size = queue.size()`. Loop `size` vezes = 1 nível. **Código (25 min):** Implementar. **Refletir (5 min):** O truque do `size` é universal pra qualquer BFS "por nível" |
| 📝 Caderno | ⚠️ **ÁUDIO (substitui revisão):** Gravar 3 min: "O que é pilha vs fila, quando usar cada, e como BFS usa fila". Ouvir. Anotar falhas |

---

## 🏁 Teste de Maestria — Semana 3 (Domingo, 30 min)

| Teste | Tempo | Passou? |
|---|---|---|
| Implementar pilha (array) + fila circular em C no papel | 12 min | ☐ |
| Avaliar `3 4 + 5 *` usando stack no papel, mostrando cada passo | 3 min | ☐ |
| Resolver [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) em Java no papel | 8 min | ☐ |
| Explicar: "O que é Monotonic Stack? Pra que serve? Complexidade?" | 2 min | ☐ |
| **REVISÃO:** Resolver [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) em Java no papel | 3 min | ☐ |

**Problemas LeetCode acumulados: ~20** ✓

---

# ═══════════════════════════════════════
# SEMANA 4 — Árvores Binárias e BST
# ═══════════════════════════════════════

> O salto de complexidade. Tudo é recursão. Se dominar recursão em árvore, domina 90% dos problemas.

---

## Dia 19 — TreeNode + Insert BST + Inorder

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Ler sobre **BST (Binary Search Tree)**: pra cada nó, todos à esquerda são menores, todos à direita são maiores. Inserção: comparar com root, ir pra esquerda ou direita recursivamente. **Inorder traversal de BST = array ordenado.** Abrir [visualgo.net/bst](https://visualgo.net/en/bst), inserir `50, 30, 70, 20, 40, 60, 80` e assistir |
| 🔵 C | Criar `bst.c`: `typedef struct TreeNode { int data; struct TreeNode *left, *right; } TreeNode;`. Implementar: `TreeNode* create_node(int val)`, `TreeNode* insert(TreeNode* root, int val)` — recursivo: se root NULL, cria nó. Se val < root->data, insere à esquerda. Senão, à direita. `void inorder(TreeNode* root)` — esquerda, print, direita. Testar: inserir `{50,30,70,20,40,60,80}`, inorder = `20 30 40 50 60 70 80` |
| 🟩 Java | **Papel (5 min):** Ler [104. Maximum Depth](https://leetcode.com/problems/maximum-depth-of-binary-tree/). Pensar recursivamente: profundidade = 1 + max(profundidade_esq, profundidade_dir). Caso base: null → 0. **Código (25 min):** Implementar. 3 linhas de código. **Refletir (5 min):** Essa é a ESSÊNCIA de problemas de árvore: "o que o nó precisa saber dos filhos?" |
| 📝 Caderno | **Padrão:** "Problemas de árvore = recursão. Perguntar: o que o nó atual precisa retornar pro pai?". **Complexidade:** "Insert BST: O(h) onde h = altura. Melhor caso O(log n), pior caso O(n) se degenerada". **Revisão:** escrever `enqueue` e `dequeue` da fila circular de cabeça |

---

## Dia 20 — Todas as Travessias + Search + Min/Max

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | As 3 travessias: **Inorder (E-R-D)** = ordenado em BST. **Preorder (R-E-D)** = serializar árvore. **Postorder (E-D-R)** = deletar árvore (filhos antes do pai). Decorar: In = "dentro" (raiz no meio), Pre = "antes" (raiz primeiro), Post = "depois" (raiz último) |
| 🔵 C | Adicionar ao `bst.c`: `void preorder(TreeNode* root)`, `void postorder(TreeNode* root)`, `TreeNode* search(TreeNode* root, int val)` — retorna o nó ou NULL, `TreeNode* find_min(TreeNode* root)` — vai sempre pra esquerda, `TreeNode* find_max(TreeNode* root)` — vai sempre pra direita. Testar tudo na árvore `{50,30,70,20,40,60,80}` |
| 🟩 Java | **Papel (5 min):** Ler [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/). Recursão: trocar left e right, depois inverter os filhos. 3 linhas. Desenhar antes e depois. **Código (20 min):** Implementar. **Depois (10 min):** Resolver [100. Same Tree](https://leetcode.com/problems/same-tree/) — comparar recursivamente |
| 📝 Caderno | **As 3 travessias com a árvore do dia:** escrever a sequência de cada uma. Inorder: `20,30,40,50,60,70,80`. Preorder: `50,30,20,40,70,60,80`. Postorder: `20,40,30,60,80,70,50`. **Revisão:** reler Dia 19 |

---

## Dia 21 — Delete BST (O Mais Difícil) 🖊️

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Os **3 casos de delete** em BST: (1) Nó é folha → remove direto. (2) Nó tem 1 filho → substitui pelo filho. (3) Nó tem 2 filhos → encontra **sucessor inorder** (menor da subárvore direita), copia o valor, deleta o sucessor. Desenhar cada caso no papel |
| 🔵 C | ⚠️ **TRACING PRIMEIRO (10 min).** Árvore `{50,30,70,20,40,60,80}`. No papel: (1) Deletar 20 (folha) — desenhar resultado. (2) Deletar 30 (2 filhos) — encontrar sucessor inorder (40), copiar, deletar 40. Desenhar resultado. **DEPOIS (20 min):** Implementar `TreeNode* delete_node(TreeNode* root, int val)`. Testar os 3 casos + deletar a raiz |
| 🟩 Java | **Papel (5 min):** Ler [98. Validate BST](https://leetcode.com/problems/validate-binary-search-tree/). ⚠️ ARMADILHA: NÃO basta checar `left < root < right` — precisa checar contra limites globais. Abordagem: `isValid(node, min, max)`. **Código (25 min):** Implementar com `long` nos limites (evitar overflow). **Refletir (5 min):** Por que usar `Long.MIN_VALUE` e `Long.MAX_VALUE`? |
| 📝 Caderno | **Os 3 casos de delete:** desenhar cada um. **Padrão:** "Validate BST → passar range (min, max) pra baixo na recursão, não comparar só pai-filho". **Complexidade:** "Delete BST: O(h). Validate: O(n)". **Revisão:** reler Dia 20 + escrever `push` e `pop` da pilha de cabeça |

---

## Dia 22 — BST Prática Intensa

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Revisar: por que BST pode degenerar pra O(n)? Quando todos os elementos são inseridos em ordem crescente, a árvore vira uma lista. Solução: árvores balanceadas (AVL, Red-Black). Preview pro que vem na Semana 5 |
| 🔵 C | **TESTE CRONOMETRADO:** Arquivo novo `bst_v2.c`. Reimplementar do zero sem consulta: `create_node`, `insert`, `inorder`, `search`, `find_min`, `delete_node`. Anotar tempo. Meta: < 20 min |
| 🟩 Java | **Papel (5 min):** Ler [230. Kth Smallest in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/). Insight: inorder de BST = sorted. Fazer inorder traversal, contar até k. **Código (20 min):** Implementar. **Depois (10 min):** [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) — diâmetro = max(esq+dir) em qualquer nó |
| 📝 Caderno | **Tempo da reimplementação:** ___ min. **Padrão:** "Kth smallest em BST → inorder = sorted, k-ésimo da traversal". **Padrão:** "Diâmetro = em cada nó, somar altura_esq + altura_dir. Pegar o max global". **Revisão:** reler Dia 21 |

---

## Dia 23 — DFS Patterns + Mais Problemas

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Os **3 padrões de DFS em árvore**: (1) Top-down: passar info do pai pro filho (ex: validate BST). (2) Bottom-up: retornar info do filho pro pai (ex: max depth, diameter). (3) Combine: usar info de ambos os filhos (ex: balanced tree). Classificar mentalmente cada problema que já resolveu |
| 🔵 C | Adicionar ao `bst.c`: `int height(TreeNode* root)` — retorna a altura da árvore. `int count_nodes(TreeNode* root)` — conta total de nós. `void free_tree(TreeNode* root)` — libera toda árvore com postorder (filhos antes do pai, pra não perder referência) |
| 🟩 Java | **Papel (5 min):** Ler [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/). Balanceada = pra TODO nó, |height(left) - height(right)| ≤ 1. **Código (20 min):** Implementar. Otimização: retornar -1 se desbalanceada (early termination). **Depois (10 min):** [235. LCA of BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) — se ambos < root, vai esquerda. Ambos > root, vai direita. Senão, root é o LCA |
| 📝 Caderno | **3 padrões DFS:** escrever e dar 1 exemplo de cada (top-down: validate BST, bottom-up: max depth, combine: balanced tree). **Revisão:** reler Dia 22 + escrever `insert` da BST de cabeça |

---

## Dia 24 — Consolidação Árvores + Áudio 🎙️

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Reler todas as anotações de caderno dos Dias 19-23. Repassar mentalmente: insert, delete (3 casos), 3 travessias, search, min, max, height, validate, kth smallest, diameter, balanced, LCA |
| 🔵 C | **MEGADESAFIO:** Implementar em C uma função `void print_level_order(TreeNode* root)` — imprimir a árvore nível por nível usando SUA fila do Dia 17. Integrar duas estruturas: BST + Queue. Testar com a árvore `{50,30,70,20,40,60,80}` → imprimir: `50 | 30 70 | 20 40 60 80` |
| 🟩 Java | **Revisão LeetCode (35 min):** Refazer 3 problemas de árvore que achou mais difícil, SEM olhar solução anterior. Cronometrar cada um. Se levou mais de 10 min em algum, ele precisa de mais prática |
| 📝 Caderno | ⚠️ **ÁUDIO:** Gravar 3 min: "O que é BST, como funciona insert, os 3 casos de delete, e por que inorder dá ordenado". Ouvir. Anotar falhas |

---

## 🏁 Teste de Maestria — Semana 4 (Domingo, 30 min)

| Teste | Tempo | Passou? |
|---|---|---|
| Implementar BST em C no papel: `insert` + `delete` + `inorder` | 15 min | ☐ |
| Escrever as 3 travessias pra árvore `{8,3,10,1,6,14,4,7,13}` | 3 min | ☐ |
| Resolver [Validate BST](https://leetcode.com/problems/validate-binary-search-tree/) em Java no papel (com range) | 5 min | ☐ |
| Explicar os 3 casos de delete com desenho | 3 min | ☐ |
| **REVISÃO:** Implementar Monotonic Stack pra [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) no papel | 5 min | ☐ |

**Problemas LeetCode acumulados: ~28** ✓

---

# ═══════════════════════════════════════
# SEMANA 5 — AVL + Consolidação Final
# ═══════════════════════════════════════

> O boss final. Rotações são visuais — DESENHAR é obrigatório.

---

## Dia 25 — Conceito AVL + Height + Balance Factor

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Ler sobre **AVL**: BST onde pra todo nó, `|height(left) - height(right)| ≤ 1`. Se violar após inserção, rotacionar. **Balance Factor (BF)** = height(left) - height(right). BF ∈ {-1, 0, 1} = OK. BF = 2 ou -2 = precisa rotacionar. Assistir animação em [visualgo.net/bst](https://visualgo.net/en/bst) → selecionar AVL Tree |
| 🔵 C | Criar `avl.c` copiando a base do `bst.c`. Modificar `TreeNode` pra incluir `int height`. Implementar: `int height(TreeNode* node)` — retorna `node->height` ou 0 se NULL. `int get_balance(TreeNode* node)` — retorna `height(left) - height(right)`. Atualizar `insert` pra recalcular height após inserção: `node->height = 1 + max(height(left), height(right))`. Testar: inserir `{10, 20, 30}` e imprimir BF de cada nó (deve dar -2 no root = desbalanceado). **NÃO rotacionar ainda** — só detectar |
| 🟩 Java | **Papel (5 min):** Ler [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) (refazer). Agora implementar em Java calculando BF exatamente como fez em C. **Código (25 min):** Refazer com a lógica de BF explícito. **Refletir (5 min):** Agora este problema é "verificar se é AVL" |
| 📝 Caderno | **Conceito:** "AVL = BST auto-balanceada. BF = height(E) - height(D). Se |BF| > 1, rotacionar". Desenhar a árvore `{10,20,30}` mostrando o BF de cada nó |

---

## Dia 26 — Rotações Simples (LL e RR)

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | **Rotação LL (Right Rotation):** quando BF = +2 e o filho esquerdo tem BF ≥ 0. O filho esquerdo sobe, o pai desce pra direita. **Rotação RR (Left Rotation):** quando BF = -2 e o filho direito tem BF ≤ 0. O filho direito sobe, o pai desce pra esquerda. **DESENHAR AMBAS NO PAPEL antes de codar** |
| 🔵 C | Implementar em `avl.c`: `TreeNode* rotate_right(TreeNode* y)` — x = y->left, T2 = x->right, x->right = y, y->left = T2, atualizar heights, retornar x. `TreeNode* rotate_left(TreeNode* x)` — espelho. Testar isoladamente: criar nós manualmente, rotacionar, verificar que a árvore ficou correta |
| 🟩 Java | **Papel (5 min):** Ler [108. Convert Sorted Array to BST](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/). Abordagem: pegar o meio como root, metade esquerda = subárvore esquerda, metade direita = subárvore direita. Recursão. **Código (25 min):** Implementar. **Refletir (5 min):** A árvore resultante é balanceada — é basicamente o que AVL faz automaticamente |
| 📝 Caderno | **Desenhar:** Rotação Right (LL) e Left (RR) com antes e depois, mostrando: quem sobe, quem desce, o que acontece com a subárvore "órfã" (T2). **Revisão:** reler Dia 25 + escrever `delete_node` da BST de cabeça |

---

## Dia 27 — Rotações Duplas (LR e RL) 🖊️

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | **Rotação LR:** BF = +2, filho esquerdo tem BF < 0. Primeiro faz Left Rotation no filho esquerdo, depois Right Rotation no nó. **Rotação RL:** BF = -2, filho direito tem BF > 0. Primeiro Right no filho direito, depois Left no nó. São combinações das rotações simples |
| 🔵 C | ⚠️ **TRACING COMPLETO NO PAPEL (15 min):** Inserir na AVL: `{30, 10, 20}`. BF de 30 = +2, BF de 10 = -1 → caso LR. (1) Rotate Left em 10: árvore vira `{30, 20, _, 10}`. (2) Rotate Right em 30: árvore vira `{20, 10, 30}`. Desenhar cada passo. **DEPOIS (15 min):** Modificar `insert` em `avl.c` pra detectar os 4 casos e chamar as rotações corretas. Testar com `{30, 10, 20}` e `{10, 30, 20}` |
| 🟩 Java | **Papel (5 min):** Ler [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/). Pra cada nó de T, verificar se a subárvore a partir dele é idêntica a S. Usar `isSameTree` como helper. **Código (25 min):** Implementar. **Refletir (5 min):** Complexidade O(m×n) — pra cada nó de T, compara com S inteira |
| 📝 Caderno | **Desenhar:** LR e RL com antes, passo intermediário e depois. **Tabela dos 4 casos:** BF=+2, filho BF≥0 → LL (rotate right). BF=+2, filho BF<0 → LR (rotate left + right). BF=-2, filho BF≤0 → RR (rotate left). BF=-2, filho BF>0 → RL (rotate right + left) |

---

## Dia 28 — AVL Insert Completo

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Revisar o fluxo completo do insert AVL: (1) Inserir como BST normal. (2) Subir atualizando heights. (3) Calcular BF. (4) Se |BF| > 1, identificar caso (LL/RR/LR/RL). (5) Rotacionar. (6) Retornar novo root |
| 🔵 C | Testar `insert` da AVL com sequências que forçam todos os 4 casos: `{10,20,30}` (RR), `{30,20,10}` (LL), `{30,10,20}` (LR), `{10,30,20}` (RL). Após cada inserção, fazer inorder E verificar que BF de todo nó está em {-1,0,1}. Implementar `void verify_avl(TreeNode* root)` que checa isso automaticamente |
| 🟩 Java | **Papel (5 min):** Ler [105. Construct Binary Tree from Preorder and Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/). Preorder[0] = root. Achar root em inorder → tudo à esquerda = subárvore esquerda, tudo à direita = subárvore direita. Recursão. **Código (25 min):** Implementar. Usar HashMap pra encontrar índice em inorder em O(1) |
| 📝 Caderno | **Fluxo AVL insert (pseudocódigo):** escrever o algoritmo completo em 10 linhas de pseudocódigo. **Revisão:** reler Dia 27 + escrever `rotate_right` de cabeça |

---

## Dia 29 — Reimplementação AVL + Revisão Geral

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Fazer uma **tabela comparativa** de TUDO: Array vs Lista vs Pilha vs Fila vs BST vs AVL vs Hash. Colunas: Insert, Delete, Search, complexidade de cada, quando usar |
| 🔵 C | **TESTE CRONOMETRADO:** Arquivo novo `avl_v2.c`. Reimplementar do zero: `create_node` (com height), `height`, `get_balance`, `rotate_right`, `rotate_left`, `insert` (com rebalanceamento). Anotar tempo. Meta: < 25 min |
| 🟩 Java | **Revisão Geral (35 min):** Resolver 3 problemas aleatórios de semanas anteriores sem olhar solução: 1 de array/string, 1 de lista, 1 de stack. Cronometrar cada. Meta: < 8 min cada |
| 📝 Caderno | **Tabela comparativa completa.** **Tempo da reimplementação AVL:** ___ min. Se > 25 min, repetir amanhã |

---

## Dia 30 — Consolidação Final + Áudio 🎙️

| Bloco | Tarefa exata |
|---|---|
| 📖 Conceito | Reler TODAS as anotações do caderno, Dia 1 ao 29. Marcar com ★ os padrões mais importantes. Criar uma "cola pessoal" de 1 página com os top 10 padrões |
| 🔵 C | **DESAFIO FINAL:** Implementar `print_level_order` na AVL usando sua fila. Inserir `{50,30,70,20,40,60,80,10,25}` na AVL, verificar que está balanceada, imprimir nível por nível |
| 🟩 Java | **Mock Interview (35 min):** Escolher 1 Easy + 1 Medium aleatórios no LeetCode (tags: Tree ou Stack ou LinkedList). Cronômetro de 35 min. Resolver sem consulta. Simular entrevista: falar em voz alta enquanto resolve |
| 📝 Caderno | ⚠️ **ÁUDIO FINAL:** Gravar 5 min explicando: "Todas as estruturas que domino: array, lista, pilha, fila, BST, AVL. Pra cada uma: o que é, quando usar, complexidade". Este é seu teste final de maestria. Se explicou tudo fluentemente = **MAESTRIA ALCANÇADA** |

---

## 🏁 Teste de Maestria Final (Domingo, 45 min)

| Teste | Tempo | Passou? |
|---|---|---|
| Implementar BST com insert + delete + inorder em C no papel | 15 min | ☐ |
| Desenhar as 4 rotações AVL (LL, RR, LR, RL) com antes e depois | 5 min | ☐ |
| Resolver 1 Easy + 1 Medium aleatório de árvore em Java no papel | 12 min | ☐ |
| Tabela de complexidade: insert/delete/search pra Array, Lista, Stack, Queue, BST, AVL | 3 min | ☐ |
| Explicar em voz alta: "Array vs Lista vs BST — quando usar cada? Complexidade?" | 3 min | ☐ |
| **REVISÃO:** Implementar pilha OU fila em C no papel | 5 min | ☐ |

**Passou em 5/6? MAESTRIA ALCANÇADA.** ✅

---

## 📊 Números Finais

| Métrica | Total |
|---|---|
| Dias de estudo | 30 |
| Horas investidas | 45 horas (1h30 × 30) |
| Problemas LeetCode | ~32-35 |
| Estruturas implementadas em C | 8 (array dinâmico, string, lista simples, lista dupla, pilha, fila, BST, AVL) |
| Algoritmos em C | 3 (Merge Sort, Binary Search, BFS) |
| Reimplementações sem consulta | 5 (lista, pilha, fila, BST, AVL) |
| Áudios de ensino gravados | 4 |
| Tracings manuais | 4 |
| Testes de maestria | 5 |

---

## Quando Estou Pronto?

```
Passou teste Semana 1-3  →  Monitor de EDA: estruturas lineares ✅
Passou teste Semana 4    →  Monitor de EDA: árvores ✅
Passou teste Semana 5    →  Entrevista técnica de Júnior ✅
Passou teste Final       →  MAESTRIA ✅
```
