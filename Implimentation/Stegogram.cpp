#include<iostream>
#include<stdlib.h>
#include<math.h>
using namespace std;

#ifndef SIZE
#define SIZE 256
#endif

#ifndef IMG_SIZE
#define IMG_SIZE 1024
#endif
const double PI = 3.1415926535897932384626433832795028841971693993751058209749445923;
const double E  = 2.7182818284590452353602874713526624977572470936999595749669676277;
FILE *file = NULL;

/*
	gamm:
	param: double x, input to function
	return: double, the gamma function applied
	implimented using an aproximations
*/
double gamm(double x) 
{
    double ret = (1.000000000190015 + 
                 76.18009172947146  / (x + 1) +  
                 -86.50532032941677 / (x + 2) + 
                 24.01409824083091  / (x + 3) +  
                 -1.231739572450155 / (x + 4) + 
                 1.208650973866179e-3/ (x + 5) + 
                 -5.395239384953e-5 / (x + 6));
    
    return ret * sqrt(2.0*PI)/x * pow(x + 5.5, x+.5) * exp(-x-5.5);
}

/*
	chisqrcdf:
	param: double x, value to test against
		   double n, degree of freedom
	return: double, the chi square cdf
*/
double chisqrcdf(double x, double n) {
	double a = 1/(gamm(n/2.0)*pow(2.0, n/2.0));
	double b = pow(x, (n/2.0) - 1.0);
	double c = pow(E, -x/2.0);
	cout << a << "\n" << b << "\n" << c << endl;
	return a*b*c;
}

/*
	fitness:
	param: int *B, size of SIZE, the model

*/
double fitness(int B[SIZE])
{
	int counts[SIZE] = {0};
	for ( int i = 0; i < SIZE; i++)
	{
		counts[B[i] + 1]++;
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
	return 1 - (chisqrcdf(sum,k-1));
}

typedef struct values
{
	int idx;
	int val;
} VAL_T;

class solution
{
	private:
		VAL_T **values;
		double fitVal;
	
	public:
		void solution()
		{	
			VAL_T  **values = (VAL_T **)malloc(4*sizeof(VAL_T *));
			for(int i = 0; i < 4; i++)
			{
				values[i] = (VAL_T *)malloc(IMG_SIZE/4 *sizeof(VAL_T))
			}
		}
		void mixSolutions(solution other)
		{
			
		}
}


int main(int argc, char *argv[])
{


	cout << chisqrcdf(3,3) << endl;
}
