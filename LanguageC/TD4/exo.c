#include <stdio.h>

void myGets(char *s,int tmax)
{
    int i;
    fgets(s, tmax, stdin);
    if(s[strlen(s)-1] == '\n') 
    {
        s[strlen(s)-1] = '\0'; // Quand on trouve un saut de ligne fin alors on marque la fin.
    }
}


int strlong(char * s)
{
  int i;
  i=0;
  while(s[i] != '\0')
  {
    i++;
  }
  return i;
}

int main()
{
  char chaine[80];
  printf("Saisir une chaine :");
  myGets(chaine,79);
  printf("%s a %d caractere(s)\n",chaine,strlong(chaine));
  return 0;
}
