#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    if(argc != 2) {
        printf("\n Usage: ./strncmp arg1\n arg1 is a int type\n");
        return 0;
    }

    char pw[9] = "Passw0rd!";
    char str1[12], str2[10];
    volatile int a = 5;
    volatile int b = atoi(argv[1]);

    if(a > 0) {
        if(a < 10 && b != 3 && (a+b < 15)) {
            printf("\nEnter in two buffer values\n");
            scanf("%s %s", str1, str2);
            char* ret = strstr(str1, "192.168.0.1");
            printf("%s \n", ret);
            if(strncmp(ret, "192.168.0.1", 11) == 0) {
                if(strncmp(str2, "unkown512", 9) == 0) {
                    printf("\nEnter password\n");
                    char user_pw[9];
                    scanf("%s", user_pw);
                    if(strncmp(user_pw, pw, 9) == 0) {
                        printf("\nPassed!\n");
                    }
                }
            }
        }

    }


    return 0;
}
