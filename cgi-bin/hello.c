#include <stdio.h>
main () {
  printf ("Content-type:text/html; charset=utf-8 \n\n" );  /* double \n\n */
  printf ( "<!DOCTYPE html>\n" );
  printf ( "<html>\n" );
  printf ( " <head><title>Bonjour</title></head>\n" );
  printf ( " <body>\n" );
  printf ( "   Hello <b>Web</b>\n" );
  printf ( " </body> \n" );
  printf ( "</html>\n" );
}
