#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int my_strlen(char *s){
    int count = 0;

    while(*s != '\0'){
        count++;
        s++;
    }

    return count;
}

int my_strcmp(char *s1, char *s2){


    while(*s1 != '\0' && *s1 == *s2){
        s1++;
        s2++;
    }

    return *s1 - *s2;
}

int main(void) {
    




    return 0;
}