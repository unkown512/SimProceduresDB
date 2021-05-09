#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(int argc, char* argv[]) {
    // Two buffers expected
    char str1[9], str2[9];
    printf("\nEnter in two inputs\n");

    scanf("%s %s", str1, str2);

    printf("\n str1 = %s \n", str1);
    printf("\n str1 = %s \n", str2);

    printf("Passed!\n");

    return 0;
}
