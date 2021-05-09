#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    if(argc != 2) {
        printf("\n Usage: ./strncmp arg1\n");
        return 0;
    }

    char password[9] = "Passw0rd!";

    int result = strncmp(password, argv[1], 9);

    if(result == 0) {
        printf("\nPassed!\n\n");
        return 0;
    } 
    return 0;
}
