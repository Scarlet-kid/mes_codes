#include <stdio.h>
float main(){
  float res;
  float somme = 0.0;
  int i = 0;
  _Bool fini = 0;
  while(!fini){
    printf("Saisir des valeurs:");
    scanf("%f",&res);
    if(res>=0)
    {
      i++;
      somme = somme + res;
    }
    else
    {
      printf("les valeurs positifs: %i\n",i);
      printf("La valeur moyenne: %f\n",1.0*somme/i);
      fini = 1;
    }
  }
}
