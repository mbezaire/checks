#include "mylib.h"
#include <stdio.h>
#include <cs50.h>

int main(void)
{
	int myarray[] = {9,4,7,3,1};
	int otherarray[] = {3,1,8,4,7,3,1};
	selectionsort(myarray, 5); //    bubblesort(otherarray);
   for (int i = 0; i < 5; i++)
      printf("%i,", myarray[i]);
}
