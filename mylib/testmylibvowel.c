#include "mylib.c"
#include <stdio.h>

int main(void)
{
	char letter =  get_char("Enter a letter");
	int result = isvowel(letter);
	printf("%d\n", result);

}
