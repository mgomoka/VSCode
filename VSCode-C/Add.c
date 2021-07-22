#include <stdio.h>

int main() {
    int numberOne, numberTwo, total;

    printf("Enter First Integer: ");
    scanf("%d", &numberOne);

    printf("Enter Second Integer: ");
    scanf("%d", &numberTwo);

    total = numberOne + numberTwo;
    printf("%d + %d = %d\n", numberOne, numberTwo, total);

    return 0;
}
