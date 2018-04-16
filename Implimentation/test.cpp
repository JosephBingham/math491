#include<iostream>
#include<stdlib.h>
using namespace std;
int main(void)
{
FILE *file = fopen("/Users/user/Desktop/math491/stego06_0512.png","r");
if(file == NULL)
{
	cout << "fuck" << endl;
}
char a;
while((a = fscanf(file,"l")) != EOF)
{
	printf("%d", a);
}
}
