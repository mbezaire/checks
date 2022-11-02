#include "mylib.h"
#include <stdio.h>
#include <cs50.h>

int main(void)
{
	int myarray[] = {9,4,7,3,1};
	int otherarray[] = {3,1,8,4,7,3,1};
	mergesort(myarray, 5);
   	mergesort(otherarray, 7);
	printf("okay\n");
}
