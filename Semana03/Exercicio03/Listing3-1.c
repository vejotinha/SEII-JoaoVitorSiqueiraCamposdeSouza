#include <stdio.h>
#include <unistd.h>

int main ()
{
    print("The process ID is %d\n", (int) getpid());
    print("The parent process ID is %d\n", (int) getppid());
    return 0;
}