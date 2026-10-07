#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv, char** env)
{
    if(argc == 3)
    {
        printf("first arg : %s\n",argv[1]);
        printf("first arg : %s\n",argv[2]);
        int num1 = atoi(argv[1]);
        int num2 = atoi(argv[2]);
        printf("%d\n",num1+num2); 
    }
    else
    {
        printf("bad arguments\n");
        return 0;
    }
    
}