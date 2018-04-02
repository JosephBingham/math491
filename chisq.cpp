#include<iostream>
#include<stdlib.h>
#include<math.h>
#define SIZE 256

double chi2cdf(double sum, double k)
{
	return sum + k;	
}


double chisq(int B[SIZE][SIZE])
{
	int counts[SIZE] = {0};
	for ( int i = 0; i < SIZE; i++)
	{
		counts[B[i][1] + 1]++;
	}
	double hist1[128] = {0};
	double hist2[128] = {0};
	for ( int i = 0; i < 128; i++)
	{
		hist1[i] = -1*counts[2*i];
		hist2[i] = (counts[2*i] + counts[2*i -1])/2.0;
	}
	int k = 128;
	int m = 1;
	while (hist2[m] < 5)
	{
		hist1[m+1] += hist1[m];
		hist2[m+1] += hist2[m];
		hist1[m] = 1;
		hist2[m] = -1;
		m += 1;
		k -= 1;
	}
	for ( int i = (128 - k); i < 128; i++) 
	{
		if (hist2[i] < 5)
		{
			hist1[i] += hist1[i - 1];
			hist2[i] += hist2[i - 1];
			hist1[i-1] = 1;
			hist2[i-1] = -1;
		}
	}
	double sum = 0;
	for(int i = 0; i < 128; i++)
	{
		sum += (pow(hist1[i] + hist2[i], 2))/hist2[i];
	}
	return 1 - (chi2cdf(sum,k-1));
}

int main(void)
{
	return 0;
}