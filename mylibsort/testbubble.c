#include "mylib.h"
#include <stdio.h>
#include <cs50.h>

int main(void)
{
	int myarray[] = {9,4,7,3,1};
	int otherarray[] = {3,1,8,4,7,3,1};
	bubblesort(otherarray);
    for (int i = 0; i < 7; i++)
      printf("%i,", otherarray[i]);
}
