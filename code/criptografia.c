#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    int a = atoi(argv[1]),
        b = atoi(argv[2]),
        p = atoi(argv[3]);
    int x,y, n=0;
    printf("\n\n");
    for (x=0; x < p; x++)
    {
        for (y = 0; y < p; y++)
        {
            if (y*y % p == (x*x*x+a*x+b) %p)
            {
                n++;
                printf("G%d = ( %d %d )", n,x,y);
            }
        }
    printf("\n\n");
    return 0;
    }
    





}