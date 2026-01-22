#include <stdio.h>


float mean(float* marks, float* weights, int nb)
{
	float s=0.0, p=0.0;
	for(int i=0; i<nb; i=i+1)
	{
		s = s + marks[i] * weights[i];
		p = p + weights[i];
	}
	return s/p;
}

int main(int argc, char** argv, char **env)
{
	float a[3] = {8.5, 12.75, 9.0};
	float b[3] = {1, 1.5, 0.5};

	float m = mean(a,b,3);
	printf("m = %f\n",m);

	return 0;

}