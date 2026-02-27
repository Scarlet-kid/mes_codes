#include <stdio.h>
#include <string.h>

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

char* my_strcpy(char *dest, const char *src)
{
  int i = 0;
  while (src[i] != '\0')
  {
    dest[i] = src[i];
    i++;
  }
  dest[i] = '\0';
  return dest;
}

int main()
{
  char chaine[80];
  printf("Saisir une chaine :");
  myGets(chaine,79);
  //printf("%s a %d caractere(s)\n",chaine,strlong(chaine));
  char ch2[30];
  printf("chaine1 = %s et chaine2 = %s\n",chaine,my_strcpy(chaine,ch2));
  return 0;
}
