#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    char str1[12];

    printf("\nEnter a buffer values\n");
    scanf("%s", str1);
    char* ret = strstr(str1, "aaaa");
    printf("%s\n", ret);
    printf("Passed!\n");
    return 0;
}
