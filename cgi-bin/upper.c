#include <stdio.h>
void main() {
   int  c;
  printf("Content-type: text/plain\n\n");   /* ne pas oublier */
   while ((c = getchar()) != EOF)
          if (islower(c))
                  putchar(c - 32);
         else
                  putchar(c);
}
