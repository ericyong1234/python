//2진수 변산 프로그램 
#include <stdio.h>

//양의 정수 n의 이진수를 출력하는 재귀적 함수
void binary(int n)
{
	if(n>1)
	{
		binary(n/2);
		printf("%d", n%2);
	}
	else
		printf("%d", n%2);
}
int main()
{
	int n;
	printf("2진수로 표시할 정수는?");
	scanf("%d",&n);
	
	binary(n);
	
	return 0;	
}
