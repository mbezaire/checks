#include "nametree.c"

int main(void) {

    // lets read in from our file, names.csv
    char filename[] = "names.csv"; // hardcode is fine
    FILE *file = fopen(filename, "r");

    node *start = NULL;
    // now that we are using NULL as a starting value, make sure you
    // have deleted the start->name[0] business - there is no memory to -> to yet!


    char name[20];  // this is a standalone variable to store
                    // what we read in via the loop

    // we read into the name variable each time
    while (fgets(name, 20, file)) {
        // each name that we read, we'll create a node for
        node *nextname = malloc(sizeof(node));
        strcpy(nextname->name, name);
        nextname->earlier = NULL;
        nextname->later = NULL; // zero-out the pointers!!

        //let's check if we're adding the very first name
        if (start == NULL) {
            start = nextname; // look to add the first one
        } else {
            // traverse to find a new location to add
            traverse(start, nextname);
        }
    }
    fclose(file);
    printf("Enter a name: ");
    fgets(name, 20, stdin);
    int result = search_tree(start, name);
    if (result == 1)
        printf("Found %s\n", name);
    else
        printf("Did not find %s\n", name);
    free_tree(start);
}