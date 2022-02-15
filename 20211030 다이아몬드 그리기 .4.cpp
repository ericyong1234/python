//다이아몬드 그리기 
#include <stdio.h>

int main()
{
	int i,j,k;
	
	for(i=1;i<=5;i++)
	{
		for(j=i;j<5;j++)
			printf(" ");
		for(k=1;k<i*2;k++)
			printf("*");
		putchar('\n');
	}
	
	for(i=1;i<5;i++)
	{
		for(j=1;j<i+1;j++)
			printf(" ");
		for(k=0;k<(5-i)*2-1;k++)
			printf("*");
		putchar('\n');
	}
	return 0;
}
