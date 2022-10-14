#include "mylib.h"
#include <stdio.h>
#include <cs50.h>

int main(void)
{
	char letter =  get_char("Enter a letter");
	int result = isconsonant(letter);
	printf("%d\n", result);

}
