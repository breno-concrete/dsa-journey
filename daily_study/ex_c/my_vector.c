#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
    int* data;
    int size;
    int capacity;
} Vector;



Vector* create(int initial_capacity){
    if(initial_capacity <= 0){
        return NULL;
    }

    Vector* v = (Vector*) malloc(sizeof(Vector));
    if(v == NULL){
        return NULL;
    }

    v->data = (int*) malloc(initial_capacity * sizeof(int));
    if(v->data == NULL){
        free(v);
        return NULL;
    }

    v->size = 0;
    v->capacity = initial_capacity;

    return v;
}

void push(Vector* v, int value){
    if(v->size == v->capacity){
        int newCapacity = v->capacity*2;

        int* newData = realloc(v->data, newCapacity*sizeof(int));

        if(newData == NULL){
            return;
        }

        v->data = newData;
        v->capacity = newCapacity;
    }

    v->data[v->size] = value;
    v->size++;
}


void print(Vector* v){
    printf("Data:\n");
    for(int i = 0; i < v->size; i++){
        printf("%d ", v->data[i]);
    }
}




int main(void) {

    Vector* v1;
    v1 = create(2);

    push(v1, 1);
    push(v1, 2);
    push(v1, 3);
    push(v1, 4);
    push(v1, 5);

    print(v1);


    free(v1->data);
    free(v1);

    return 0;
}