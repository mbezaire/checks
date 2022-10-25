#include "mylib.h"
#include <stdio.h>
#include <cs50.h>

int main(void)
{
	int myarray[] = {5,1,2,3,4};
	int otherarray[] = {12,4,6,8,10};
	int checkfor = get_int("Enter an integer: ");
	bool ans = binsearch(checkfor,otherarray,5);
    //ans = binsearch(12,otherarray,5);
    if (ans)
        printf("true\n");
    else
        printf("false\n");
}


