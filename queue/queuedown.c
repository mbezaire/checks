#include "queue.h"
#include <stdio.h>
#include <cs50.h>

int main(void)
{
	queue myarray;
	myarray.front = 0;
	myarray.size = 0;
	
	enqueue(&myarray,1);
	enqueue(&myarray,2);
	enqueue(&myarray,3);
	enqueue(&myarray,4);
	enqueue(&myarray,5);
	int x = dequeue(&myarray);
	int y = dequeue(&myarray);
	enqueue(&myarray,6);
	enqueue(&myarray,7);
	int z = dequeue(&myarray);
	
	printf("front:%i size:%i dequeued:%i %i %i in queue:", myarray.front, myarray.size, x, y, z)
	for (int i = 0; i < myarray.size; i++) {
    	printf("%i,", myarray.array[i]);
	}
	// front:3 size:4 dequeued:1 2 3 in queue

