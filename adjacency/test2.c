#include "adjacency.c"
#include <stdio.h>


/*
3 4 3 2
4 5 4 2
4 4 4 1
2 2 3 1
*/
void adjc(int tbl[4][4], int (*adjtbl)[4]);

int main(void) {
    int table[4][4]  =

                     {{0, 0, 0, 0},

                     {0, 1, 1, 1},

                     {0, 1, 1, 1},

                     {0, 1, 1, 1}};

    int adj[4][4];

    adjacency(table, adj);

    int i = 0;
    while (i < 16) {
        printf("%i", adj[i/4][i%4]);
        i++;
    }
    printf("\n");

}

