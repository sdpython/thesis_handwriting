#include "stdio.h"
#include "stdlib.h"
#include "string.h"

void main (int argc, char * argv []) 
{
  char * tempo [3] ;
  if (argc <= 1) {
    argc = 2 ;
    argv = tempo ;
    tempo [0] = "upper_index" ;
    tempo [1] = "C:\\Documents and Settings\\Dupré\\Mes documents\\recherche\\these\\bibliographie\\bibliographie.idx" ;
  }

  int i ;
  for (i = 0 ; i < argc ; ++i) {
    printf ("argument %d :\t - %s -\n", i, argv [i]) ;
  }

  FILE * f = fopen (argv [1], "r") ;
  if (f == NULL) {
    printf ("unable to open file %s\n", argv [1]) ;
    return ;
  }

  int pos = ftell (f) ;
  fseek (f, 0, SEEK_END) ;
  pos = ftell (f)  - pos ;
  fseek (f, 0, SEEK_SET) ;

  printf ("taille du fichier %d\n", pos) ;

  char * buffer = new char [pos + 100] ;
  char * place = buffer ;
  char * line = fgets (place, (int) (buffer + pos + 100 - place - 1), f) ;
  char * p ;
  int nb_line = 0 ;
  while (line != NULL) {

    ++nb_line ;
    
    p = strstr (line, "@") ;
    if (p != NULL) {
      for ( ; (*p != '{') &&(p > line) ; --p) {
        switch (*p) {
          case 'é' : case 'è' : case 'ê' :  *p = 'e' ; break ;
          case 'ù' : case 'û' :             *p = 'u' ; break ;
          case 'à' : case 'â' :             *p = 'a' ; break ;
          case 'î' :                        *p = 'i' ; break ;
          case 'ô' :                        *p = 'o' ; break ;
          default : break ;
        }
      }
    }

    p = strstr (line, "@") ;
    if (p != NULL) {
      line = p + 1 ;
      p = strstr (line, "@") ;

      if (p != NULL) {
        for ( ; (*p != '{') && (*p != '!') && (p > line) ; --p) {
          switch (*p) {
            case 'é' : case 'è' : case 'ê' :  *p = 'e' ; break ;
            case 'ù' : case 'û' :             *p = 'u' ; break ;
            case 'à' : case 'â' :             *p = 'a' ; break ;
            case 'î' :                        *p = 'i' ; break ;
            case 'ô' :                        *p = 'o' ; break ;
            default : break ;
          }
        }
      }
    }

    place += strlen (place) ;
    line = fgets (place, (int) (buffer + pos + 100 - place - 1), f) ;
  }
  
  fclose (f) ;

  printf ("écriture du fichier %s\n", argv [1]) ;
  printf ("ligne %d\n", nb_line) ;

  f = fopen (argv [1], "w") ;
  fprintf (f, "%s", buffer) ;
  fclose (f) ;
  delete [] buffer ;
}
