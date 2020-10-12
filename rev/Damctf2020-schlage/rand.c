#include <stdio.h>
#include <stdlib.h>

int main()
{
int seed_value = 0;
	puts("give me a seed value\n");
	scanf("%d", &seed_value); //seed value passed here from pin2
	srand(seed_value);
	printf("%d\n", rand()); //used for pin2
	printf("%d\n", rand()); //used for pin4

	return 0;
}
