void trier( int t[], int n)
{
  int tmp;
  int i;
  int j;
  for(i=1;i<=n;i++)
  {
  tmp = t[i];
  j=i;
  while(j>0 && t[j-1]>tmp)
  {
    t[j]=t[j-1];
    j=j-1;
  }
  t[j] = tmp;
  }
}
