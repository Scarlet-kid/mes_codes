#include <stdio.h>

float main(void)
{
    float res;
    printf("Saisir une valeur réelle :");
    scanf("%f",&res);
    if (res<0)
    {
        printf("La valeur absolue du nombre est %f\n",-res);
    }
    else
    {
        printf("La valeur absolue du nombre est %f\n",res);
    }
}

// int main(void){
//   float val;
//   printf("Saisir une valeur réelle:");
//   scanf("%f",&val);
//   if (val<0){
//     printf("%f\n",-val);
//   }
//   else{
//       printf("%f\n",val);
//   }
//   return 0;
// }

