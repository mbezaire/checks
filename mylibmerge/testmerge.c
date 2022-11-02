#include "mylib.h"
#include <stdio.h>
#include <cs50.h>

int main(void)
{
	int myarray[] = {9,4,7,3,1};
	int otherarray[] = {3,1,8,4,7,3,1,5,0,13,-1};
	mergesort(otherarray, 11);
    for (int i = 0; i < 11; i++)
      printf("%i,", otherarray[i]);
}
