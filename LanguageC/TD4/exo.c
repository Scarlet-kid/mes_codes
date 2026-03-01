#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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

int my_strcmp(const char *s1, const char *s2)
{
  int i = 0;
  while (s1[i] != '\0' && s2[i] != '\0')
  {
    if (s1[i] != s2[i])
    {
      return s1[i]- s2[i];
    }
    i++;
  }
  return s1[i]- s2[i];
}

char* my_strcat(char *str1, int size1, char *str2,int size2)
{
  char* str3;
  str3 = (char*)(malloc(sizeof(char*)*(size1+size2+1)));
  for(int i = 0;i<size1;i++)
  {
    str3[i]=str1[i];
  }
  for(int j=size1;j<=size2;j++)
  {
    str3[j]=str2[j];
  }
  str3[size1+size2+1] = '\0';
  return str3;
}

int main()
{
  // char chaine[80];
  // printf("Saisir une chaine :");
  // myGets(chaine,79);
  //printf("%s a %d caractere(s)\n",chaine,strlong(chaine));
  // char ch2[30];
  // my_strcpy(ch2,chaine);
  // printf("chaine1 = %s et chaine2 = %s\n",chaine,ch2);
  char ch1[5] = "walut";
  char ch2[5] = "salut";
  //printf("%d\n",my_strcmp(ch1,ch2));
  printf("%s\n",my_strcat(ch1,5,ch2,5));
  return 0;
}
