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
    v->capacity = initial_capacity

    return v;


int main(void) {
    
    return 0;
}