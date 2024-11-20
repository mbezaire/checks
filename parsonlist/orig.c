// Author:
// Template from Dr Bezaire
// Create, print, and free a Linked List
// TODO: First, unscramble these lines and fix their indentation
// so that the code compiles and runs without valgrind errors
// NEXT: try the suggestions in the 2 comments - what happens? why?
// LAST: submit your code: submit50 mbezaire/checks/main/parsonlist

int main(void) {

#include <string.h>
#include <stdio.h>
}
ppl = ppl->next;
void freeall(node *ppl) {
printf("%s: %i\n", ppl->name, ppl->num);
int num;
if (datafile == NULL)
}
print(start);
typedef struct node_t {
struct node_t *next;
{
while(fscanf(datafile, "%s %i\n", name, &num) != EOF) {
return 1;

tmp = newn;
}
if (ppl->next != NULL)
int num;
fclose(datafile);
tmp->next = newn;
tmp = newn;
while (ppl != NULL) {
if (start == NULL) {
if (ppl == NULL)
node *start = NULL, *tmp;

freeall(ppl->next);
char name[10]; // what if we declared using `char *name;` instead?
}
start = newn;
tmp->next = NULL;
} node;

node *newn = malloc(sizeof(node));
}
freeall(start);
}
char name[10];
}
printf("Error: file not found\n");
return;
strcpy(newn->name,name); // what if we used `newn->name = name` instead?
FILE *datafile = fopen("data.txt", "r");
newn->num = num;

void print(node *ppl) {

free(ppl);
#include <stdlib.h>
