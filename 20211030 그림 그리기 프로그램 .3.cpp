//그림 그리기 프로그램 
#include <stdio.h>

int main()
{
	int i,j;
	
	for(i=1;i<=9;i++)
	{
		for(j=1;j<=9;j++)
		{
			if(i==1 || i==9 || j==1 || j==9)
				printf("*");
			else
				printf(" ");
		}
		putchar('\n');
	}
	return 0;
}
