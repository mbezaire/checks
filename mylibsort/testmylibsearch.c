#include "mylib.h"
#include <stdio.h>
#include <cs50.h>

int main(void)
{
	int myarray[] = {5,1,2,3,4};
	int otherarray[] = {12,4,6,8,10};
	decimal mynumber;
	bool ans = linsearch(5,myarray,5);
    ans = binsearch(12,otherarray,5);
	printf("okay\n");
}



