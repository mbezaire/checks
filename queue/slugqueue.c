#include "queue.h"
#include <stdio.h>
#include <cs50.h>

int main(void)
{
	queue myarray;
	myarray.front = 0;
	myarray.size = 0;
	
	enqueue(&myarray,5);
	dequeue(&myarray);
	printf("okay\n");
}
