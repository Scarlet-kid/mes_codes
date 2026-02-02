#include <stdio.h>
#include "biblio.h"
int main()
{
float notes[3] = {12.5, 10.5, 6.5} ;
float mean = moyenne(notes,3) ;
printf("la moyenne = %f\n", mean);
return 0 ;
}