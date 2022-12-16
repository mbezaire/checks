#include "queue.h"
#include <stdio.h>
#include <cs50.h>

int main(void)
{
	queue myarray;
	myarray.front = 0;
	myarray.size = 0;

	enqueue(&myarray,5);
	enqueue(&myarray,3);
	enqueue(&myarray,1);
	enqueue(&myarray,2);

	printf("front:%i size:%i in queue:", myarray.front, myarray.size);
	for (int i = 0; i < myarray.size; i++) {
    	printf("%i,", myarray.array[i]);
	}
	// 0 4:5,3,1,2,
}
