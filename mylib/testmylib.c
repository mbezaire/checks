#include "mylib.c"
#include <stdio.h>
#include <cs50.h>

int main(void)
{
	char letter =  get_char("Enter a letter");
	int result = isvowel(letter);
	result = isconsonant(letter);
	printf("okay\n");

}
